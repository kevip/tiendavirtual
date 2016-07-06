from django.conf.urls import url
from administrador import views

urlpatterns = [
    url(r'^administrador/$', views.administrador, name='administrador'),
    #tiendas
    url(r'^administrador/nueva_tienda$', views.nueva_tienda, name='nueva_tienda'),
    url(r'^administrador/registrar_tienda', views.registrar_tienda, name='registrar_tienda'),
    url(r'^administrador/tiendas', views.dashboard_tiendas, name='dashboard_tiendas'),
    url(r'^administrador/lista_tiendas', views.lista_tiendas, name='lista_tiendas'),
    #productos
    url(r'^administrador/lista_productos', views.lista_productos, name='lista_productos'),
    url(r'^administrador/productos', views.dashboard_productos, name='dashboard_productos'),
    url(r'^administrador/nuevo_producto', views.nuevo_producto, name='nuevo_producto'),
    url(r'^administrador/registrar_producto', views.registrar_producto, name='registrar_producto'),
    url(r'^administrador/eliminar_producto/(?P<id_producto>[0-9]+)/$', views.eliminar_producto, name='eliminar_producto'),
    url(r'^administrador/editar_producto/(?P<id_producto>[0-9]+)/$', views.editar_producto, name='editar_producto'),
    #compras
    url(r'^administrador/compras', views.dashboard_compras, name='dashboard_compras'),
    url(r'^administrador/nueva_compra', views.nueva_compra, name='nueva_compra'),
    url(r'^administrador/registrar_compra', views.registrar_compra, name='registrar_compra'),
    url(r'^administrador/lista_compras', views.lista_compras, name='lista_compras'),
    #proveedores
    url(r'^administrador/proveedores', views.dashboard_proveedores, name='dashboard_proveedores'),
    url(r'^administrador/nuevo_proveedor', views.nuevo_proveedor, name='nuevo_proveedor'),
    url(r'^administrador/registrar_proveedor', views.registrar_proveedor, name='registrar_proveedor'),
    url(r'^administrador/lista_proveedores', views.lista_proveedores, name='lista_proveedores'),

]