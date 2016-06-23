from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from .models import Cliente, Tiendas, Localizacion, Empleado

from .forms import RegUsForm

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TiendasSerializer, LocalizacionSerializer
# Create your views here.


def home(request):
    if request.user.is_authenticated():
        return render(request, "presentation/home.html", {})
    else:
        form = RegUsForm()
        return render(request, "presentation/home.html", {
            'form': form,
        })


def iniciar_sesion(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        try:
            user_e = User.objects.get(email=email)
        except User.DoesNotExist:
            user_e = None

        user = authenticate(username=user_e, password=password)

        if not user_e:
            return HttpResponse("<h1>no existe usuario<a href='/'>Volver</a></h1>")
        elif user is not None:
            if user.is_active:
                login(request, user)
        else:
            return HttpResponse("<h1>no se pudo autenticar<a href='/'>Volver</a></h1>")
    return HttpResponseRedirect('/')


def cerrar_sesion(request):
    logout(request)

    return HttpResponseRedirect('/')


def registrar_usuario(request):
    if request.method == "POST":
        action = request.POST.get('action', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        existe_usuario = User.objects.filter(email=email)
        if not existe_usuario:
            usuario = User(first_name=first_name, last_name=last_name, email=email)
            usuario.username = first_name + " " + last_name
            usuario.set_password(password)
            usuario.is_superuser = False
            usuario.save()
            return HttpResponse("<h1>Se registró usuario con éxito <a href='/'>Volver</a></h1>")
        else:
            return HttpResponse("<h1>El usuario ya existe  <a href='/'>Volver</a></h1></h1>")
    return HttpResponseRedirect('/')


def stores(request):
    return render(request, "presentation/stores.html", {})

#api
def products(request):
    return render(request, "presentation/products.html",{})

def tiendas(request):
    localizaciones = Localizacion.objects.all()
    localizaciones = serializers.serialize('json',localizaciones)
    return HttpResponse(localizaciones,content_type="application/json")

class ListStores(APIView):
    def get(self, request):
        tiendas = Tiendas.objects.all()
        serializer = TiendasSerializer(tiendas, many=True)
        return Response(serializer.data)