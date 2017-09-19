from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length = 100)
	apellido_paterno = models.CharField(max_length = 100)
	apellido_materno = models.CharField(max_length = 100)
	razon_social = models.CharField(max_length = 100)
	rfc = models.CharField('RFC', max_length = 15)
	telefono = models.CharField(max_length = 12)
	telefono_celular = models.CharField(max_length = 12)
	fecha_nacimiento = models.DateField()

class Contacto(models.Model):
	nombre = models.CharField(max_length = 100)
	email = models.EmailField()
	comentario = models.TextField(max_length = 500)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return self.nombre
