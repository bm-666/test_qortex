from rest_framework import serializers
from catalog.models.artist_model import ArtistModel


class ArtistBaseSchema(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = ["name"]

class ArtistCreateSchema(ArtistBaseSchema):
    pass

class ArtistUpdateSchema(ArtistBaseSchema):
    pass

class ArtistReadSchema(ArtistBaseSchema):
    class Meta(ArtistBaseSchema.Meta):
        fields = ArtistBaseSchema.Meta.fields + ["id", "created_at"]
