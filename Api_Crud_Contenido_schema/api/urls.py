from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    categoriaViewSet,
    respuestaForoViewSet,
    temaForoViewSet,
    videoEducativoViewSet
)

router = DefaultRouter()

router.register(r'categorias', categoriaViewSet)
router.register(r'respuestas', respuestaForoViewSet)
router.register(r'temas', temaForoViewSet)
router.register(r'videos', videoEducativoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]