from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import PROTECT


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    isActivo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Area(models.Model):
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    isActivo = models.BooleanField(default=True)
    responsable = models.ForeignKey(User, on_delete=PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=PROTECT, blank=True, null=True)

    def __str__(self):
        return self.nombre

"""
Codificador de pruebas, el administrador funcional las define
"""
class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=20)
    objetivo = models.TextField(null=True)
    area = models.ForeignKey(Area, on_delete=PROTECT, blank=True, null=True)

    def __str__(self):
        return self.nombre

"""
Codificador de unidad de medidas, las magnitudes que se manejen ancladas desde el front(longitud,
tiempo,masa,)
"""
class UnidadM(models.Model):
    nombre = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=10)
    magnitud = models.CharField(max_length=10)
    

    def __str__(self):
        return self.nombre
""""
Indicadores que miden en las pruebas que se realizan
"""
class Indicadores(models.Model):
    indicador = models.CharField(max_length=250)
    unidad = models.ForeignKey(UnidadM, on_delete=PROTECT, blank=True, null=True)
    """
        Prueba a la que pertenece el indicador
    """
    servicio = models.ForeignKey(Servicios, on_delete=PROTECT, blank=True, null=True)
    

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    isActivo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    isActivo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Disciplina(models.Model):
    nombre = models.CharField(max_length=100)
    isActivo = models.BooleanField(default=True)
    deporte = models.ForeignKey(Deporte, on_delete=PROTECT)

    def __str__(self):
        return self.nombre


class Evaluacion(models.Model):
    nombre = models.CharField(max_length=100)
    isActivo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
