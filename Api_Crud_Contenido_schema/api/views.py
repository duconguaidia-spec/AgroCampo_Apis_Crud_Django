from django.shortcuts import render

from rest_framework import viewsets

from .models import(
    Categoria,
    respuestaforo,
    temaforo,
    videoeducativo
)

from .serializers import(
    CategoriaSerializer,
    respuestaforoSerializer,
    temaforoSerializer,
    videoeducativoSerializer
    
)

class categoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class respuestaforoViewSet(viewsets.ModelViewSet):
    queryset = respuestaforo.objects.all()
    serializer_class = respuestaforoSerializer

class temaforoViewSet(viewsets.ModelViewSet):
    queryset = temaforo.objects.all()
    serializer_class = temaforoSerializer

class videoeducativoViewSet(viewsets.ModelViewSet):
    queryset = videoeducativo.objects.all()
    serializer_class = videoeducativoSerializer