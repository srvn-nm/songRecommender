from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from CC_SongRecommender.mailgun import send_email_with_firebase
from CC_SongRecommender.spotify import get_spotify_recommendations
from service_one.models import Request


@api_view(['POST'])
def send_song_suggestions(request):
    global suggestions
    try:
        # Get pending requests
        pending_requests = Request.objects.filter(status='ready')

        for request_obj in pending_requests:
            # Extract SpotifyID from the request
            spotify_id = request_obj.song_id

            # Get user's email
            user_email = request_obj.email

            # Send song suggestions using Spotify API
            suggestions = get_spotify_recommendations(spotify_id, None, None)

            # Code to send email with suggestions to the user
            send_email_with_firebase(user_email, "song suggestions", suggestions)

            # Update request status to done
            request_obj.status = 'done'
            request_obj.save()

        return Response({"message": "Suggestions sent successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
