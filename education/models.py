from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Parametre_vocal(models.Model):
  vitesse = models.IntegerField()
  langue = models.CharField(max_length=255)
  voix = models.CharField(max_length=255)
  
class Contenu(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()
  parametre = models.OneToOneField(Parametre_vocal, on_delete=models.CASCADE)


