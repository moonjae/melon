from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.album_list, name='album-list')

]
