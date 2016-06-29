from django.contrib import admin
from .models import Producto, Categoria, Subcategoria


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'descripcion', 'estado', 'imagen', 'categoria')
    search_fields = ('nombre',)

    def categoria(self, Categoria):
        return Categoria.nombre



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'detalle', 'categoria')

    def categoria(self, Categoria):
        return Categoria.nombre
    search_fields = ('nombre',)