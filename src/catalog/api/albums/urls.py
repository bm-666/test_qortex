from django.urls import path
from .views import (
    albums_view,
    add_song_to_album,
    get_album
)

urlpatterns = [
    path('', albums_view, name='album-view'),
    path('albums/<int:album_id>/', get_album, name='get_album'),
    path('albums/<int:album_id>/songs/', add_song_to_album, name='add-song-to-album'),

]