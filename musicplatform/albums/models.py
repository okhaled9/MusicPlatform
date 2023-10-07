from django.db import models
from artists.models import Artist


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
