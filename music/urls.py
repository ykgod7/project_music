from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('music_rank/f_like', views.m_music_rank_like, name='music_rank_like'),
    path('music_rank/f_title', views.m_music_rank_title, name='music_rank_title'),
    path('<str:username>', views.mypage, name='mypage')
]