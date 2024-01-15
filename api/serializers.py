from rest_framework import serializers
from .models import Categoria, Produto, Fornecedor, User


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nome', 'descricao']


class ProdutoSerializer(serializers.ModelSerializer):

    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), allow_null=True)

    class Meta:
        model = Produto
        fields = ['id', 'codigo', 'nome', 'preco', 'categoria', 'descricao']    


class FornecedorSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True)
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'codigo', 'produto']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'idade', 'cpf']
