# Título do projeto - Loja Mercado Bloqueado


# Descrição do projeto
O projeto contempla uma loja virtual, no estilo mercado livre
para venda de mercadorias novas ou usadas pelo site


# Funcionalidades do projeto
O sistema deve gerenciar os usuários e suas mercadorias por meio de anúncios


# Tecnologias utilizadas
O sistema utiliza as seguintes tecnlogias
Linguagem: Python
Framework: Django
Banco de dados: SQLite

# Inicialização
Após o git clone, instalar:
1 - pip install virtualenv
2 - venv\Scripts\activate.bat
3 - django-admin startproject setup . (esse ponto no final é pra não ter subpastas)
4 - python manage.py runserver
5 - pip instal python-dotenv - instalar o recurso para esconder a secret key

secret key
'django-insecure--!6$$n#=ou6&m$rz+gpfrs^yg$*ny(c5400oz)2$yx%-)qrw_u'

iniciar um app
python manage.py startapp galeria

setar lista de templates

comando para conectar os arquivos estaticos
python manage.py collectstatic

comando para conectar o banco de dados (a cada criação de uma tabela no banco de dados 
python manage.py makemigrate 
python manage.py migrate 

criar super usuario
python manage.py createsuperuser 

# Implementaçções futuras

# Colaboradores

# 
