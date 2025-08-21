from rest_framework import serializers

from catalog.enums.status_code import ResponseCode
from catalog.schemas.song_schemas import SongReadSchema


class SongResponse(serializers.Serializer):
    data: SongReadSchema
    status: ResponseCode