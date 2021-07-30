from django.contrib import admin
from music.models import Artist, Music, MyPlaylist, Playlist, PlaylistComment

admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(MyPlaylist)
admin.site.register(Playlist)
admin.site.register(PlaylistComment)


