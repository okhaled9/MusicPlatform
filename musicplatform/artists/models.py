from django.db import models
from django.db.models import Count, Q


class ArtistManager(models.Manager):
    def get_queryset(self):
        return (super().get_queryset().annotate(approved_albums=Count("album", filter=Q(album__is_approved=True))))


class Artist(models.Model):
    stage_name = models.CharField(max_length=50, unique=True)  # required=true by default and blank = false by default
    social_link = models.URLField(blank=True)  # null=false by default
    objects = ArtistManager()

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ["stage_name"]
