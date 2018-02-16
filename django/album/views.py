from django.shortcuts import render
from .models import Album


# Create your views here.



def album_list(request):
    albums_list = Album.objects.all()
    context = {
        'albums': albums_list
    }
    return render(request, 'album/album.html', context)
