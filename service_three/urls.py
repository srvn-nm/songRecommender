from django.urls import path
from .views import send_song_suggestions

urlpatterns = [
    path('send-song-suggestions/', send_song_suggestions, name='send-song-suggestions'),
]
