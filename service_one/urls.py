from django.urls import path
from .views import MusicUploadView

urlpatterns = [
    path('submit-request/', MusicUploadView.post, name='submit-request'),
]
