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


# index.html : select
def m_list_like(request):

    # info_list = models.MyPlaylist.objects.all().order_by('p_like')
    playlists = models.MyPlaylist.objects.all().order_by('p_like')
    return render(request, 'index.html', {'playlists': playlists, 'select': 'l_like'})


def m_list_new(request):

    # info_list = models.MyPlaylist.objects.all().order_by('list_pub_date')
    playlists = models.MyPlaylist.objects.all().order_by('list_pub_date')
    return render(request, 'index.html', {'playlists': playlists, 'select': 'l_new'})


# def index(request):
#     playlists = models.Playlist.objects.all()
#     return render(request, 'index.html', {'playlists': playlists})


def playlist(request, list_id):
    playlists = get_object_or_404(models.MyPlaylist, pk=list_id)
    return render(request, 'playlist.html', {'playlists': playlists})
