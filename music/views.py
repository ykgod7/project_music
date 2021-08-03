from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from . import models


def mypage(request, username):
    user = get_user_model()
    return render(request, 'mypage.html', {'user': user})


def m_music_rank_like(request):

    info_music = models.Music.objects.all().order_by('-m_like')
    return render(request, 'music_rank.html', {'info_music': info_music, 'select': 'f_like'})


def m_music_rank_title(request):

    info_music = models.Music.objects.all().order_by('m_title')
    return render(request, 'music_rank.html', {'info_music': info_music, 'select': 'f_title'})


def index(request):
    playlists = models.Playlist.objects.all()
    return render(request, 'index.html', {'playlists': playlists})
