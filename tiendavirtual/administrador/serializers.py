from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from tienda.models import Tiendas,Localizacion

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacion
        fields = '__all__'

class TiendasSerializer(serializers.ModelSerializer):
    localizacion = LocalizacionSerializer(many=False, read_only=True)
    class Meta:
        model = Tiendas
        fields = '__all__'

class LocalizacionCreateSerializer(ModelSerializer):
    class Meta:
        model = Localizacion
        fields = [
            'id',
            'latitud',
            'longitud'
        ]