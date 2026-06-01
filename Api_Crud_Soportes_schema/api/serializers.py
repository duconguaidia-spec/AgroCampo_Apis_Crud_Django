from rest_framework import serializers

from .models import (
    categoriapreguntas,
    preguntafrecuente
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoriapreguntas
        fields = '__all__'


class preguntafrecuenteSerializer(serializers.ModelSerializer):

    id_categoria_faq = CategoriaSerializer(read_only=True)
    
    class Meta:
        model = preguntafrecuente
        fields = '__all__'

