from django.shortcuts import render, redirect
from .models import Artist
import datetime


# Create your views here.



def artist_list(request):
    artists_list = Artist.objects.all()
    context = {
        'artists': artists_list
    }
    return render(request, 'artist/artist_list.html', context=context)



def artist_add(request):

    context = {

    }

    if request.method == 'POST':

        name = request.POST['name']
        real_name = request.POST['real_name']
        nationality = request.POST['nationality']
        birth_date = datetime.datetime.strptime(request.POST['birthdate'], '%Y-%m-%d').date()

        constellation = request.POST['constellation']
        bloodtype = request.POST['bloodtype']


        artist = Artist.objects.create(
            name = name,
            real_name = real_name,
            nationality = nationality,
            birth_date = birth_date,
            constellation = constellation,
            blood_type = bloodtype
        )
        return redirect('artist-list')
    return render(request, 'artist/artist_add.html', context = context)