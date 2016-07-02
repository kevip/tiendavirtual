from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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


def catalogo_categoria(request, id_categoria):

    categoria = get_object_or_404(Categoria, id=id_categoria)
    p = Producto.objects.filter(categoria = categoria.id)
    c = Categoria.objects.all()
    s = Subcategoria.objects.all()

    return render(request, "presentation/products.html", {'productos': p,
                                                          'categorias': c,
                                                          'subcategorias': s,
                                                          })
