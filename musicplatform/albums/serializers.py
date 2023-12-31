from rest_framework import serializers
from .models import Album


class AblumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    class Meta:
        model = Album
        fields = "__all__"
