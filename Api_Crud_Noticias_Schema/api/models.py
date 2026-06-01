from django.db import models

# Create your models here.
class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20)
    cuerpo = models.TextField(null=True, blank=True)
    url_video = models.CharField(max_length=255, null=True, blank=True)
    imagen_destacada = models.CharField(max_length=255)
    fuente = models.CharField(max_length=150, null=True, blank=True)
    fecha_noticia = models.DateField(null=True, blank=True)
    id_usuario = models.IntegerField()
    acceso_limitado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, default='Borrador')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'noticias'