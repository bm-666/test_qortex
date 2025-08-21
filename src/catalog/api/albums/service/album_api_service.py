from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.request import Request
from rest_framework.response import Response

from catalog.schemas.album_song_schemas import AlbumSongCreateSchema, AlbumSongReadSchema
from catalog.schemas.album_schemas import AlbumCreateSchema, AlbumReadSchema
from catalog.services.album_service import AlbumsService
from catalog.services.album_songs_service import AlbumSongsService
from catalog.services.songs_service import SongsService


class AlbumApiService:
    """
    API-слой для работы с альбомами и песнями внутри альбомов.
    Инкапсулирует взаимодействие между HTTP-запросами и бизнес-логикой.
    """

    def __init__(self):
        self.album_service = AlbumsService()
        self.album_song_service = AlbumSongsService()
        self.song_service = SongsService()

    def create_album(self, request: Request) -> AlbumReadSchema:
        """
        Создаёт новый альбом по данным из запроса.

        Args:
            request (Request): HTTP-запрос с полями альбома

        Returns:
            AlbumReadSchema: Сериализованный объект созданного альбома

        Raises:
            ValidationError: Если входные данные некорректны
        """
        schema = AlbumCreateSchema(data=request.data)
        schema.is_valid(raise_exception=True)

        return self.album_service.create(schema)

    def create_album_song(self, request: Request, album_id: int) -> AlbumSongReadSchema:
        """
        Добавляет песню в альбом с заданным порядковым номером (track_number).

        Args:
            request (Request): HTTP-запрос с полями song_id и track_number
            album_id (int): ID альбома, куда добавляется песня

        Returns:
            AlbumSongReadSchema: Сериализованный объект связи альбом–песня

        Raises:
            NotFound: Если альбом или песня не найдены
            ValidationError: Если песня уже добавлена в альбом или данные невалидны
        """
        if self.album_service.get_by_id(album_id) is None:
            raise NotFound(detail="Альбом не найден", code=status.HTTP_404_NOT_FOUND)

        song_id = request.data.get("song")

        if self.song_service.get_by_id(song_id) is None:
            raise NotFound(detail="Песня не найдена", code=status.HTTP_404_NOT_FOUND)

        if self.album_song_service.get_by_album_song_pair(album_id=album_id, song_id=song_id):
            raise ValidationError("Песня уже добавлена в этот альбом", code=status.HTTP_400_BAD_REQUEST)

        # Обогащаем данные album_id перед валидацией
        data = request.data.copy()
        data["album"] = album_id

        schema = AlbumSongCreateSchema(data=data)
        schema.is_valid(raise_exception=True)

        return self.album_song_service.create(schema)

    def get_album_by_id(self, album_id: int) -> AlbumReadSchema:
        """
        Возвращает альбом по его ID.

        Args:
            album_id (int): Уникальный идентификатор альбома

        Returns:
            AlbumReadSchema: Сериализованный объект альбома

        Raises:
            NotFound: Если альбом не найден
        """
        album = self.album_service.get_by_id(album_id)
        if album is None:
            raise NotFound(detail="Альбом не найден", code=status.HTTP_404_NOT_FOUND)

        return album

    def get_albums(self) -> list[AlbumReadSchema]:
        """
        Возвращает список всех альбомов в системе.

        Returns:
            list[AlbumReadSchema]: Список сериализованных альбомов
        """
        return self.album_service.get()
