from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .models import Categoria,  Produto, Fornecedor, User, AvaliacaoUser
from rest_framework.exceptions import AuthenticationFailed

UserModel = get_user_model()

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nome', 'descricao']



class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'codigo']


class ProdutoSerializer(serializers.ModelSerializer):

    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), allow_null=True)
    fornecedor = serializers.CharField(source='fornecedor.id')

    class Meta:
        model = Produto
        fields = ['id', 'codigo', 'nome', 'preco', 'categoria', 'descricao', 'fornecedor']

class UserCRiarContaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password_validacao = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['id', "email", "nome", "cpf", "celular", "idade", "rua", "numero", "bairro", "complemento","cidade", "estado", "cep" ,"password", "password_validacao", ]

    def validate(self, attrs):
        password = attrs.get('password', '')
        password_validacao = attrs.get('password_validacao', '')

        if password != password_validacao:
            raise serializers.ValidationError("As senhas são diferentes")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            nome=validated_data.get('nome'),
            cpf=validated_data.get('cpf'),
            celular=validated_data.get('celular'),
            password=validated_data.get('password')
        )

        return user

class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=256, min_length=6)
    password = serializers.CharField(max_length=255, min_length=6)

    class Meta:
        model = UserModel 
        fields = ('email', 'password')


    def check_user(self, validated_data):
        user = authenticate(email=validated_data['email'], password=validated_data['password'])

        if not user:
            raise AuthenticationFailed("Credenciais incorretas. Tente novamente")

        return user
        

class AvaliacaoUserSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='user.id')

    class Meta:
        model = AvaliacaoUser
        fields = ['id', 'usuario', 'descricao', 'nota']

    def create(self, validated_data):
        produto_id = self.context.get('produto_id')
        return AvaliacaoUser.objects.create(produto_id=produto_id, **validated_data)