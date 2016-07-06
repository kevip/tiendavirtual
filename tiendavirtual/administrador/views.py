from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from administrador.forms import (
    RegistrarTiendaForm,
    RegistrarLocalizacionForm,
    RegistrarProducto,
    RegistrarProveedorForm,
    RegistrarCompraForm,
    EditarProductoForm,)
from tienda.models import Tiendas
from productos.models import Producto
from compras.models import Proveedor,Compra
# Create your views here.

def administrador(request):
    template = loader.get_template("administrador/dashboard.html")
    context = {}
    return HttpResponse(template.render(context, request))

#TIENDAS
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

def lista_tiendas(request):
    template = loader.get_template("administrador/tienda/lista_tiendas.html")
    tiendas = Tiendas.objects.all()
    context = {'tiendas':tiendas}
    return HttpResponse(template.render(context, request))


#PRODUCTOS
def nuevo_producto(request):
    form = RegistrarProducto
    template = loader.get_template("administrador/productos/nuevo_producto.html")
    context = {
    'form': form,        
    }
    return HttpResponse(template.render(context, request))

def lista_productos(request):
    template = loader.get_template("administrador/productos/lista_productos.html")
    productos = Producto.objects.filter(estado=1)
    context = {'productos':productos}
    return HttpResponse(template.render(context, request))

def registrar_producto(request):
    if request.method == "POST":
        form = RegistrarProducto(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Se editó producto con éxito <a href='/administrador/lista_productos'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/administrador')

def editar_producto(request,id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    producto = model_to_dict(producto)
    form = EditarProductoForm(initial= producto)
    template = loader.get_template("administrador/productos/nuevo_producto.html")
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def eliminar_producto(request,id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    producto.estado = 0
    producto.save()
    return HttpResponseRedirect('/administrador/lista_productos/')

def dashboard_productos(request):
    template = loader.get_template("administrador/productos/dashboard_productos.html")
    context = {}
    return HttpResponse(template.render(context, request))

#COMPRAS
def nueva_compra(request):
    form = RegistrarProducto
    formc = RegistrarCompraForm
    template = loader.get_template("administrador/compras/nueva_compra.html")
    context = {
        'form': form,
        'formc': formc,
    }
    return HttpResponse(template.render(context, request))

def lista_compras(request):
    pass
    template = loader.get_template("administrador/compras/lista_compras.html")
    compras = Compra.objects.all()
    context = {'compras':compras}
    return HttpResponse(template.render(context, request))

def registrar_compra(request):
    if request.method == "POST":
        form = RegistrarProducto(request.POST, request.FILES)
        fecha = request.POST.get('fecha', None)
        proveedor = request.POST.get('proveedor', None)
        costo = request.POST.get('costo', None)
        proveedor = Proveedor.objects.get(id=proveedor)
        if form.is_valid():
            nuevo_producto = form.save()
            compra = Compra(fecha=fecha, proveedor=proveedor, costo=costo, producto=nuevo_producto)
            compra.save()
            return HttpResponse("<h1>Se registró compra con éxito <a href='/administrador/compras'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/administrador')

def dashboard_compras(request):
    template = loader.get_template("administrador/compras/dashboard_compras.html")
    context = {}
    return HttpResponse(template.render(context, request))

#FIN COMPRAS

#PROVEEDORES
def nuevo_proveedor(request):
    form = RegistrarProveedorForm
    template = loader.get_template("administrador/proveedores/nuevo_proveedor.html")
    context = {
    'form': form,
    }
    return HttpResponse(template.render(context, request))

def lista_proveedores(request):
    template = loader.get_template("administrador/proveedores/lista_proveedores.html")
    proveedores= Proveedor.objects.all()
    context = {'proveedores':proveedores}
    return HttpResponse(template.render(context, request))

def registrar_proveedor(request):
    if request.method == "POST":
        razon_social = request.POST.get('razon_social', None)
        direccion = request.POST.get('direccion', None)
        correo = request.POST.get('correo', None)
        telefono = request.POST.get('telefono', None)
        proveedor = Proveedor(razon_social=razon_social, direccion=direccion, correo=correo, telefono=telefono)
        proveedor.save()
        return HttpResponse("<h1>Se registró proveedor con éxito <a href='/administrador/proveedores'>Volver</a></h1>")
    else:
        return HttpResponseRedirect('/administrador')

def dashboard_proveedores(request):
    template = loader.get_template("administrador/proveedores/dashboard_proveedores.html")
    context = {}
    return HttpResponse(template.render(context, request))

#FIN PROVEEDORES