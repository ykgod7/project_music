from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth import get_user_model
from . import models
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import MyplayListForm


def mypage(request, username):
    user = get_user_model()
    return render(request, 'mypage.html', {'user': user})


def m_music_rank_like(request):

    info_music = models.Music.objects.all().order_by('-m_like')
    return render(request, 'music_rank.html', {'info_music': info_music, 'select': 'f_like'})


def m_music_rank_title(request):

    info_music = models.Music.objects.all().order_by('m_title')
    return render(request, 'music_rank.html', {'info_music': info_music, 'select': 'f_title'})


def m_list_like(request):
    playlists = models.MyPlaylist.objects.all().order_by('-mp_like')
    return render(request, 'index.html', {'playlists': playlists, 'select': 'l_like'})


def m_list_new(request):
    playlists = models.MyPlaylist.objects.all().order_by('list_pub_date')
    return render(request, 'index.html', {'playlists': playlists, 'select': 'l_new'})


def music_video(request):
    cur_user = request.user
    if request.method == 'POST':
        return
    else:
        user = User.objects.get(username=request.user)
        play_list = models.Playlist.objects.select_related('myplaylist_fk')
        context = {
            'user': user,
            'play_list': models.Playlist.objects.select_related('myplaylist_fk').filter(user_fk=user),
        }
        return render(request, 'music_detail/video.html', context)


def playlist(request, list_id):
    playlists = get_object_or_404(models.MyPlaylist, pk=list_id)
    user = request.user
    profile = Profile.objects.get(user=user)
    p_liked = profile.like_playlist.filter(id=list_id)
    if p_liked.exists():
        p_liked = False
    else:
        p_liked = True

    context = {'playlists': playlists, 'p_liked': p_liked}
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

