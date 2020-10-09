from django.db import models

# Create your models here.
class Ropa_Hombre(models.Model):

    is_camiseta = models.BooleanField()
    is_camisa = models.BooleanField()
    is_chaqueta = models.BooleanField()
    is_pantalon = models.BooleanField()
    is_sudadera = models.BooleanField()
    is_accesorio = models.BooleanField()
    imagen_1 = models.ImageField(default = 'null', upload_to =  "inventario")
    imagen_2 = models.ImageField(default = 'null', upload_to =  "inventario")
    imagen_3 = models.ImageField(default = 'null', upload_to =  "inventario")
    imagen_4 = models.ImageField(default = 'null', upload_to =  "inventario")
    Titulo = models.TextField()
    Precio = models.IntegerField()
    Descripcion = models.TextField()
    Tallas = models.TextField()
    Colores = models.TextField(default = 'null')
    Idn = models.IntegerField()
