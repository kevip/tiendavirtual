from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from administrador.forms import RegistrarTiendaForm, RegistrarLocalizacionForm

# Create your views here.


def nueva_tienda(request):
    form = RegistrarTiendaForm
    forml = RegistrarLocalizacionForm
    template = loader.get_template("administrador/nueva_tienda.html")
    context = {
        'form': form,
        'forml': forml,
    }
    return HttpResponse(template.render(context, request))


def registrar_tienda(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre', None)
        direccion = request.POST.get('direccion', None)
        localizacion = request.POST.get('localizacion', None)
        password = request.POST.get('password', None)
        horario_atencion = request.POST.get('horario_atencion', None)
        telefono = request.POST.get('telefono', None)
        imagen = request.POST.get('imagen', None)

        form = RegistrarTiendaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Se registró usuario con éxito <a href='/'>Volver</a></h1>")
        else:
            return HttpResponseRedirect('/')