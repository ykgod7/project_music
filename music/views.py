from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from . import models


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


# index.html : select
def m_list_like(request):

    # info_list = models.MyPlaylist.objects.all().order_by('p_like')
    playlists = models.MyPlaylist.objects.all().order_by('p_like')
    return render(request, 'playlist_rank.html', {'playlists': playlists, 'select': 'l_like'})


def m_list_new(request):

    # info_list = models.MyPlaylist.objects.all().order_by('list_pub_date')
    playlists = models.MyPlaylist.objects.all().order_by('list_pub_date')
    return render(request, 'playlist_rank.html', {'playlists': playlists, 'select': 'l_new'})


def index(request):
    return render(request, 'index.html')
