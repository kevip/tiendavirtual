from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()



class Localizacion(models.Model):
    latitud = models.DecimalField(max_digits=12, decimal_places=9)
    longitud = models.DecimalField(max_digits=12, decimal_places=9)

    class Meta:
        verbose_name = 'Localizacion'
        verbose_name_plural = 'Localizaciones'


class Tiendas(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    direccion = models.TextField('Direccion')
    localizacion = models.ForeignKey('Localizacion', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tienda = models.ForeignKey('Tiendas', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()
