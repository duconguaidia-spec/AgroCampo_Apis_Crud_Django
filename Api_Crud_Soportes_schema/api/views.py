from rest_framework import viewsets

from .models import (
    categoriapreguntas,
    preguntafrecuente
)

from .serializers import (
    CategoriaSerializer,
    preguntafrecuenteSerializer,
    
)


class categoriapreguntasViewSet(viewsets.ModelViewSet):
    queryset = categoriapreguntas.objects.all()
    serializer_class = CategoriaSerializer


class preguntafrecuenteViewSet(viewsets.ModelViewSet):
    queryset = preguntafrecuente.objects.all()
    serializer_class = preguntafrecuenteSerializer



