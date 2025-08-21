from typing import Any

from catalog.models.artist_model import ArtistModel

class ArtistsRepository:
    def __init__(self):
        self.model = ArtistModel

    def create(self, artist: dict[str, Any]) -> ArtistModel:
        return self.model.objects.create(**artist)

    def find(self) -> list[ArtistModel]:
        return self.model.objects.all()