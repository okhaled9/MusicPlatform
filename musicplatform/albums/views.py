from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Album
from .serializers import *
from django.conf import settings


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AblumSerializer
    lookup_field = "name"

    @action(detail=False, methods=["PATCH"], url_path="approve")
    def approve(self, request, **kwargs):
        if type(request.data["approve"]) != bool:
            return Response(
                {"detail": "approve has to be a boolean"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        approve = True if request.data["approve"] else False

        albums = self.get_queryset()

        if "approve" not in request.data:
            return Response(
                {"detail": "approve is required in the body"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        albums.update(is_approved=approve)

        message = "all approved" if approve else "all disapproved"
        return Response({"detail": message}, status=status.HTTP_200_OK)
