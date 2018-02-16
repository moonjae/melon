from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.artist_list, name='artist-list'),
    path('add/', views.artist_add, name= 'artist-add')
]