from rest_framework import serializers

from .models import (
    ReporteActividad,
)


class ReporteActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteActividad
        fields = '__all__'