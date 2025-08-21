from rest_framework import serializers
from catalog.models.album_model import AlbumModel
from catalog.models.artist_model import ArtistModel
from catalog.models.song_model import SongModel


class AlbumCreateSchema(serializers.ModelSerializer):
    class Meta:
        model = AlbumModel
        fields = ["title", "artist", "release_year"]


class AlbumReadSchema(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    songs = serializers.SerializerMethodField()

    class Meta:
        model = AlbumModel
        fields = ["id", "title", "artist", "release_year", "songs"]

    def get_songs(self, obj):
        """
        Возвращает список песен в альбоме с их названиями и порядковыми номерами.

        Args:
            obj (AlbumModel): экземпляр альбома

        Returns:
            list[dict]: список песен с полями title и track_number
        """
        # Получаем все связи песен с этим альбомом, упорядоченные по track_number
        album_songs = obj.album_songs.select_related("song").order_by("track_number")

        return [
            {
                "title": album_song.song.title,
                "track_number": album_song.track_number,
            }
            for album_song in album_songs
        ]
