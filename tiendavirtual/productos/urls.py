from django.conf.urls import url
from productos import views

urlpatterns = [
    url(r'^catalogo/$', views.catalogo, name='catalogo'),
    url(r'^catalogo/categoria/(?P<id_categoria>[0-9]+)/$', views.catalogo_categoria, name='catalogo_categoria'),
    url(r'^catalogo/categoria/(?P<id_categoria>[0-9]+)/subcategoria/(?P<id_subcategoria>[0-9]+)$', views.catalogo_subcategoria, name='catalogo_subcategoria'),
]