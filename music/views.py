from django.shortcuts import render
from . import models

# Create your views here.


def m_music_rank(request):

    info_music = models.Music.objects.all()
    return render(request, 'music_rank.html', {'info_music': info_music})
