from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('music_rank/', views.m_music_rank, name='music_rank')
]