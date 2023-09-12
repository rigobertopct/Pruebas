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
    sigla = models.CharField(max_length=10)
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
""""
Indicadores que se miden en las pruebas que se realizan
"""
class Indicadores(models.Model):
    indicador = models.CharField(max_length=250)
    unidad = models.CharField(max_length=250)
    
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

class Deportista(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre y Apellidos", unique=True)
    edad = models.PositiveIntegerField(null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    estatura = models.DecimalField(max_digits=5, decimal_places=2, null=True)   
    foto = models.ImageField(upload_to='pugiles', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'deportista'
        verbose_name_plural = 'deportistas'
        db_table = 'deportista'
"""
Modelo de aplicación de la prueba
"""
class Prueba(models.Model):
    fecha = models.DateField()
    deporte = models.ForeignKey(Deporte, on_delete=PROTECT)
    deportista = models.ForeignKey(Deportista, on_delete=PROTECT)
    servicio = models.ForeignKey(Servicios, on_delete=PROTECT)
    lugar = models.ForeignKey(Lugar, on_delete=PROTECT)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=PROTECT)
    archivo = models.FileField()
    resultado = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=255)
    valoracion = models.CharField(max_length=255)
      

    class Meta:
        verbose_name = 'prueba'
        verbose_name_plural = 'pruebas'
        db_table = 'prueba'
        
"""
Modelo para poner el resultado de los indicadores en una prueba
"""
class PruebaResultIndic(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=PROTECT)
    indicador = models.ForeignKey(Indicadores, on_delete=PROTECT)
    valor_ind = models.CharField(max_length=255)
         
    
