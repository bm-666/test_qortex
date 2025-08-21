from django.urls import path
from .views import artists_view


urlpatterns = [
    path('', artists_view, name='artists-view'),
]