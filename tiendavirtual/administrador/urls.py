from django.conf.urls import url
from administrador import views

urlpatterns = [
    url(r'^administrador/$', views.administrador, name='administrador'),
    url(r'^administrador/nueva_tienda$', views.nueva_tienda, name='nueva_tienda'),
    url(r'^administrador/registrar_tienda', views.registrar_tienda, name='registrar_tienda'),
]