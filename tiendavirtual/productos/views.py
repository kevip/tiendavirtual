from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto,Categoria,Subcategoria
# Create your views here.


def catalogo(request):
    p = Producto.objects.all()
    c = Categoria.objects.all()
    s = Subcategoria.objects.all()

    return render(request,"presentation/products.html",{'productos': p,
               'categorias': c,
               'subcategorias':s,
               })
