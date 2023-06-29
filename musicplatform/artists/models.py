from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(max_length=50, unique=True)  # required=true by default and blank = false by default
    social_link = models.URLField(blank=True)  # null=false by default

    def __str__(self):
        return self.stage_name

    class Meta:
        ordering = ["stage_name"]
