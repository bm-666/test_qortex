from rest_framework import serializers
from catalog.models.album_song_model import AlbumSongModel
from catalog.schemas.song_schemas import SongReadSchema


class AlbumSongCreateSchema(serializers.ModelSerializer):
    class Meta:
        model = AlbumSongModel
        fields = ["album", "song", "track_number"]


class AlbumSongReadSchema(serializers.ModelSerializer):
    song = SongReadSchema()

    class Meta:
        model = AlbumSongModel
        fields = ["id", "album", "song", "track_number"]
