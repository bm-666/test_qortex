from typing import Any
from catalog.models.song_model import SongModel

class SongsRepository:

    def __init__(self):
        self.model = SongModel

    def create(self, song: dict[str, Any]) -> SongModel:
        return self.model.objects.create(**song)

    def find_by_id(self, find_id: str) -> SongModel | None:
        return self.model.objects.filter(id=find_id).first()

    def find(self) -> list[SongModel]:
        return self.model.objects.all()