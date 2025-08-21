from catalog.repos.songs_repository import SongsRepository
from catalog.schemas.song_schemas import SongCreateSchema, SongReadSchema

class SongsService:
    def __init__(self):
        self.repo = SongsRepository()

    def create(self, song: SongCreateSchema) -> SongReadSchema:
        result = self.repo.create(song.validated_data)
        return SongReadSchema(result)

    def get_by_id(self, song_id: str) -> SongReadSchema | None:
        song = self.repo.find_by_id(song_id)
        return SongReadSchema(song) if song is not None else None
    def get(self) -> list[SongReadSchema]:
        songs = self.repo.find()

        return [
            SongReadSchema(song).data
            for song in songs
        ]