from django.conf.urls import url
from .views import(
    LocalizacionCreateAPIView
)

urlpatterns = [
    url(r'^api/localizacion/crear', LocalizacionCreateAPIView.as_view(), name='crear'),
]