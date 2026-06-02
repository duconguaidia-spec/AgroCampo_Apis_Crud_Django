from rest_framework import serializers
from django.contrib.auth.models import User
from .models import respuestaForo, temaForo, categoria, videoEducativo


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

    id_autor = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )

    id_tema = serializers.PrimaryKeyRelatedField(
        queryset=temaForo.objects.all(),
        write_only=True
    )

    id_autor_nombre = serializers.StringRelatedField(
        source='id_autor',
        read_only=True
    )

    id_tema_titulo = serializers.StringRelatedField(
        source='id_tema',
        read_only=True
    )

    class Meta:
        model = respuestaForo
        fields = [
            'id_respuesta',
            'id_tema',
            'id_autor', 
            'descripcion',
            'activo',
            'fecha_creacion',
            'fecha_modificacion',
            'id_autor_nombre',
            'id_tema_titulo'
        ]


class temaForoSerializer(serializers.ModelSerializer):

    id_autor = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )

    id_categoria = serializers.PrimaryKeyRelatedField(
        queryset=categoria.objects.all(),
        write_only=True
    )

    id_autor_nombre = serializers.StringRelatedField(
        source='id_autor',
        read_only=True
    )

    id_categoria_nombre = serializers.StringRelatedField(
        source='id_categoria',
        read_only=True
    )

    class Meta:
        model = temaForo
        fields = [
            'id_tema',
            'titulo',
            'descripcion',
            'id_autor',
            'id_categoria',
            'estado',
            'activo',
            'fecha_creacion',
            'fecha_modificacion',
            'id_autor_nombre',
            'id_categoria_nombre'
        ]


class videoEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoEducativo
        fields = '__all__'