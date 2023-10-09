from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    approved_albums = serializers.ReadOnlyField()
    album_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # album_set = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = "__all__"
