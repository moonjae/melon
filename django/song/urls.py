from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.song_list, name='song-list')

]