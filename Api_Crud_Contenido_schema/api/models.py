from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre


class temaForo(models.Model):
    id_tema = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()

    id_autor = models.ForeignKey(User, on_delete=models.CASCADE)

    id_categoria = models.ForeignKey(
        categoria,
        on_delete=models.CASCADE
    )

    estado = models.CharField(max_length=20, default='Pendiente')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'temaforo'

    def __str__(self):
        return self.titulo


class respuestaForo(models.Model):
    id_respuesta = models.AutoField(primary_key=True)

    id_tema = models.ForeignKey(
        temaForo,
        on_delete=models.CASCADE
    )

    id_autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'respuestaforo'

    def __str__(self):
        return self.descripcion


class videoEducativo(models.Model):
    id_video = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    url_video = models.CharField(max_length=255)
    id_usuario = models.IntegerField()
    estado = models.CharField(max_length=20, default='Borrador')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'videoeducativo'

    def __str__(self):
        return self.titulo