from django.urls import path, include
from rest_framework import routers
from .views import CategoriaViewSet, ForncedorViewSet, ProdutoViewwSet,LoginUserViewSet, createAccountUser, AvaliacaoUserViewSet #, ProdutoViewwSet, FornecedorViewwSet


router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'user_cadastro', createAccountUser, basename='cadastro')
router.register(r'login', LoginUserViewSet, basename='login')
router.register(r'produto', ProdutoViewwSet)
router.register(r'fornecedor', ForncedorViewSet)
router.register(r'avaliacao_produto/(?P<produto_pk>[^/.]+)/$', AvaliacaoUserViewSet, basename='avaliacao_produto')


urlpatterns = [
    path('', include(router.urls)),
    #path('login/', LoginUserViewSet.as_view({'post': 'login'}), name='user-login'),
]