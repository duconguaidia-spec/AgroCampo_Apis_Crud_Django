from rest_framework import serializers

from .models import (
    CategoriaGanado,
    Subasta,
    TrPreciosubastaganado
)

class CategoriaGanadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaGanado
        fields = '__all__'

class SubastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subasta
        fields = '__all__'
        
class TrPreciosubastaganadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrPreciosubastaganado
        fields = '__all__'