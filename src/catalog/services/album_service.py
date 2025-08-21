from catalog.models import AlbumModel
from catalog.repos.albums_repository import AlbumsRepository
from catalog.schemas.album_schemas import AlbumReadSchema, AlbumCreateSchema


class AlbumsService:
    def __init__(self):
        self.repo = AlbumsRepository()

    def get(self) -> list[AlbumReadSchema]:
        albums = self.repo.find()

        return [
            AlbumReadSchema(album).data
            for album in albums
        ]

    def get_by_id(self, album_id: int) -> AlbumReadSchema | None:
        album = self.repo.find_by_id(album_id)
        return AlbumReadSchema(album) if album else None

    def create(self, album: AlbumCreateSchema) -> AlbumReadSchema:
        new_album = self.repo.create(album.validated_data)
        return AlbumReadSchema(new_album)