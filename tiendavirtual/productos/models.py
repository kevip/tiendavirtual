from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100)


class Subcategoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    detalle = models.CharField('Detalle', max_length=100, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)


class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField('Descripcion')
    estado = models.SmallIntegerField()
    imagen = models.ImageField('Imagen', upload_to='stores/', blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
