from celery.backends import database
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.response import Response
from rest_framework.views import APIView

from CC_SongRecommender.S3_helper import upload_to_server
from CC_SongRecommender.tasks import send_confirmation_email, process_music_recognition
from .models import Request
from .serializers import RequestSerializer


class MusicUploadView(APIView):
    # noinspection PyCompatibility
    def post(self, request, *args, **kwargs):
        # Extract email and file from request
        email = request.data['email']
        audio_file = request.data['file']  # Simplified, adjust based on your frontend

        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            email = validated_data['email']
            audio_file = validated_data['audio_file']

        if email and audio_file:
            # Save the initial music request to the database
            music_request = Request.objects.create(email=email, status='pending')
            default_storage.save(audio_file, music_request)
            upload_to_server(audio_file, audio_file.id)

            # serializer
            music_request = serializer.save(status='pending')
            file_path = f'music_requests/{music_request.id}/{audio_file.name}'
            saved_path = default_storage.save(file_path, ContentFile(audio_file.read()))
            music_request.audio_file = saved_path
            music_request.save()

            # Asynchronously send confirmation email
            send_confirmation_email.delay(email)

            # Asynchronously process music recognition and recommendation
            process_music_recognition.delay(music_request.id, audio_file.name)

            return Response({"message": "Your music is being processed"}, status=202)
        else:
            return Response({"error": "email or file is empty"}, status=400)
