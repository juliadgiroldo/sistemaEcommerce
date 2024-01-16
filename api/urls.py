from django.urls import path, include
from rest_framework import routers
from .views import CategoriaViewSet, ForncedorViewSet, ProdutoViewwSet, LoginUserViewSet, createAccountUser, AvaliacaoUserViewSet
from api import views

router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'user_cadastro', createAccountUser, basename='cadastro')
router.register(r'login', LoginUserViewSet, basename='login')
router.register(r'produto', ProdutoViewwSet)
router.register(r'fornecedor', ForncedorViewSet)
router.register(r'avaliacao_produto', AvaliacaoUserViewSet, basename='avaliacao_produto')


urlpatterns = [
    path('', include(router.urls)),
    # path('login/', LoginUserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('avaliacao_produto/<int:product_pk>/', views.AvaliacaoUserViewSet.as_view({'get': 'list'}), name='product-reviews'),
]

# Note: The router.urls should not be included again, as they are already included in the 'include(router.urls)' above.
