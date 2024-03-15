from CC_SongRecommender.shazam import recognize_song_shazam
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service_one.models import Request
from service_two.serializers import SongRecognitionSerializer


@api_view(['POST'])
def recognize_song(request):
    serializer = SongRecognitionSerializer(data=request.data)
    if serializer.is_valid():
        try:
            request_id = serializer.validated_data['request_id']
            audio_file = serializer.validated_data['audio_file']
            request_obj = Request.objects.get(pk=request_id)

            # Perform song recognition using Shazam API
            spotify_id = recognize_song_shazam(audio_file)

            # Update the request object with the SpotifyID
            request_obj.song_id = spotify_id
            request_obj.status = 'ready'
            request_obj.save()

            return Response({"message": "Song recognized successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=400)
