from django.db import models


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_rol

    class Meta:
        managed = False
        db_table = 'Rol'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    correo = models.CharField(unique=True, max_length=100)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')
    verificacion_dos_pasos = models.BooleanField()
    avatar = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        managed = False
        db_table = 'Usuario'


class Contrasena(models.Model):
    id_contrasena = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    contrasena_hash = models.CharField(max_length=255)
    activa = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contrasena usuario {self.id_usuario_id}"

    class Meta:
        managed = False
        db_table = 'Contrasena'


class PerfilExtendido(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    id_usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='id_usuario')
    direccion = models.CharField(max_length=150, blank=True, null=True)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    intereses = models.CharField(max_length=255, blank=True, null=True)
    redes_sociales = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil {self.id_usuario_id}"

    class Meta:
        managed = False
        db_table = 'PerfilExtendido'


class TokenRecuperacion(models.Model):
    id_token = models.AutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=10)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    expiracion = models.DateTimeField()
    usado = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

    class Meta:
        managed = False
        db_table = 'TokenRecuperacion'


class VerificacionDosPasos(models.Model):
    id_verificacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    tipo_metodo = models.CharField(max_length=20)
    codigo_otp = models.CharField(max_length=10, blank=True, null=True)
    expiracion_otp = models.DateTimeField(blank=True, null=True)
    activo = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo_metodo} - {self.id_usuario_id}"

    class Meta:
        managed = False
        db_table = 'VerificacionDosPasos'


class AuditoriaUsuario(models.Model):
    id_auditoria = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    tipo_evento = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    ip_origen = models.CharField(max_length=45, blank=True, null=True)
    fecha_evento = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo_evento

    class Meta:
        managed = False
        db_table = 'AuditoriaUsuario'
