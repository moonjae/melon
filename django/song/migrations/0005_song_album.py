# Generated by Django 2.0.2 on 2018-02-07 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_album'),
        ('song', '0004_remove_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='album.Album'),
            preserve_default=False,
        ),
    ]
