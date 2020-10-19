from django.db import models

# Create your models here.
class Ropa_Hombre(models.Model):

    is_camiseta = models.BooleanField()
    is_camisa = models.BooleanField()
    is_chaqueta = models.BooleanField()
    is_pantalon = models.BooleanField()
    is_sudadera = models.BooleanField()
    is_accesorio = models.BooleanField()
    imagen_1 = models.ImageField(upload_to =  "inventario", blank = True, null = True)
    imagen_2 = models.ImageField(upload_to =  "inventario", blank = True, null = True)
    imagen_3 = models.ImageField(upload_to =  "inventario", blank = True, null = True)
    imagen_4 = models.ImageField(upload_to =  "inventario", blank = True, null = True)
    Titulo = models.TextField()
    Precio = models.IntegerField()
    Descripcion = models.TextField()
    Tallas = models.TextField()
    Colores = models.TextField(default = 'null')
    Idn = models.IntegerField()
