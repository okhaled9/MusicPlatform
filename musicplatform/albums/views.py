from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Album
from .serializers import *

from albums.models import Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AblumSerializer
    lookup_field = "name"

    @action(detail=False, methods=["PATCH"], url_path="approve")
    def approve(self, request, **kwargs):
        try:
            album = get_object_or_404(self.get_queryset(), name=request.data["album_name"])
            approve = request.data["approve"]
            if (type(request.data["approve"]) != bool): raise KeyError("approve is required to be a boolean")
        except Exception as e:
            return Response({"detail": repr(e)}, status=status.HTTP_400_BAD_REQUEST)

        album.is_approved = approve
        album.save()
        message = f" '{album.name}' is {"approved" if approve else "disapproved"}"
        return Response({"message": message}, status=status.HTTP_200_OK)
