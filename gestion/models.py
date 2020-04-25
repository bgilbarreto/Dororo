from django.db import models

# Create your models here.

class Lugar (models.Model):
    nombre = models.CharField (max_length=25)

class Parte (models.Model):
    nombre = models.CharField (max_length=25)

class demonio (models.Model):
    nombre = models.CharField(max_length=25)
    parte = models.ForeignKey(Parte, on_delete = models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete = models.CASCADE)
    estado = models.CharField(max_length=20)

class Batalla (models.Model):
    lugar = models.ForeignKey (Lugar, on_delete = models.CASCADE)
    Demonio = models.ForeignKey (demonio, on_delete = models.CASCADE)
    ganador = models.CharField (max_length= 25)

class Objetos_Dororo (models.Model):
    nombre = models.CharField (max_length=25)
    procedencia = models.CharField(max_length=50)
