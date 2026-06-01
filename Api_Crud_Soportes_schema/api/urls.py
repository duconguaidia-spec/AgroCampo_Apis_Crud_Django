from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    categoriapreguntasViewSet,
    preguntafrecuenteViewSet
)

router = DefaultRouter()

router.register(r'categorias', categoriapreguntasViewSet)
router.register(r'preguntasfrecuentes', preguntafrecuenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]