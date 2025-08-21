from catalog.models import ArtistModel
from catalog.repos.artists_repository import ArtistsRepository
from catalog.schemas.artist_schemas import ArtistCreateSchema, ArtistReadSchema


class ArtistsService:
    def __init__(self):
        self.repo = ArtistsRepository()

    def create(self, artist: ArtistCreateSchema) -> ArtistReadSchema:
        artist = self.repo.create(artist.validated_data)
        return ArtistReadSchema(artist)

    def get(self) ->list[ArtistReadSchema]:
        artists = self.repo.find()

        return [
            ArtistReadSchema(artist).data
            for artist in artists
        ]