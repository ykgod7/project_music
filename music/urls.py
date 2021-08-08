from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('music_rank/f_like/', views.m_music_rank_like, name='music_rank_like'),
    path('music_rank/f_title/', views.m_music_rank_title, name='music_rank_title'),
    path('l_like/', views.m_list_like, name='list_like'),
    path('l_new/', views.m_list_new, name='list_new'),
    path('<str:username>', views.mypage, name='mypage'),
    path('<str:username>/<int:list_id>', views.mypage_list, name='mypage_list'),
    path('<str:username>/<int:music_id>/<int:list_id>', views.delete_music, name='delete_music'),
    path('musicvideo/<str:videoId>/<str:videoTitle>/<str:videoArtist>/', views.music_video, name='music_video'),
    path('playlist/<int:list_id>', views.playlist, name='playlist'),
    path('playlist_like_toggle/<int:playlist_id>/', views.playlist_like_toggle, name="playlist_like_toggle"),
    path('create_comment/<int:playlist_id>', views.create_comment, name='create_comment'),
    path('delete_comment/<int:playlist_id>', views.delete_comment, name='delete_comment'),
]