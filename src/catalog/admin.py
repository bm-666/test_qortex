from django.contrib import admin
from catalog.models import (
    ArtistModel,
    AlbumModel,
    AlbumSongModel,
    SongModel
)

@admin.register(ArtistModel)
class ArtistAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'id']

@admin.register(AlbumModel)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']

@admin.register(SongModel)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']

@admin.register(AlbumSongModel)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ['album', 'song', 'track_number']

# Register your models here.
