from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    CategoriaGanado,
    Subasta,
    TrPreciosubastaganado
)
from .serializers import (
    CategoriaGanadoSerializer,
    SubastaSerializer,
    TrPreciosubastaganadoSerializer
)
# Create your views here.

class CategoriaGanadoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaGanado.objects.all()
    serializer_class = CategoriaGanadoSerializer

class SubastaViewSet(viewsets.ModelViewSet):
    queryset = Subasta.objects.all()
    serializer_class = SubastaSerializer
    
class TrPreciosubastaganadoViewSet(viewsets.ModelViewSet):
    queryset = TrPreciosubastaganado.objects.all()
    serializer_class = TrPreciosubastaganadoSerializer

