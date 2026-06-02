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

    subasta_detalle = SubastaSerializer(
        source='id_subasta',
        read_only=True
    )

    categoria_detalle = CategoriaGanadoSerializer(
        source='id_categoria_ganado',
        read_only=True
    )

    class Meta:
        model = TrPreciosubastaganado
        fields = '__all__'