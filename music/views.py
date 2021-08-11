from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from user.forms import PopupLoginForm
from .forms import MyplayListForm
import json
from . import models
from .models import Profile, PlaylistComment, MyPlaylist, Music, Playlist, Artist
from urllib import parse

def index(request):
    return render(request, 'index.html')

def mypage(request):
    user = get_user_model()
    liked_playlist = Profile.objects.filter(user=request.user)
    playlist = MyPlaylist.objects.filter(user_fk=request.user)
    return render(request, 'mypage.html', {'playlist': playlist, 'liked_playlist': liked_playlist})


def mypage_list(request, list_id):
    playlist = MyPlaylist.objects.filter(user_fk=request.user)
    liked_playlist = Profile.objects.filter(user=request.user)
    selected_list = Playlist.objects.filter(myplaylist_fk=list_id)
    return render(request, 'mypage.html', {
        'playlist': playlist,
        'selected_list': selected_list,
        'liked_playlist': liked_playlist,
    })


def delete_music(request, music_id, list_id):
    selected_music = get_object_or_404(Playlist, pk=music_id)
    selected_music.delete()
    return HttpResponseRedirect(reverse('music:mypage_list', args=(list_id,)))


def m_music_rank_like(request):
    info_music = models.Music.objects.all().order_by('-m_like')
    return render(request, 'music_rank.html', {'info_music': info_music, 'select': 'f_like'})


def m_music_rank_title(request):
    info_music = models.Music.objects.all().order_by('m_title')
    return render(request, 'music_rank.html', {'info_music': info_music, 'select': 'f_title'})


def m_list_like(request):
    playlists = models.MyPlaylist.objects.all().order_by('-mp_like')
    return render(request, 'list_rank.html', {'playlists': playlists, 'select': 'l_like'})


def m_list_new(request):
    playlists = models.MyPlaylist.objects.all().order_by('list_pub_date')
    return render(request, 'list_rank.html', {'playlists': playlists, 'select': 'l_new'})


def list_rank(request):
    playlists = models.MyPlaylist.objects.all().order_by('-mp_like')
    return render(request, 'list_rank.html', {'playlists': playlists, 'select': 'l_like'})


def music_video(request, videoId, videoTitle, videoArtist):
    cur_user = request.user
    v_Title = parse.unquote(videoTitle)
    v_Artist = parse.unquote(videoArtist)
    if request.method == 'POST':
        if 'next' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect(request.POST.get('next'))
        user = User.objects.get(username=request.user)
        myplaylist_pk = request.POST.get('mp_key')
        # 가수 -> 곡,영상코드

        try:
            artist_key = Artist.objects.get(a_name=v_Artist)
        except ObjectDoesNotExist:
            artist_key = Artist.objects.create(a_name=v_Artist)
        try:
            music_key = Music.objects.get(m_title=v_Title)
        except:
            music_key = Music.objects.create(m_title=v_Title, m_videoCd=videoId, artist_fk=artist_key)

        if (myplaylist_pk == 'new'):
            myplaylist = MyPlaylist.objects.create(mp_name=request.POST.get('mp_name'), user_fk=user)
            playlist = Playlist.objects.create(music_fk=music_key, myplaylist_fk=myplaylist, user_fk=user)
            return HttpResponse(json.dumps({'data': 'success'}))
        else:
            playlist = Playlist.objects.create(music_fk=music_key,
                                               myplaylist_fk=MyPlaylist.objects.get(pk=myplaylist_pk), user_fk=user)
        return HttpResponse(json.dumps({'data': 'success'}))
    else:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            myplay_list = models.MyPlaylist.objects.filter(user_fk=user.pk)
            context = {
                'play_list': myplay_list,
                'videoId': videoId,
                'videoTitle': v_Title,
                'videoArtist': v_Artist
            }
        else:
            context = {'videoId': videoId,
                       'videoTitle': v_Title,
                       'videoArtist': v_Artist,
                       'form': PopupLoginForm()
                       }
        return render(request, 'music_detail/video.html', context)


def playlist(request, list_id):
    playlists = get_object_or_404(models.MyPlaylist, pk=list_id)
    if request.method == 'POST':
        if 'next' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect(request.POST.get('next'))
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        p_liked = profile.like_playlist.filter(id=list_id)

        if p_liked.exists():
            p_liked = False
        else:
            p_liked = True

        context = {'playlists': playlists, 'p_liked': p_liked}
    else:
        context = {'playlists': playlists, 'p_liked': True, 'form': PopupLoginForm()}
    return render(request, 'playlist.html', context)


@login_required
def playlist_like_toggle(request, playlist_id):
    m_playlist = get_object_or_404(models.MyPlaylist, id=playlist_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    check_like_playlist = profile.like_playlist.filter(id=playlist_id)

    if check_like_playlist.exists():
        profile.like_playlist.remove(m_playlist)
        m_playlist.mp_like -= 1
        m_playlist.save()
    else:
        profile.like_playlist.add(m_playlist)
        m_playlist.mp_like += 1
        m_playlist.save()

    return redirect('music:playlist', playlist_id)


@login_required
def create_comment(request, playlist_id):
    if request.method == 'POST':
        comment = request.POST.get('content')
        playlist = get_object_or_404(models.MyPlaylist, pk=playlist_id)
        user_comment = playlist.playlistcomment_set.filter(user_fk=request.user)

        if user_comment:
            messages.add_message(request, messages.ERROR, '이미 댓글을 등록하셨습니다.')
            return redirect('music:playlist', playlist_id)

        if comment:
            obj = PlaylistComment.objects.create(user_fk=request.user, c_contents=comment, myplaylist_fk=playlist)
            obj.save()

        return redirect('music:playlist', playlist_id)
    else:
        return redirect('music:playlist', playlist_id)


def delete_comment(request, playlist_id):
    playlist = get_object_or_404(models.MyPlaylist, pk=playlist_id)
    user_comment = playlist.playlistcomment_set.filter(user_fk=request.user)
    user_comment.delete()
    return redirect('music:playlist', playlist_id)
