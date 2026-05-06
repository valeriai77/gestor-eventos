from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    afiche = models.ImageField(upload_to='afiches/')

    def __str__(self):
        return self.nombre


class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='participantes/')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre