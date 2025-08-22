from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view

from catalog.api.songs.request import SongCreateRequest

from catalog.api.songs.service.songs_api_service import SongApiService
from catalog.schemas.song_schemas import SongReadSchema


@extend_schema_view(
    get=extend_schema(
        summary="Получить список всех песен",
        description=(
            "Возвращает список всех песен, доступных в системе.\n\n"
            "**Метод GET:**\n"
            "- Извлекает все песни из базы данных.\n"
            "- Возвращает список объектов `SongReadSchema`."
        ),
        responses={200: SongReadSchema(many=True)},
        tags=["songs"],
    ),
    post=extend_schema(
        summary="Создать новую песню",
        description=(
            "Создаёт новую песню на основе переданных данных.\n\n"
            "**Метод POST:**\n"
            "- Принимает данные по схеме `SongCreateRequest`.\n"
            "- Возвращает созданную песню в формате `SongReadSchema`."
        ),
        request=SongCreateRequest,
        responses={201: SongReadSchema},
        tags=["songs"],
    )
)
@api_view(['GET', 'POST'])
def songs_view(request):
    """
    Получить список всех песен или создать новую.

    Args:
        request (Request): HTTP-запрос (GET для получения, POST для создания)

    Returns:
        Response: Список песен или данные новой песни
    """
    api_service = SongApiService()

    if request.method == 'GET':
        # Получаем все песни
        result = api_service.get_songs()
        return Response(data=result, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # Создаём новую песню
        result = api_service.create_song(request)
        return Response(data=result.data, status=status.HTTP_201_CREATED)
