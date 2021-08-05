from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

from .forms import MyplayListForm
from . import models
from .models import MyPlaylist, Playlist, Music
import json

def mypage(request, username):
    user = get_user_model()
    return render(request, 'mypage.html', {'user': user})


# music_rank.html :select
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
        if 'next' in request.POST:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect(request.POST.get('next'))
        user = User.objects.get(username=request.user)
        music_key = Music.objects.get(m_title='좋은날')
        myplaylist_pk = request.POST.get('mp_key')
        if (myplaylist_pk == 'new'):
            myplaylist = MyPlaylist.objects.create(mp_name=request.POST.get('mp_name'), user_fk=user)
            playlist = Playlist.objects.create(music_fk=music_key, myplaylist_fk=myplaylist, user_fk=user)
            return HttpResponse(json.dumps({'data': 'success'}))
        else:
            playlist = Playlist.objects.create(music_fk=music_key, myplaylist_fk=MyPlaylist.objects.get(pk=myplaylist_pk), user_fk=user)
        return HttpResponse(json.dumps({'data': 'success'}))
    else:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            myplay_list = models.MyPlaylist.objects.filter(user_fk=user.pk)
            context = {
                'play_list': myplay_list,
            }
        else:
            context = {}
        return render(request, 'music_detail/video.html', context)
