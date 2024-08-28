import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

#Aqui realizamos a configuração do nossa API com nosso banco de dados
DEBUG = True #Permite que qualquer alteração não precisa reinicar o banco de dados

#passando as configurações para acessar nosso banco de dados
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SERVER = os.getenv('SERVER')
DB = os.getenv('DB')

#Acessando nosso banco de dados
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
#Salvar nossas alterações do banco de dados
SQLALCHEMY_TRACK_MODIFICATIONS = True