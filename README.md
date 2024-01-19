
# Sistema E-commerce

O sistema trata-se de um Ecommerce onde o usuário pode cadastrar categoria, fornecedores, produtos, registrar-se e fazer login

#Instalação

1. Entre na pasta onde o repositório será clonado

2. Faça o clone do repositório
''' 
git clone https://github.com/juliadgiroldo/sistemaEcommerce.git
'''

3. Entre no diretório sistemaEcommerce

4. Excluir a pasta .venv que foi baixada junto ao repositório

5. Criar um ambiente virtual

'''
python -m venv .venv
'''

6. Entre no ambiente virtual

Se estiver usando powershell
'''
.\.venv\Scripts\activate.ps1
'''
Se estiver usando cmd
'''
.\.venv\Scripts\activate.bat
'''

7. Construa as imagens com docker-compose

'''
docker-compose build
'''

8. Rode o docker-compose em background

'''
docker-compose up -d
'''
9. Faça as migrações 
'''
docker-compose exec python manage.py makemigrations
'''
e depois 
'''
docker-compose exec python manage.py migrate
'''
10. Rode o servidor

'''
docker-compose exec python manage.py runserver
'''
 e acesse o localhost através do link : http://127.0.0.1:8000/


 #Models

 Um produto possui nome, cayegoria, preço, codigo, descrição e fornecedor.
 O fornecedor possui nome e codigo. Um fornecedor fornece vários produtos, mas um produto é fornecido apenas por um fornecedor
 A categoria possui nome e descrição.
 O usuário possui nome, email, username, endereço e celular
 A avaliação do usuário possui nota, usuario, produto e descrição. O produto pode possuir diversas avaliações.
