from django.shortcuts import render
from django.contrib.auth import get_user_model
from . import models


def mypage(request, username):
    user = get_user_model()
    return render(request, 'mypage.html', {'user': user})


def m_music_rank(request):

    info_music = models.Music.objects.all().order_by('-m_like')
    return render(request, 'music_rank.html', {'info_music': info_music})
