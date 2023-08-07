from django.db import models
from artists.models import Artist
from django.utils import timezone


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="New Album")
    creation_datetime=models.DateTimeField(default=timezone.now)
    release_datetime=models.DateTimeField()
    cost = models.DecimalField(decimal_places=2,max_digits=10)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name