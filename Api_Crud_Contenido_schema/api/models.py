from django.db import models

#Modelo tabla categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=80)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        db_table = 'categoria'

    )