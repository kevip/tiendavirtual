from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from administrador.forms import RegistrarTiendaForm, RegistrarLocalizacionForm

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
            return HttpResponse("<h1>Se registró tienda con éxito <a href='/administrador/nueva_tienda'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/administrador')

