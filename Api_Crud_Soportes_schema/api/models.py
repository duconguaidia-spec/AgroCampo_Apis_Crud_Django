from django.db import models


class categoriapreguntas(models.Model):
    id_categoria_preguntas = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=80)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categoriapreguntas'
    
    def __str__(self):
        return self.nombre_categoria    

class preguntafrecuente(models.Model):
    id_faq = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    id_categoria_faq = models.ForeignKey(categoriapreguntas, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'preguntafrecuente'

    def __str__(self):
        return self.pregunta



# Create your models here.
