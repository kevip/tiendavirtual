from django.conf.urls import url
from productos import views

urlpatterns = [
    url(r'^catalogo/$', views.catalogo, name='catalogo'),
]