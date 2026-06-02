from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'roles', RolViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'contrasenas', ContrasenaViewSet)
router.register(r'perfiles_extendidos', PerfilExtendidoViewSet)
router.register(r'tokens_recuperacion', TokenRecuperacionViewSet)
router.register(r'verificaciones_dos_pasos', VerificacionDosPasosViewSet)
router.register(r'auditorias_usuario', AuditoriaUsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
