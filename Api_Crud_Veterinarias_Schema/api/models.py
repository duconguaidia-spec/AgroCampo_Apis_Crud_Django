from django.db import models


# Modelo tabla Especialidad
class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=80, unique=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_especialidad

    class Meta:
        db_table = 'Especialidad'


# Modelo tabla ServicioGeneral
class ServicioGeneral(models.Model):
    id_servicio_general = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_servicio

    class Meta:
        db_table = 'ServicioGeneral'


# Modelo tabla Veterinaria
class Veterinaria(models.Model):
    id_veterinaria = models.AutoField(primary_key=True)
    nombre_clinica = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=12)
    correo_publico = models.CharField(max_length=100, null=True, blank=True)
    horario_atencion = models.CharField(max_length=150, null=True, blank=True)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    id_usuario = models.IntegerField(null=True, blank=True)
    aprobado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_clinica

    class Meta:
        db_table = 'Veterinaria'


# Modelo tabla ProductoVeterinaria
class ProductoVeterinaria(models.Model):
    id_producto_vet = models.AutoField(primary_key=True)
    id_veterinaria = models.ForeignKey(
        Veterinaria,
        on_delete=models.CASCADE,
        db_column='id_veterinaria'
    )
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'ProductoVeterinaria'


# Modelo tabla ResenaVeterinaria
class ResenaVeterinaria(models.Model):
    id_resena = models.AutoField(primary_key=True)
    id_veterinaria = models.ForeignKey(
        Veterinaria,
        on_delete=models.CASCADE,
        db_column='id_veterinaria'
    )
    id_usuario = models.IntegerField()
    calificacion = models.IntegerField()
    comentario = models.CharField(max_length=500, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Reseña {self.id_resena} - {self.id_veterinaria}'

    class Meta:
        db_table = 'ResenaVeterinaria'


# Modelo tabla ServicioVeterinaria
class ServicioVeterinaria(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    id_veterinaria = models.ForeignKey(
        Veterinaria,
        on_delete=models.CASCADE,
        db_column='id_veterinaria'
    )
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_servicio

    class Meta:
        db_table = 'ServicioVeterinaria'


# Modelo tabla tr_VeterinariaEspecialidad
class VeterinariaEspecialidad(models.Model):
    id_vet_especialidad = models.AutoField(primary_key=True)
    id_veterinaria = models.ForeignKey(
        Veterinaria,
        on_delete=models.CASCADE,
        db_column='id_veterinaria'
    )
    id_especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.RESTRICT,
        db_column='id_especialidad'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id_veterinaria} - {self.id_especialidad}'

    class Meta:
        db_table = 'tr_VeterinariaEspecialidad'
        unique_together = ('id_veterinaria', 'id_especialidad')


# Modelo tabla tr_VeterinariaServicio
class VeterinariaServicio(models.Model):
    id_vet_servicio = models.AutoField(primary_key=True)
    id_veterinaria = models.ForeignKey(
        Veterinaria,
        on_delete=models.CASCADE,
        db_column='id_veterinaria'
    )
    id_servicio_general = models.ForeignKey(
        ServicioGeneral,
        on_delete=models.RESTRICT,
        db_column='id_servicio_general'
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id_veterinaria} - {self.id_servicio_general}'

    class Meta:
        db_table = 'tr_VeterinariaServicio'
        unique_together = ('id_veterinaria', 'id_servicio_general')