from django.db import models

# Create your models here.
class Hombre(models.Model):
    es_camisa = models.BooleanField(default = 'False')
    es_chaqueta = models.BooleanField(default = 'False')
    es_pantalon = models.BooleanField(default = 'False')
    es_accesorio = models.BooleanField(default = 'False')
    imagen_1 = models.ImageField(default = 'null', upload_to = 'inventario')
    imagen_2 = models.ImageField(default ='null', upload_to = 'inventario')
    imagen_3 = models.ImageField(default = 'null', upload_to = 'inventario')
    titulo = models.TextField(default = 'null')
    precio = models.IntegerField()
    descripcion = models.TextField(default = 'null')
    tallas = models.TextField(default = 'null')
