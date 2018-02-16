from django.db import models
from album.models import Album
from artist.models import Artist


class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField('이름', max_length=50)
    release_date = models.DateField('발매일', blank= True, null= True)
    genre = models.CharField('장르', max_length = 30)
    FLAC = models.CharField('FLAC', max_length = 30, null = True)



    @property
    def formatted_release_date(self):
        a = str(self.album.release_date)
        return a





    @property
    def artists(self):
        a = self.album
        artists_string = ','.join(a.artist.values_list('name', flat=True))
        return artists_string

    def __str__(self):
        return self.name
