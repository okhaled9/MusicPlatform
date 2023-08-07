# Generated by Django 4.2.2 on 2023-08-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(default='New Album', max_length=20),
        ),
    ]
