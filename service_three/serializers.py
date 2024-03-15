from rest_framework import serializers


class SongSuggestionsSerializer(serializers.Serializer):
    song_title = serializers.CharField()
    artist = serializers.CharField()
    genre = serializers.CharField()
    # Add other fields as needed for suggestions
