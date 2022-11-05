from django.db import models
from ckeditor.fields import RichTextField

class Administrador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Posteo(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion_corta = models.CharField(max_length=200)
    contenido = RichTextField()
    foto = models.ImageField(upload_to="posts", null=True, blank=True)
    es_una_promo = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Tarifa(models.Model):
    periodo = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    cantidad_maxima_personas = models.IntegerField()

class Negocio(models.Model):
    nombre = models.CharField(max_length=30)
    instragram = models.URLField(null=True)
    maps = models.URLField(null=True)
    mail = models.EmailField(null=True)

class Reserva(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    mail = models.EmailField(null=True)
    fecha_desde = models.DateTimeField()
    fecha_hasta = models.DateTimeField()
    cantidad_adultos = models.IntegerField()
    cantidad_menores = models.IntegerField()
    consulta = RichTextField()




