from rest_framework import serializers

class TextToSpeechSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=5000)
    language = serializers.CharField(max_length=10)
    selectedVoice = serializers.CharField(max_length=10)