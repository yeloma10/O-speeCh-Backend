from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip
import tempfile
import os
from account.serializer import TextToSpeechSerializerVideo

class TextToSpeechView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TextToSpeechSerializerVideo(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data.get('text')
            language = serializer.validated_data.get('language')
            selected_voice = serializer.validated_data.get('selectedVoice')
            video_file = serializer.validated_data.get('videoFile')

            tts = gTTS(text=text, lang=language, slow=False)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_fp:
                tts.save(audio_fp.name)
                audio_fp.close()

               
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as video_fp:
                    video_fp.write(video_file.read())
                    video_fp.close()

                    video_clip = VideoFileClip(video_fp.name)
                    audio_clip = AudioFileClip(audio_fp.name)

                    final_clip = video_clip.set_audio(audio_clip)          
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as final_fp:
                        final_clip.write_videofile(final_fp.name, codec='libx264', audio_codec='aac')
                        final_fp.seek(0)
                        response = HttpResponse(final_fp.read(), content_type="video/mp4")
                        response['Content-Disposition'] = 'attachment; filename="synced_video.mp4"'

            os.remove(audio_fp.name)
            os.remove(video_fp.name)
            os.remove(final_fp.name)

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
