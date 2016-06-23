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

    def __str__(self):
        return "({0}, {1})".format(self.latitud,self.longitud)

class Tiendas(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    direccion = models.TextField('Direccion')
    localizacion = models.ForeignKey('Localizacion', on_delete=models.CASCADE)
    horario_atencion = models.CharField('Horario', max_length=100, blank=True)
    telefono = models.CharField('Telefono', max_length=100, blank=True)
    imagen = models.ImageField('Imagen', upload_to='stores/', blank=True)
    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'

    def __str__(self):
        return self.nombre

    def __iter__(self):
        return [ self.nombre,
                 self.direccion,
                 self.localizacion,
                 self.horario_atencion,
                 self.telefono,
                 self.imagen]

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tienda = models.ForeignKey('Tiendas', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()
