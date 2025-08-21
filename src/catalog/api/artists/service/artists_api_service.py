from rest_framework.request import Request
from rest_framework.exceptions import APIException

from catalog.schemas.artist_schemas import ArtistCreateSchema, ArtistReadSchema
from catalog.services.artists_service import ArtistsService


class ArtistsAPIService:
    """
    API-слой для работы с исполнителями.
    Обрабатывает входные запросы и делегирует бизнес-логику соответствующему сервису.
    """

    def __init__(self):
        self.service = ArtistsService()

    def create_artist(self, request: Request) -> ArtistReadSchema:
        """
        Создаёт нового артиста на основе входных данных запроса.

        Args:
            request (Request): HTTP-запрос с данными исполнителя

        Returns:
            ArtistReadSchema: Сериализованный объект созданного артиста

        Raises:
            ValidationError: Если переданные данные некорректны
            APIException: При внутренней ошибке сервера
        """
        # Валидируем входные данные
        schema = ArtistCreateSchema(data=request.data)
        schema.is_valid(raise_exception=True)

        # Создаём артиста и возвращаем результат
        return self.service.create(schema)

    def get_artists(self) -> list[ArtistReadSchema]:
        """
        Возвращает список всех исполнителей в системе.

        Returns:
            list[ArtistReadSchema]: Список сериализованных объектов артистов
        """
        return self.service.get()
