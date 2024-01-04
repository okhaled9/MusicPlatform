from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from pathlib import Path
from artists.models import Artist


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("artist", "name")


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    cover = models.ImageField(upload_to="covers")
    thumbnail = ImageSpecField(
        source="cover",
        processors=[ResizeToFit(255, 255)],
        format="jpeg",
        options={"quality": 60},
    )
    audio = models.FileField(upload_to="songs")

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("album", "name")


@receiver(signal=post_delete, sender=Song)
def delete_cover(instance, **kwargs):
    # delete cover and audio after object is deleted
    cover_path = Path(instance.cover.path)
    cover_path.unlink()

    audio_path = Path(instance.audio.path)
    audio_path.unlink()
