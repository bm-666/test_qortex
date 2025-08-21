from rest_framework import serializers

class ArtistCreateRequest(serializers.Serializer):
    name = serializers.CharField()
