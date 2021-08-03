from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    a_name = models.CharField(max_length=50)

    def __str__(self):
        return self.a_name


class Music(models.Model):
    m_like = models.IntegerField(default=0)
    m_title = models.CharField(max_length=100)
    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.m_title


class MyPlaylist(models.Model):
    mp_like = models.IntegerField(default=0)
    made_by = models.CharField(max_length=20, default='신지환')
    mp_title = models.CharField(max_length=20)
    music_fk = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return self.myplaylist_name


class Playlist(models.Model):       # 프레젠테이션 5p
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.myplaylist_fk)


class PlaylistComment(models.Model):
    c_contents = models.TextField()
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)

    def __str__(self):
        return self.c_contents


