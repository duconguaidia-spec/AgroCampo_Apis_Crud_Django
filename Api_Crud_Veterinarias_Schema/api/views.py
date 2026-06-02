from django.shortcuts import render

from rest_framework import viewsets

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

from .serializers import (
    EspecialidadSerializer,
    ServicioGeneralSerializer,
    VeterinariaSerializer,
    VeterinariaEspecialidadSerializer,
    VeterinariaServicioSerializer,
    ServicioVeterinariaSerializer,
    ProductoVeterinariaSerializer,
    ResenaVeterinariaSerializer,
)


# CRUD tabla Especialidad (GET, POST, PUT, DELETE)
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer


# CRUD tabla ServicioGeneral (GET, POST, PUT, DELETE)
class ServicioGeneralViewSet(viewsets.ModelViewSet):
    queryset = ServicioGeneral.objects.all()
    serializer_class = ServicioGeneralSerializer


# CRUD tabla Veterinaria (GET, POST, PUT, DELETE)
class VeterinariaViewSet(viewsets.ModelViewSet):
    queryset = Veterinaria.objects.all()
    serializer_class = VeterinariaSerializer


# CRUD tabla VeterinariaEspecialidad (GET, POST, PUT, DELETE)
class VeterinariaEspecialidadViewSet(viewsets.ModelViewSet):
    queryset = VeterinariaEspecialidad.objects.all()
    serializer_class = VeterinariaEspecialidadSerializer


# CRUD tabla VeterinariaServicio (GET, POST, PUT, DELETE)
class VeterinariaServicioViewSet(viewsets.ModelViewSet):
    queryset = VeterinariaServicio.objects.all()
    serializer_class = VeterinariaServicioSerializer


# CRUD tabla ServicioVeterinaria (GET, POST, PUT, DELETE)
class ServicioVeterinariaViewSet(viewsets.ModelViewSet):
    queryset = ServicioVeterinaria.objects.all()
    serializer_class = ServicioVeterinariaSerializer


# CRUD tabla ProductoVeterinaria (GET, POST, PUT, DELETE)
class ProductoVeterinariaViewSet(viewsets.ModelViewSet):
    queryset = ProductoVeterinaria.objects.all()
    serializer_class = ProductoVeterinariaSerializer


# CRUD tabla ResenaVeterinaria (GET, POST, PUT, DELETE)
class ResenaVeterinariaViewSet(viewsets.ModelViewSet):
    queryset = ResenaVeterinaria.objects.all()
    serializer_class = ResenaVeterinariaSerializer