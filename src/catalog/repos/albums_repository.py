from typing import Any

from catalog.models import AlbumModel


class AlbumsRepository:
    def __init__(self):
        self.model = AlbumModel

    def find(self) -> list[AlbumModel]:
        return self.model.objects.all()

    def find_by_id(self, find_id: int) -> AlbumModel:
        return self.model.objects.filter(id=find_id).first()

    def create(self, album: dict[str, Any]) -> AlbumModel:
        return self.model.objects.create(**album)


