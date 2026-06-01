from django.db import models
from django.utils import timezone

class ReporteActividad(models.Model):
    id_reporte_actividad = models.AutoField(primary_key=True)
    tipo_reporte = models.CharField(max_length=100)
    fecha_generacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"ReporteActividad {self.id_reporte_actividad} - {self.tipo_reporte}"