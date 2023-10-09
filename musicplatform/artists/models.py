from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(max_length=50, unique=True)
    social_link = models.URLField(blank=True)

    @property
    def approved_albums(self):
        return self.album_set.filter(is_approved=True).count()

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ["stage_name"]
