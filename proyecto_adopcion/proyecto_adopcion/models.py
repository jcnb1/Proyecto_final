from django.db import models
from proyecto_adopcion.adopcion.models import Persona



class Mascota(models.Model):
    tipo_mascota = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    descripcion = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.CharField(max_length=50, blank=True)


