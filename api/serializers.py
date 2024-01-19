from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .models import Carrinho, Categoria, PedidoItem,  Produto, Fornecedor, User, AvaliacaoUser
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

class UserCriarContaSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password_validacao = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['id', "email","username", "nome", "cpf", "celular", "idade", "rua", "numero", "bairro", "complemento","cidade", "estado", "cep" ,"password", "password_validacao", ]

    def validate(self, attrs):
        password = attrs.get('password', '')
        password_validacao = attrs.get('password_validacao', '')

        if password != password_validacao:
            raise serializers.ValidationError("As senhas são diferentes")
        return attrs

def create(self, validated_data):
    user = User.objects.create_user(
        username=validated_data['username'],  
        email=validated_data.get('email'),
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
        model = User 
        fields = ('email', 'password')


    def check_user(self, validated_data):
        user = authenticate(email=validated_data['email'], password=validated_data['password'])

        if not user:
            raise AuthenticationFailed("Credenciais incorretas. Tente novamente")

        return user
        

class AvaliacaoUserSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = AvaliacaoUser
        fields = ['id', 'usuario', 'descricao', 'nota']

    def create(self, validated_data):
        produto_id = self.context.get('produto_id')
        return AvaliacaoUser.objects.create(produto_id= produto_id, **validated_data)
    
class  PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco']

    
class PedidoFinalSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name="subTotal")
    class Meta:
        model = PedidoItem
        fields = ['id', 'carrinho','pedido', 'quantidade', 'sub_total']

    def subTotal(self, pedido: PedidoItem):
        return pedido.quantidade * pedido.produto.preco

class CarrinhoSerializer(serializers.ModelSerializer):
    produtos = PedidoFinalSerializer(many=True)
    total = serializers.SerializerMethodField(method_name="total_pedido")
    class Meta:
        model = Carrinho
        fields =  ['id','produtos', 'total']


    def total_pedido(self, cart: Carrinho):
        items = cart.items.all()
        total = sum([item.quantidade* item.produto.preco for item in items])
        return total
    
