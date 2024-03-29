from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import  AllowAny
from rest_framework.authentication import SessionAuthentication
from .models import Categoria, Fornecedor, User, Produto, AvaliacaoUser
from . serializers import  CategoriaSerializer, FornecedorSerializer, LoginUserSerializer, UserCriarContaSerializer, ProdutoSerializer,AvaliacaoUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nome': ['icontains']
    }
    pagination_class = PageNumberPagination

class ProdutoViewwSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nome': ['icontains'],
        'categoria': ['exact'],
        'codigo': ['exact']
    }
    pagination_class = PageNumberPagination

class ForncedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nome': ['icontains'],
        'codigo': ['exact']
    }
    pagination_class = PageNumberPagination


class AvaliacaoUserViewSet(viewsets.ModelViewSet):
    queryset = AvaliacaoUser.objects.all()
    serializer_class = AvaliacaoUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nota': ['exact']
    }
    pagination_class = PageNumberPagination

    def get_serializer_context(self):
        return {"produto_id": self.kwargs.get("produto_id")}
    
class createAccountUser(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserCriarContaSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.create(user_data)

            if user:
                return Response(user, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class LoginUserAPIView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    