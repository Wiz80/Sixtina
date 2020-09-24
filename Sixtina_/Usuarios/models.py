from django.db import models

# Create your models here.
class Usuario(models.Model):

    email = models.EmailField()
    contraseña = models.CharField(max_length = 100)
    nombre = models.TextField()
    apellidos = models.TextField()
    documento = models.IntegerField()
    departamento = models.TextField()
    municipio = models.TextField()
    direccion = models.TextField(default = 'null')
