from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    EspecialidadViewSet,
    ServicioGeneralViewSet,
    VeterinariaViewSet,
    VeterinariaEspecialidadViewSet,
    VeterinariaServicioViewSet,
    ServicioVeterinariaViewSet,
    ProductoVeterinariaViewSet,
    ResenaVeterinariaViewSet,
)

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Veterinarias",
        default_version='v1',
        description="Documentación de la API de Veterinarias",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

# Registro de endpoints del api
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'servicios-generales', ServicioGeneralViewSet)
router.register(r'veterinarias', VeterinariaViewSet)
router.register(r'veterinaria-especialidades', VeterinariaEspecialidadViewSet)
router.register(r'veterinaria-servicios', VeterinariaServicioViewSet)
router.register(r'servicios-veterinaria', ServicioVeterinariaViewSet)
router.register(r'productos-veterinaria', ProductoVeterinariaViewSet)
router.register(r'resenas-veterinaria', ResenaVeterinariaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]