from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.api.albums.request import AlbumCreateRequest, AlbumSongRequest
from catalog.api.albums.service.albums_api_service import AlbumApiService
from catalog.schemas.album_schemas import AlbumReadSchema


@extend_schema_view(
    get=extend_schema(
        summary="Получить список всех альбомов",
        description=(
            "Возвращает список всех альбомов, доступных в системе.\n\n"
            "**Метод GET:**\n"
            "- Извлекает все альбомы из базы данных.\n"
            "- Возвращает список объектов `AlbumReadSchema`."
        ),
        responses={200: AlbumReadSchema(many=True)},
        tags=["albums"],
    ),
    post=extend_schema(
        summary="Создать новый альбом",
        description=(
            "Создаёт новый альбом на основе данных, переданных в теле запроса.\n\n"
            "**Метод POST:**\n"
            "- Принимает данные нового альбома по схеме `AlbumCreateRequest`.\n"
            "- Возвращает созданный альбом в формате `AlbumReadSchema`."
        ),
        request=AlbumCreateRequest,
        responses={201: AlbumReadSchema},
        tags=["albums"],
    )
)
@api_view(['GET', 'POST'])
def albums_view(request):
    service = AlbumApiService()

    if request.method == 'GET':
        result = service.get_albums()
        return Response(data=result, status=status.HTTP_200_OK)

    if request.method == 'POST':
        result = service.create_album(request.data)
        return Response(data=result.data, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Добавить песню в альбом",
    description=(
        "Добавляет песню в существующий альбом по его `album_id`.\n\n"
        "**Метод POST:**\n"
        "- Принимает данные песни по схеме `AlbumSongRequest`.\n"
        "- Добавляет песню в указанный альбом.\n"
        "- Возвращает статус выполнения."
    ),
    request=AlbumSongRequest,
    responses={201: None},
    tags=["albums"],
)
@api_view(['POST'])
def add_song_to_album(request, album_id: int):
    api_service = AlbumApiService()
    api_service.create_album_song(request, album_id)
    return Response({"detail": "Песня добавлена в альбом"}, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="Получить альбом по ID",
    description=(
        "Возвращает данные конкретного альбома по его уникальному идентификатору `album_id`.\n\n"
        "**Метод GET:**\n"
        "- Находит и возвращает объект альбома, если он существует.\n"
        "- Если альбом не найден, возвращает соответствующую ошибку (не обрабатывается в этом коде)."
    ),
    responses={200: AlbumReadSchema},
    tags=["albums"],
)
@api_view(['GET'])
def get_album(request, album_id: int):
    api_service = AlbumApiService()
    result = api_service.get_album_by_id(album_id)
    return Response(data=result.data, status=status.HTTP_200_OK)
