from django.urls import path, include
from rest_framework import routers
from .views import CategoriaViewSet #, ProdutoViewwSet, FornecedorViewwSet


router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
#router.register(r'produto', ProdutoViewwSet)
#router.register(r'fornecedor', FornecedorViewwSet)

urlpatterns = [
    path('', include(router.urls)),
]