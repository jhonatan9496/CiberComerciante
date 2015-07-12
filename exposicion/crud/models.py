from django.db import models

# Create your models here.
class Autor(models.Model):
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	ciudad = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length=255)
	fecha = models.DateField()
	autor = models.ForeignKey(Autor)

	def __unicode__(self):
		return self.titulo	