from django.contrib import admin

from .models import Proveedor,Compra

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'direccion', 'correo', 'telefono')
    search_fields = ('nombre',)
@admin.register(Compra)
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'proveedor', 'fecha', 'costo')
    search_fields = ('nombre',)
