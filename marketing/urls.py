from django.urls import path
from .views import *
urlpatterns = [
    path('api/marketting/', TextToSpeechView.as_view(), name='text-to-speech')
]