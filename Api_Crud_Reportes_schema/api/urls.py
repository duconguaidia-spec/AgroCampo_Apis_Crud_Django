from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ReporteActividadViewSet
)

router = DefaultRouter()

router.register(r'reportes', ReporteActividadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]