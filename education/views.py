from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from gtts import gTTS
from io import BytesIO
from  account.serializer import TextToSpeechSerializer

@api_view(['POST'])
def text_to_speech(request):
    if request.method == 'POST':
        serializer = TextToSpeechSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            language = serializer.validated_data['language']
            selected_voice = serializer.validated_data['selectedVoice']
            
            try:
                tts = gTTS(text=text, lang=language, slow=False)
                speech_file = BytesIO()
                tts.write_to_fp(speech_file)
                speech_file.seek(0)

                response = HttpResponse(speech_file, content_type='audio/mp3')
                response['Content-Disposition'] = 'attachment; filename="speech.mp3"'
                
                return response
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

