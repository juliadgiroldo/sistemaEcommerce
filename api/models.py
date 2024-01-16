from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import RegexValidator
from api.managers import GerirUsuario

ESTADOS = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

class User(AbstractUser, PermissionsMixin):
    nome = models.CharField(max_length=180)
    password = models.CharField(max_length=255)
    password_validacao = models.CharField(max_length=255)
    email= models.CharField(max_length=256,
                            unique=True,
                            validators=[
                                RegexValidator(
                                    regex = r'^[A-Za-z0-9_!#$%&\'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$',
                                    message="Email invalido",
                                    code='email_invalido'
                                )
                            ])
    idade = models.IntegerField(default=0)
    celular = models.CharField(max_length=15,
                               validators=[
                                   RegexValidator(
                                       regex=r'^\(\d{2}\)9\d{4}\d{4}$',
                                       message='Numero de celular invalido',
                                       code= 'celular_invalido'
                                   )
                               ])
    cpf = models.CharField(max_length=14, unique=True,
                           validators=[
                               RegexValidator(
                                   regex=r'^\d{3}\d{3}\d{3}\d{2}$',
                                   message='CPF inválido',
                                   code='cpf_invalido'
                               )
                           ])
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=5, 
                            validators=[
                                RegexValidator(
                                    regex=r'^\d{1,5}$',
                                    message='Numero invalido',
                                    code  = 'numero_invalido'
                                )
                            ])
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(choices=ESTADOS, max_length=2)
    cep = models.CharField(max_length=100,
                          validators=[
                              RegexValidator(
                                  regex=r'^\d{5}(-\d{3})?$',
                                  message='CEP invalido',
                                  code='cep_invalido'
                              )
                          ])

    staff = models.BooleanField(default=False)
    superUser = models.BooleanField(default=False)


    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [ "nome", "cpf"]

    objects = GerirUsuario()

    def __str__(self):
        return self.nome
    
    @property

    def token(self):
        
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    


class Categoria(models.Model):
    nome = models.CharField(max_length=180)
    descricao = models.CharField(max_length=280)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=180)

    def __str__(self):
        return self.codigo

class Estoque(models.Model):
    quantidade = models.IntegerField()
    quantidade_min = models.IntegerField()

class Produto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=180)
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=None)
    descricao = models.CharField(max_length=280)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.nome
    

class PedidoItem(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    cpf_user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def total_pedido_item(self):
        total_item = self.quantidade * self.produto.preco
        return total_item
    
class Carrinho(models.Model):
    produtos = models.ManyToManyField(PedidoItem)
    cpf_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def calcular_total(self):
        total_pedido = sum(item.total_pedido_item() for item in self.produtos.all())
        return total_pedido
    
class AvaliacaoUser(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=300)
    nota = models.IntegerField()
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)