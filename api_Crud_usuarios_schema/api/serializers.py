from rest_framework import serializers

from .models import (
    AuditoriaUsuario,
    Contrasena,
    PerfilExtendido,
    Rol,
    TokenRecuperacion,
    Usuario,
    VerificacionDosPasos,
)


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):

    rol_detalle = RolSerializer(
        source='id_rol',
        read_only=True
    )

    class Meta:
        model = Usuario
        fields = '__all__'


class ContrasenaSerializer(serializers.ModelSerializer):

    usuario_detalle = UsuarioSerializer(
        source='id_usuario',
        read_only=True
    )

    class Meta:
        model = Contrasena
        fields = '__all__'


class PerfilExtendidoSerializer(serializers.ModelSerializer):

    usuario_detalle = UsuarioSerializer(
        source='id_usuario',
        read_only=True
    )

    class Meta:
        model = PerfilExtendido
        fields = '__all__'


class TokenRecuperacionSerializer(serializers.ModelSerializer):

    usuario_detalle = UsuarioSerializer(
        source='id_usuario',
        read_only=True
    )

    class Meta:
        model = TokenRecuperacion
        fields = '__all__'


class VerificacionDosPasosSerializer(serializers.ModelSerializer):

    usuario_detalle = UsuarioSerializer(
        source='id_usuario',
        read_only=True
    )

    class Meta:
        model = VerificacionDosPasos
        fields = '__all__'


class AuditoriaUsuarioSerializer(serializers.ModelSerializer):

    usuario_detalle = UsuarioSerializer(
        source='id_usuario',
        read_only=True
    )

    class Meta:
        model = AuditoriaUsuario
        fields = '__all__'
        