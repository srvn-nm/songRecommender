from rest_framework import serializers


class SongRecognitionSerializer(serializers.Serializer):
    audio_file = serializers.FileField()
    request_id = serializers.IntegerField()
