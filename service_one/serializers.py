from rest_framework import serializers
from .models import Request


from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'email', 'audio_file', 'status', 'song_id']