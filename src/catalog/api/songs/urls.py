from django.urls import path
from .views import songs_view

urlpatterns = [
    path('', songs_view, name='songs-view'),
]