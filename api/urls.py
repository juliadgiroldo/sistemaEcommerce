from django.urls import path, include
from rest_framework import routers
from .views import CarrinhoViewSet, CategoriaViewSet, ForncedorViewSet, PedidioFinalViewSet, ProdutoViewwSet, LoginUserViewSet, createAccountUser, AvaliacaoUserViewSet
from api import views

router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'user_cadastro', createAccountUser, basename='cadastro')
router.register(r'login', LoginUserViewSet, basename='login')
router.register(r'produto', ProdutoViewwSet)
router.register(r'fornecedor', ForncedorViewSet)
router.register(r'carrinho', CarrinhoViewSet)
router.register(r'pedido', PedidioFinalViewSet)
#router.register(r'avaliacao_produto', AvaliacaoUserViewSet, basename='avaliacao_produto')


urlpatterns = [
    path('', include(router.urls)),
    path("review/<int:produto_id>/", views.AvaliacaoUserViewSet.as_view({"get": "list", "post": "create"}), name="product-reviews"),

]



