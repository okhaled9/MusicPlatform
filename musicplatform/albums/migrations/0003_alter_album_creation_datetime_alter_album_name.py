# Generated by Django 4.2.2 on 2023-12-30 01:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("albums", "0002_album_is_approved_alter_album_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="creation_datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="album",
            name="name",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]