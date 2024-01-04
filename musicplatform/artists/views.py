from .models import Artist
from .serializers import *
from django.http import HttpResponse
from rest_framework import viewsets


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = "stage_name"
