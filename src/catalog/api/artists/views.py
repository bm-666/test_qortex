from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view

from catalog.api.artists.request import ArtistCreateRequest
from catalog.api.artists.service.artists_api_service import ArtistsAPIService
from catalog.schemas.artist_schemas import ArtistReadSchema


@extend_schema_view(
    get=extend_schema(
        summary="Получить список всех артистов",
        description=(
            "Возвращает список всех артистов, зарегистрированных в системе.\n\n"
            "**Метод GET:**\n"
            "- Извлекает всех артистов из базы данных.\n"
            "- Возвращает список объектов `ArtistReadSchema` (или другой read-схемы, если она есть)."
        ),
        responses={200: ArtistReadSchema(many=True)},
        tags=["artists"],
    ),
    post=extend_schema(
        summary="Создать нового артиста",
        description=(
            "Создаёт нового артиста на основе переданных данных.\n\n"
            "**Метод POST:**\n"
            "- Принимает данные артиста по схеме `ArtistCreateRequest`.\n"
            "- Возвращает созданного артиста в формате `ArtistReadSchema`."
        ),
        request=ArtistCreateRequest,
        responses={201: ArtistReadSchema},
        tags=["artists"],
    )
)
@api_view(['GET', 'POST'])
def artists_view(request):
    """
    Получить список всех артистов или создать нового.

    Args:
        request (Request): HTTP-запрос с методом GET или POST

    Returns:
        Response: Список артистов или данные нового артиста
    """
    service = ArtistsAPIService()

    if request.method == 'GET':
        # Получаем всех артистов
        result = service.get_artists()
        return Response(data=result, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # Создаём нового артиста
        result = service.create_artist(request)
        return Response(data=result.data, status=status.HTTP_201_CREATED)
