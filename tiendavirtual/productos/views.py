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
    s = Subcategoria.objects.filter(categoria=categoria.id)

    template = loader.get_template("presentation/products.html")
    context = {
        'productos': p,
        'categorias': c,
        'subcategorias': s,
        'categoria': categoria
    }
    return HttpResponse(template.render(context, request))

def catalogo_subcategoria(request, id_categoria, id_subcategoria):

    categoria = get_object_or_404(Categoria, id=id_categoria)
    subcategoria = get_object_or_404(Subcategoria, id=id_subcategoria)
    p = Producto.objects.filter(categoria = categoria.id, subcategoria= subcategoria.id)
    c = Categoria.objects.all()
    s = Subcategoria.objects.filter(categoria=categoria.id)

    template = loader.get_template("presentation/products.html")
    context = {
        'productos': p,
        'categorias': c,
        'subcategorias': s,
        'categoria': categoria,
        'subcategoria': subcategoria
    }
    return HttpResponse(template.render(context, request))