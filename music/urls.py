from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('music_rank/f_like', views.m_music_rank_like, name='music_rank_like'),
    path('music_rank/f_title', views.m_music_rank_title, name='music_rank_title'),
    path('<str:username>', views.mypage, name='mypage'),
    path('playlist/<int:list_id>', views.playlist, name='playlist'),
    path('l_like', views.m_list_like, name='list_like'),
    path('l_new', views.m_list_new, name='list_new'),
]