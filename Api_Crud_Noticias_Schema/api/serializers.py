from rest_framework import serializers

from .models import (
    Noticias,
)

# Serializador para noticias
class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = '__all__'