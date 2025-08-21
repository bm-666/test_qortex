from django.urls import path, include

urlpatterns = [
    path('albums/', include('catalog.api.albums.urls')),
    path('artists/', include('catalog.api.artists.urls')),
    path('songs/', include('catalog.api.songs.urls')),
]