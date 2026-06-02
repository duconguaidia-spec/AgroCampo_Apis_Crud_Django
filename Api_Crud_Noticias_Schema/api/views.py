from django.shortcuts import render

from rest_framework import viewsets

from .models import (
    Noticias
)

from .serializers import (
    NoticiasSerializer
)

# Crud de tabla jugador (GET, POST, PUT, DELETE)

class NoticiasViewSet(viewsets.ModelViewSet):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer