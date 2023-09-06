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


class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    isActivo = models.BooleanField(default=True)
    area = models.ForeignKey(Area, on_delete=PROTECT, blank=True, null=True)

    def __str__(self):
        return self.nombre


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
