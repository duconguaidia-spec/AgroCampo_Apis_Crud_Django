from rest_framework import viewsets

from .models import (
    categoria,
    respuestaForo,
    temaForo,
    videoEducativo
)

from .serializers import (
    CategoriaSerializer,
    respuestaForoSerializer,
    temaForoSerializer,
    videoEducativoSerializer
)


class categoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer


class respuestaForoViewSet(viewsets.ModelViewSet):
    queryset = respuestaForo.objects.all()
    serializer_class = respuestaForoSerializer


class temaForoViewSet(viewsets.ModelViewSet):
    queryset = temaForo.objects.all()
    serializer_class = temaForoSerializer


class videoEducativoViewSet(viewsets.ModelViewSet):
    queryset = videoEducativo.objects.all()
    serializer_class = videoEducativoSerializer