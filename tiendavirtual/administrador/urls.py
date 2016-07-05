from django.conf.urls import url
from administrador import views

urlpatterns = [
    url(r'^administrador/$', views.administrador, name='administrador'),
    #tiendas
    url(r'^administrador/nueva_tienda$', views.nueva_tienda, name='nueva_tienda'),
    url(r'^administrador/registrar_tienda', views.registrar_tienda, name='registrar_tienda'),
    url(r'^administrador/tiendas', views.dashboard_tiendas, name='dashboard_tiendas'),
    url(r'^administrador/lista_tiendas', views.lista_tiendas, name='lista_tiendas'),
    url(r'^administrador/lista_productos', views.lista_productos, name='lista_productos'),
    #productos
    url(r'^administrador/productos', views.dashboard_productos, name='dashboard_productos'),
    url(r'^administrador/nuevo_producto', views.nuevo_producto, name='nuevo_producto'),
    url(r'^administrador/registrar_producto', views.registrar_producto, name='registrar_producto'),
]