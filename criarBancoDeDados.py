import pymysql

# Conecte-se ao servidor MySQL
conexao = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Maximo123',
    database='api_flask'  # Substitua pelo nome do banco de dados que você quer usar
)

try:
    # Crie um cursor para interagir com o banco de dados
    cursor = conexao.cursor()

    # SQL para criar a tabela
    criar_tabela_sql = """
    CREATE TABLE curso (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        descricao VARCHAR(100) NOT NULL,
        data_publicacao DATE NOT NULL
    );
    """

    # Execute o comando SQL
    cursor.execute(criar_tabela_sql)

    # Confirme a transação
    conexao.commit()

    print('Tabela criada com sucesso!')

except Exception as e:
    print(f'Ocorreu um erro: {e}')
    # Reverter se algo deu errado
    conexao.rollback()

finally:
    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()
