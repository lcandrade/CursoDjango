from django.db import models

# Create your models here.
class Prueba (models.Model):
    titulo= models.CharField(max_length=38)
    subtitulo= models.CharField(max_length=50)
