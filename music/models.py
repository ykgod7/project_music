from django.db import models


class Artist(models.Model):     # 프레젠테이션..?
    a_name = models.CharField(max_length=50)


class Music(models.Model):      # 프레젠테이션 7p
    m_like = models.IntegerField(default=0)
    m_title = models.CharField(max_length=100)
    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE)


class MyPlaylist(models.Model):     # 프레젠테이션 8p
    music_fk = models.ForeignKey(Music, on_delete=models.CASCADE)


class Playlist(models.Model):       # 프레젠테이션 5p
    p_like = models.IntegerField(default=0)
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)


class PlaylistComment(models.Model):        # 프레젠테이션 5p
    c_contents = models.TextField()
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE)


