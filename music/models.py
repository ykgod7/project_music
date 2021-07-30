from django.db import models


class Artist(models.Model):
    a_name = models.CharField(max_length=50)


class Music(models.Model):
    m_like = models.IntegerField(default=0)
    m_title = models.CharField(max_length=100)
    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)


class MyPlaylist(models.Model):
    music_fk = models.ForeignKey(Music, on_delete=models.CASCADE)


class Playlist(models.Model):
    p_like = models.IntegerField(default=0)
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)


class PlaylistComment(models.Model):
    c_contents = models.TextField()
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)


