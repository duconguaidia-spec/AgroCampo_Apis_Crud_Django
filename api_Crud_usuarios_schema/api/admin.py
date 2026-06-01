from django.contrib import admin

from .models import (
    AuditoriaUsuario,
    Contrasena,
    PerfilExtendido,
    Rol,
    TokenRecuperacion,
    Usuario,
    VerificacionDosPasos,
)


admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Contrasena)
admin.site.register(PerfilExtendido)
admin.site.register(TokenRecuperacion)
admin.site.register(VerificacionDosPasos)
admin.site.register(AuditoriaUsuario)
