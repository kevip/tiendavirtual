from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Cliente, Localizacion, Tiendas, Empleado


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ('id', User,)
    search_fields = ('nombre',)

@admin.register(Localizacion)
class LocalizacionAdmin(admin.ModelAdmin):

    list_display = ('id', 'latitud', 'longitud')
    search_fields = ('id',)

@admin.register(Tiendas)
class TiendasAdmin(admin.ModelAdmin):

	list_display = ('id','nombre','direccion','localizacion')
    #search_fields = ('nombre',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):

    list_display = ('id', User,'tienda')
    search_fields = ('nombre',)