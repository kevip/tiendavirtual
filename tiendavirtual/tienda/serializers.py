from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tiendas,Localizacion

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacion
        fields = '__all__'

class TiendasSerializer(serializers.ModelSerializer):
    localizacion = LocalizacionSerializer(many=False, read_only=True)
    class Meta:
        model = Tiendas
        fields = '__all__'