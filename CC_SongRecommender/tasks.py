from celery import shared_task
from django.core.mail import send_mail  # Assuming you configure Django's email backend with Firebase
from service_one.models import Request
from .shazam import recognize_song_shazam  # Placeholder for your actual implementation
from .spotify import get_spotify_recommendations  # Placeholder for your actual implementation


@shared_task
def send_confirmation_email(email, subject, message):
    send_mail(subject, message, 'your_email@example.com', [email])


@shared_task
def process_music_recognition(music_request_id):
    global music_request
    try:
        music_request = Request.objects.get(id=music_request_id)
        # Assume recognize_song_shazam returns the spotify_id directly
        spotify_id = recognize_song_shazam(music_request.audio_file.path)

        recommendations = get_spotify_recommendations(spotify_id, "", "")
        formatted_recommendations = format_recommendations(recommendations)

        send_confirmation_email.delay(music_request.email, "Your Music Recommendations", formatted_recommendations)

        music_request.song_id = spotify_id
        music_request.status = 'ready'  # Set to 'ready' before sending recommendations
        music_request.save()

    except Exception as e:
        music_request.status = 'failure'
        music_request.save()
        raise e


# noinspection PyCompatibility
def format_recommendations(recommendations):
    message = "Here are your music recommendations:\n\n"
    for idx, rec in enumerate(recommendations['tracks'], start=1):
        artists = ', '.join(artist['name'] for artist in rec['artists'])
        message += f"{idx}. {rec['name']} by {artists}\n"
    return message


@shared_task
def process_recommendations():
    ready_requests = Request.objects.filter(status='ready')
    for music_req in ready_requests:
        recommendations = get_spotify_recommendations(music_req.song_id, "", "")
        recommendations_message = format_recommendations(recommendations)

        send_confirmation_email.delay(music_req.email, "Music Recommendations", recommendations_message)

        music_req.status = 'done'
        music_req.save()
