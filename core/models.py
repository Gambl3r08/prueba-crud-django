from django.db import models

class cancion(models.Model):
    nombre = models.CharField(max_length=70)
    autor = models.CharField(max_length=70)
    album = models.CharField(max_length=70)
    duracion = models.CharField(max_length=20)
    fechaLanzamiento = models.DateField()


