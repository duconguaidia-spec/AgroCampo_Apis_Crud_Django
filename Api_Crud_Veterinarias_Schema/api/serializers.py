from rest_framework import serializers

from .models import (
    Especialidad,
    ServicioGeneral,
    Veterinaria,
    VeterinariaEspecialidad,
    VeterinariaServicio,
    ServicioVeterinaria,
    ProductoVeterinaria,
    ResenaVeterinaria,
)


# Serializador para Especialidad
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'


# Serializador para ServicioGeneral
class ServicioGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioGeneral
        fields = '__all__'


# Serializador para Veterinaria
class VeterinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinaria
        fields = '__all__'


# Serializador para VeterinariaEspecialidad
class VeterinariaEspecialidadSerializer(serializers.ModelSerializer):
    id_veterinaria = serializers.StringRelatedField()
    id_especialidad = serializers.StringRelatedField()

    class Meta:
        model = VeterinariaEspecialidad
        fields = '__all__'


# Serializador para VeterinariaServicio
class VeterinariaServicioSerializer(serializers.ModelSerializer):
    id_veterinaria = serializers.StringRelatedField()
    id_servicio_general = serializers.StringRelatedField()

    class Meta:
        model = VeterinariaServicio
        fields = '__all__'


# Serializador para ServicioVeterinaria
class ServicioVeterinariaSerializer(serializers.ModelSerializer):
    id_veterinaria = serializers.StringRelatedField()

    class Meta:
        model = ServicioVeterinaria
        fields = '__all__'


# Serializador para ProductoVeterinaria
class ProductoVeterinariaSerializer(serializers.ModelSerializer):
    id_veterinaria = serializers.StringRelatedField()

    class Meta:
        model = ProductoVeterinaria
        fields = '__all__'


# Serializador para ResenaVeterinaria
class ResenaVeterinariaSerializer(serializers.ModelSerializer):
    id_veterinaria = serializers.StringRelatedField()

    class Meta:
        model = ResenaVeterinaria
        fields = '__all__'