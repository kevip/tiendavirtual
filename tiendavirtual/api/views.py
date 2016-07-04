from rest_framework.generics import (
    CreateAPIView)

from .serializers import (
    LocalizacionCreateSerializer)


class LocalizacionCreateAPIView(CreateAPIView):
    serializer_class = LocalizacionCreateSerializer