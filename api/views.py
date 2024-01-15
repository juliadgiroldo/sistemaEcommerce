from rest_framework import viewsets
from .models import Categoria
from . serializers import CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nome': ['icontains']
    }

