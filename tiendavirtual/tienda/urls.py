from django.conf.urls import url
from tienda import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cerrar_sesion/$',views.cerrar_sesion,name='cerrar_sesion'),
    url(r'^home/$', views.home, name='home'),
    url(r'^iniciar_sesion/$', views.iniciar_sesion, name='iniciar_sesion'),
    url(r'^registrar_usuario/$', views.registrar_usuario, name='registrar_usuario'),
    url(r'^stores/$', views.stores, name='stores'),
    url(r'^api/tiendas/$', views.tiendas, name='tiendas'),
]
