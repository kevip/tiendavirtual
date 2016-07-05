from django.db import models



class Proveedor(models.Model):
    razon_social = models.CharField('Razon Social', max_length=100)
    direccion = models.CharField('Direccion', max_length=100)
    correo = models.CharField('Correo', max_length=100)
    telefono= models.CharField('Telefono', max_length=100)

    def __str__(self):
        return self.razon_social

class Compra(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    fecha = models.DateField(blank=True)
    costo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

class DetalleCompra(models.Model):
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    compra = models.ForeignKey('Compra', on_delete=models.CASCADE)
    precioUnitario = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()
    descripcion = models.TextField(blank=True)
    ''''
    def __str__(self):
        return "({0}, {1})".format(self.latitud, self.longitud)
    '''