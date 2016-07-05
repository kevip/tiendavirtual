from django.contrib import admin

from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'direccion', 'correo', 'telefono')
    search_fields = ('nombre',)
