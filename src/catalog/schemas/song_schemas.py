from rest_framework import serializers
from catalog.models.song_model import SongModel


class SongCreateSchema(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields = ["title"]


class SongReadSchema(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields = ["id", "title"]
