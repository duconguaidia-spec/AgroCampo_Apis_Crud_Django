
from django.db import models


class CategoriaGanado(models.Model):
    id_categoria_ganado = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=10)
    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categoria_ganado'


class Subasta(models.Model):
    id_subasta = models.AutoField(primary_key=True)
    fecha_subasta = models.DateField()
    ubicacion = models.CharField(max_length=150, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario_registra = models.IntegerField()
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subasta'


class TrPreciosubastaganado(models.Model):
    id_precio_subasta = models.AutoField(primary_key=True)
    id_subasta = models.ForeignKey(Subasta, models.DO_NOTHING, db_column='id_subasta')
    id_categoria_ganado = models.ForeignKey(CategoriaGanado, models.DO_NOTHING, db_column='id_categoria_ganado')
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField()
    fecha_modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tr_precioSubastaGanado'
        unique_together = (('id_subasta', 'id_categoria_ganado'),)
