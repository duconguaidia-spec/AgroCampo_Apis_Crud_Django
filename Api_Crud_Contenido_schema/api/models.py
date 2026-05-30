from datetime import timezone

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

class respuestaforo(models.Model):

    id_respuesta = models.AutoField(primary_key=True)
    id_tema = models.ForeignKey('Tema', on_delete=models.CASCADE)
    id_autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        db_table = 'respuestaforo'

class temaforo(models.Model):
    id_tema = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    id_autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, default='Pendiente')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'temaforo'

class videoeducativo(models.Model):
    id_video = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    url_video = models.CharField(max_length=255)
    id_usuario = models.IntegerField()
    estado = models.CharField(max_length=20, default='Borrador')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'videoeducativo'
