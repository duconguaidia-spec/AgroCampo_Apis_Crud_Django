from rest_framework import serializers

from .models import (
    categoria,
    respuestaForo,
    temaForo,
    videoEducativo
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'


class respuestaForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = respuestaForo
        fields = '__all__'


class temaForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = temaForo
        fields = '__all__'


class videoEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoEducativo
        fields = '__all__'