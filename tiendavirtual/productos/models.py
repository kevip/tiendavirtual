from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100)

    def __str__(self):
        return self.nombre


class Subcategoria(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    detalle = models.CharField('Detalle', max_length=100, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField('Descripcion')
    estado = models.SmallIntegerField()
    imagen = models.ImageField('Imagen', upload_to='productos/', blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey('Subcategoria', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
