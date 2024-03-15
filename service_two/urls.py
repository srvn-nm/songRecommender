from django.urls import path
from .views import recognize_song

urlpatterns = [
    path('recognize-song/', recognize_song, name='recognize-song'),
]
