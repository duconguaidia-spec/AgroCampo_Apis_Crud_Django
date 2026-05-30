
from django.urls import include
from django.urls import path


from rest_framework.routers import DefaultRouter

from .views import (
    categoriaViewSet,
    respuestaforoViewSet,
    temaforoViewSet,
    videoeducativoViewSet
)

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

# Registro de endpoints del api
router.register(r'categorias', categoriaViewSet)
router.register(r'respuestas', respuestaforoViewSet)
router.register(r'temas', temaforoViewSet)
router.register(r'videos', videoeducativoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin