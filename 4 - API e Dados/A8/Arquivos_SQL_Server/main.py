# %% [markdown]
# ### Neste arquivo veremos como inserir e recuperar arquivos no SQL Server 
# 

# %%
import pyodbc
import db_connection as dbcon
import os

# %%
#Cria Query que cria tabela 
create_table_sql = """
    DROP TABLE IF EXISTS TB_ARQUIVOS

    CREATE TABLE TB_ARQUIVOS (
    Id INT PRIMARY KEY IDENTITY(1,1),
    NomeArquivo NVARCHAR(255) NOT NULL,
    ConteudoArquivo VARBINARY(MAX) NOT NULL
)
"""


# %%
#Instacia nossa classe de conexão
sql_con = dbcon.SQLServerConnection()
sql_con.connect()
cursor = sql_con.connection.cursor()

# %%
#executa query no banco de dados
cursor.execute(create_table_sql)
cursor.commit()

cursor.close()
sql_con.disconnect()

# %%
#Cria variaveis de path das pastas
arquivos_to_sql = './arquivos_to_sql/'

arquivos_from_sql = './arquivos_from_sql/'

# %%
# Função para abrir arquivos e devolver o conteudo em Byte
def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

# %%
#Pega cada arquivos da pasta e insere no banco de dados

sql_con.connect()
cursor = sql_con.connection.cursor()

for file_name in os.listdir(arquivos_to_sql):
    file_path = os.path.join(arquivos_to_sql, file_name)
    file_content = read_file(file_path)

    query_insert = """
    INSERT INTO TB_ARQUIVOS (NomeArquivo, ConteudoArquivo)
    VALUES(?,?)    
    """

    cursor.execute(query_insert, (file_name, file_content))

#Confirma os inserts
cursor.commit()


#Fecha conexão
cursor.close()
sql_con.disconnect()

# %%
sql_con.connect()
cursor = sql_con.connection.cursor()

query = "SELECT NomeArquivo, ConteudoArquivo FROM TB_ARQUIVOS"

cursor.execute(query)

for row in cursor.fetchall():
    file_name = row.NomeArquivo
    file_content = row.ConteudoArquivo

    #print(file_name)
    #print(file_content)

    with open(os.path.join(arquivos_from_sql, file_name), 'wb') as file:
        file.write(file_content)


#Fecha conexão
cursor.close()
sql_con.disconnect()


