from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . views import *

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()

router.register(r'categorias_ganado', CategoriaGanadoViewSet)
router.register(r'subasta', SubastaViewSet)
router.register(r'tr_preciosubastaganado', TrPreciosubastaganadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]