from rest_framework import serializers

class AlbumCreateRequest(serializers.Serializer):
    title = serializers.CharField()
    artist = serializers.CharField()
    release_year = serializers.IntegerField()

class AlbumSongRequest(serializers.Serializer):
    song = serializers.IntegerField()
    track_number = serializers.IntegerField()