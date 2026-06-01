from rest_framework import viewsets

from .models import (
    AuditoriaUsuario,
    Contrasena,
    PerfilExtendido,
    Rol,
    TokenRecuperacion,
    Usuario,
    VerificacionDosPasos,
)
from .serializers import (
    AuditoriaUsuarioSerializer,
    ContrasenaSerializer,
    PerfilExtendidoSerializer,
    RolSerializer,
    TokenRecuperacionSerializer,
    UsuarioSerializer,
    VerificacionDosPasosSerializer,
)


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ContrasenaViewSet(viewsets.ModelViewSet):
    queryset = Contrasena.objects.all()
    serializer_class = ContrasenaSerializer


class PerfilExtendidoViewSet(viewsets.ModelViewSet):
    queryset = PerfilExtendido.objects.all()
    serializer_class = PerfilExtendidoSerializer


class TokenRecuperacionViewSet(viewsets.ModelViewSet):
    queryset = TokenRecuperacion.objects.all()
    serializer_class = TokenRecuperacionSerializer


class VerificacionDosPasosViewSet(viewsets.ModelViewSet):
    queryset = VerificacionDosPasos.objects.all()
    serializer_class = VerificacionDosPasosSerializer


class AuditoriaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaUsuario.objects.all()
    serializer_class = AuditoriaUsuarioSerializer
