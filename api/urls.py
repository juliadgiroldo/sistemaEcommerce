from django.urls import path, include
from rest_framework import routers
from .views import  CategoriaViewSet, ForncedorViewSet, ProdutoViewwSet, LoginUserAPIView, createAccountUser
from api import views


router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'cadastro', createAccountUser, basename='cadastro')
router.register(r'produto', ProdutoViewwSet)
router.register(r'fornecedor', ForncedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("review/<int:produto_id>/", views.AvaliacaoUserViewSet.as_view({"get": "list", "post": "create"}), name="product-reviews"),
    path('login/', LoginUserAPIView.as_view(), name='login'),
]
