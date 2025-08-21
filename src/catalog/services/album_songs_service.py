from catalog.repos.album_songs_repository import AlbumSongsRepository
from catalog.schemas.album_song_schemas import AlbumSongCreateSchema, AlbumSongReadSchema


class AlbumSongsService:
    def __init__(self):
        self.repo = AlbumSongsRepository()

    def create(self, song: AlbumSongCreateSchema) -> AlbumSongReadSchema:
        result = self.repo.create(song.validated_data)
        return AlbumSongReadSchema(result)

    def get_by_album_song_pair(self, album_id: int, song_id: int) -> AlbumSongReadSchema | None:
        result = self.repo.find_by_album_song_pair(album_id, song_id)
        return AlbumSongReadSchema(result) if result else None