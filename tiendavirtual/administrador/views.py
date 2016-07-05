from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from administrador.forms import RegistrarTiendaForm, RegistrarLocalizacionForm,RegistrarProducto
from tienda.models import Tiendas
#from productos.models import Productos

# Create your views here.

def administrador(request):
    template = loader.get_template("administrador/dashboard.html")
    context = {}
    return HttpResponse(template.render(context, request))


def nueva_tienda(request):
    form = RegistrarTiendaForm
    forml = RegistrarLocalizacionForm
    template = loader.get_template("administrador/tienda/nueva_tienda.html")
    context = {
        'form': form,
        'forml': forml,
    }
    return HttpResponse(template.render(context, request))


def registrar_tienda(request):
    if request.method == "POST":
        form = RegistrarTiendaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Se registró tienda con éxito <a href='/administrador/tiendas'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/administrador')

def dashboard_tiendas(request):
    template = loader.get_template("administrador/tienda/dashboard_tiendas.html")
    context = {}
    return HttpResponse(template.render(context, request))

def dashboard_productos(request):
    template = loader.get_template("administrador/productos/dashboard_productos.html")
    context = {}
    return HttpResponse(template.render(context, request))

def lista_tiendas(request):
    template = loader.get_template("administrador/tienda/lista_tiendas.html")
    tiendas = Tiendas.objects.all()
    context = {'tiendas':tiendas}
    return HttpResponse(template.render(context, request))

def registrar_producto(request):
    if request.method == "POST":
        form = RegistrarProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Se registró producto con éxito <a href='/administrador/productos'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/administrador')


def nuevo_producto(request):
    form = RegistrarProducto
    template = loader.get_template("administrador/productos/nuevo_producto.html")
    context = {
    'form': form,        
    }
    return HttpResponse(template.render(context, request))

def lista_productos(request):
    template = loader.get_template("administrador/productos/lista_productos.html")
    productos = Productos.objects.all()
    context = {'productos':productos}
    return HttpResponse(template.render(context, request))