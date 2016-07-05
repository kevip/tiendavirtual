from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from administrador.forms import RegistrarTiendaForm, RegistrarLocalizacionForm,RegistrarProducto, RegistrarProveedorForm
from tienda.models import Tiendas
from productos.models import Producto
from compras.models import Proveedor
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
    productos = Producto.objects.all()
    context = {'productos':productos}
    return HttpResponse(template.render(context, request))

def registrar_producto(request):
    if request.method == "POST":
        form = RegistrarProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Se registró producto con éxito <a href='/administrador/productos'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/administrador')

def dashboard_productos(request):
    template = loader.get_template("administrador/productos/dashboard_productos.html")
    context = {}
    return HttpResponse(template.render(context, request))

#COMPRAS
def nueva_compra(request):
    form = RegistrarProducto
    template = loader.get_template("administrador/compras/nueva_compra.html")
    context = {
    'form': form,
    }
    return HttpResponse(template.render(context, request))

def lista_compras(request):
    pass
    template = loader.get_template("administrador/compras/lista_compras.html")
    productos = Producto.objects.all()
    context = {'productos':productos}
    return HttpResponse(template.render(context, request))

def registrar_compra(request):
    '''
    if request.method == "POST":
        form = RegistrarProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Se registró producto con éxito <a href='/administrador/productos'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/administrador')
    '''
def dashboard_compras(request):
    template = loader.get_template("administrador/compras/dashboard_compras.html")
    context = {}
    return HttpResponse(template.render(context, request))

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