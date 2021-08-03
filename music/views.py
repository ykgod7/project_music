from django.shortcuts import render
from . import models
from django.contrib.auth.models import User
from .forms import MyplayListForm
from .models import MyPlaylist

def m_music_rank(request):

    info_music = models.Music.objects.all().order_by('-m_like')
    return render(request, 'music_rank.html', {'info_music': info_music})

def music_video(request):
    cur_user = request.user
    if request.method == 'POST':
        return
    else:
        user = User.objects.get(username=request.user)
        play_list = models.Playlist.objects.select_related('myplaylist_fk')
        # myplay_list = [l for l in play_list.]
        context = {
            'user': user,
            'play_list': models.Playlist.objects.select_related('myplaylist_fk').filter(user_fk=user),
        }
        return render(request, 'music_detail/video.html', context)
