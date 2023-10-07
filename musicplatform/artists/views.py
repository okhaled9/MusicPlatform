from .models import Artist
from .serializers import *
from django.http import HttpResponse
from rest_framework import viewsets


def index(request):
    http = "<h1>Hello Dev!</h1> <h2><a href='api/'>API</a></h2>"
    return HttpResponse(http)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = "stage_name"
