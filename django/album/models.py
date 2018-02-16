from django.db import models
from artist.models import Artist



class Album(models.Model):

    img_cover = models.ImageField('커버이미지', upload_to ='album', blank = True)

    artist = models.ManyToManyField(Artist, verbose_name = '아티스트 목록')

    title = models.CharField('앨범명', max_length=50)

    release_date = models.DateField('발매일', blank=True, null=True)

    agency = models.CharField(max_length=50)

    production_company = models.CharField(max_length=50)

    @property
    def genre(self):
        genre_string = ','.join(self.song_set.values_list('genre', flat = True))
        return genre_string

    def __str__(self):
        artists_string = ','.join((self.artist.values_list('name', flat = True)).distinct())
        return "{}, ({})".format(self.title, artists_string)



