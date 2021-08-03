from django.db import models


class Artist(models.Model):     # 프레젠테이션..?
    a_name = models.CharField(max_length=50)

    def __str__(self):
        return self.a_name


class Music(models.Model):      # 프레젠테이션 7p
    m_like = models.IntegerField(default=0)
    m_title = models.CharField(max_length=100)
    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.m_title


class MyPlaylist(models.Model):
    p_like = models.IntegerField(default=0)
    made_by = models.CharField(max_length=20, default='신지환')
    myplaylist_name = models.CharField(max_length=20)
    music_fk = models.ForeignKey(Music, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.myplaylist_name


class Playlist(models.Model):
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.myplaylist_fk)


class PlaylistComment(models.Model):        # 프레젠테이션 5p
    c_contents = models.TextField()
    myplaylist_fk = models.ForeignKey(MyPlaylist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.c_contents


