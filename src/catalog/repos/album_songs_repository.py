from typing import Any
from catalog.models.album_song_model import AlbumSongModel

class AlbumSongsRepository:
    def __init__(self):
        self.model = AlbumSongModel

    def create(self, song: dict[str, Any]) -> AlbumSongModel:
        return self.model.objects.create(**song)

    def find_by_album_song_pair(self, find_album_id: int, find_song_id: int) -> AlbumSongModel | None:
        return AlbumSongModel.objects.filter(album=find_album_id, song=find_song_id).first()