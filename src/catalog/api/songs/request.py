from rest_framework import serializers


class SongCreateRequest(serializers.Serializer):
    title = serializers.CharField()
    #album = serializers.CharField()