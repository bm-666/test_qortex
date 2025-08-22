from rest_framework.request import Request
from catalog.schemas.song_schemas import SongReadSchema, SongCreateSchema
from catalog.services.songs_service import SongsService


class SongApiService:
    """
    API-слой для работы с песнями.
    Отвечает за валидацию входных данных и делегирование бизнес-логики в SongService.
    """

    def __init__(self):
        self.service = SongsService()

    def create_song(self, request: Request) -> SongReadSchema:
        """
        Создаёт новую песню на основе переданных данных запроса.

        Args:
            request (Request): HTTP-запрос с телом данных песни

        Returns:
            SongReadSchema: Сериализованные данные созданной песни

        Raises:
            ValidationError: Если данные не проходят валидацию
        """
        # Валидируем входные данные
        new_song = SongCreateSchema(data=request.data)
        new_song.is_valid(raise_exception=True)

        # Создаём песню через бизнес-слой
        return self.service.create(new_song)

    def get_songs(self) -> list[SongReadSchema]:
        """
        Возвращает список всех песен в системе.

        Returns:
            list[SongReadSchema]: Список сериализованных объектов песен
        """
        return self.service.get()
