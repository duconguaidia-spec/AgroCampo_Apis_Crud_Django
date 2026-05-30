from rest_framework import serializers

from .models import(
Categoria,
respuestaforo,
temaforo,
videoeducativo
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class respuestaforoSerializer(serializers.ModelSerializer):
    class Meta:
        model = respuestaforo
        fields = '__all__'

class temaforoSerializer(serializers.ModelSerializer):
    class Meta:
        model = temaforo
        fields = '__all__'

class videoeducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoeducativo
        fields = '__all__'