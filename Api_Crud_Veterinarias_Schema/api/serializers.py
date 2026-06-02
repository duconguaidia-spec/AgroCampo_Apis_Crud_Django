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
    # Para escritura (POST/PUT)
    id_veterinaria_id = serializers.PrimaryKeyRelatedField(
        queryset=Veterinaria.objects.all(), source='id_veterinaria', write_only=True
    )
    id_especialidad_id = serializers.PrimaryKeyRelatedField(
        queryset=Especialidad.objects.all(), source='id_especialidad', write_only=True
    )
    # Para lectura (GET)
    id_veterinaria = VeterinariaSerializer(read_only=True)
    id_especialidad = EspecialidadSerializer(read_only=True)

    class Meta:
        model = VeterinariaEspecialidad
        fields = '__all__'


# Serializador para VeterinariaServicio
class VeterinariaServicioSerializer(serializers.ModelSerializer):
    # Para escritura (POST/PUT)
    id_veterinaria_id = serializers.PrimaryKeyRelatedField(
        queryset=Veterinaria.objects.all(), source='id_veterinaria', write_only=True
    )
    id_servicio_general_id = serializers.PrimaryKeyRelatedField(
        queryset=ServicioGeneral.objects.all(), source='id_servicio_general', write_only=True
    )
    # Para lectura (GET)
    id_veterinaria = VeterinariaSerializer(read_only=True)
    id_servicio_general = ServicioGeneralSerializer(read_only=True)

    class Meta:
        model = VeterinariaServicio
        fields = '__all__'


# Serializador para ServicioVeterinaria
class ServicioVeterinariaSerializer(serializers.ModelSerializer):
    # Para escritura (POST/PUT)
    id_veterinaria_id = serializers.PrimaryKeyRelatedField(
        queryset=Veterinaria.objects.all(), source='id_veterinaria', write_only=True
    )
    # Para lectura (GET)
    id_veterinaria = VeterinariaSerializer(read_only=True)

    class Meta:
        model = ServicioVeterinaria
        fields = '__all__'


# Serializador para ProductoVeterinaria
class ProductoVeterinariaSerializer(serializers.ModelSerializer):
    # Para escritura (POST/PUT)
    id_veterinaria_id = serializers.PrimaryKeyRelatedField(
        queryset=Veterinaria.objects.all(), source='id_veterinaria', write_only=True
    )
    # Para lectura (GET)
    id_veterinaria = VeterinariaSerializer(read_only=True)

    class Meta:
        model = ProductoVeterinaria
        fields = '__all__'


# Serializador para ResenaVeterinaria
class ResenaVeterinariaSerializer(serializers.ModelSerializer):
    # Para escritura (POST/PUT)
    id_veterinaria_id = serializers.PrimaryKeyRelatedField(
        queryset=Veterinaria.objects.all(), source='id_veterinaria', write_only=True
    )
    # Para lectura (GET)
    id_veterinaria = VeterinariaSerializer(read_only=True)

    class Meta:
        model = ResenaVeterinaria
        fields = '__all__'