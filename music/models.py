from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    like_playlist = models.ManyToManyField('MyPlaylist', blank=True, related_name='like_users')
    music = models.ManyToManyField('Music', blank=True, related_name='mlike_users')
    # music_like = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)


class Artist(models.Model):
    a_name = models.CharField(max_length=50)

    def __str__(self):
        return self.a_name


class Music(models.Model):
    m_like = models.IntegerField(default=0)
    m_title = models.CharField(max_length=100)
    m_videoCd = models.CharField(max_length=100, null=True)
    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.m_title


class MyPlaylist(models.Model):
    mp_name = models.CharField(max_length=100, null=True)
    mp_like = models.IntegerField(default=0)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    list_pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mp_name)


class Playlist(models.Model):
    music_fk = models.ForeignKey(Music, on_delete=models.CASCADE, null=True)
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE, null=True)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.myplaylist_fk.mp_name)


class PlaylistComment(models.Model):
    c_contents = models.TextField()
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.c_contents



