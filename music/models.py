from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    a_name = models.CharField(max_length=50)


class Music(models.Model):
    m_like = models.IntegerField(default=0)
    m_title = models.CharField(max_length=100)
    # artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)


class MyPlaylist(models.Model):
    mp_title = models.CharField(max_length=100)
    mp_like = models.IntegerField(default=0)


class Playlist(models.Model):
    music_fk = models.ForeignKey(Music, on_delete=models.CASCADE)
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)


class PlaylistComment(models.Model):
    c_contents = models.TextField()
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)


