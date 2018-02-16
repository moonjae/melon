from django.shortcuts import render
from .models import Song
# Create your views here.



def song_list(request):

    songs_list = Song.objects.all()
    context  = { 'songs' : songs_list
    }
    return render(request, 'song/song.html', context = context)