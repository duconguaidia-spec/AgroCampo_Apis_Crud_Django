
from rest_framework import viewsets

from .models import (
    ReporteActividad,
)

from .serializers import (
    ReporteActividadSerializer,
    
)


class ReporteActividadViewSet(viewsets.ModelViewSet):
    queryset = ReporteActividad.objects.all()
    serializer_class = ReporteActividadSerializer

