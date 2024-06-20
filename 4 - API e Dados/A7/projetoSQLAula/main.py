#Aula 7 - 19/06/2024
#Nesta aula aprederemos a conectar no banco de dados 
#Fazer Inser de dados no SQL de partir de arquivos 
#Recuperar estes dados do banco e exibir-los
#Recuperar estes dados e manipular 

from pathlib import Path 
import pandas as pd
#importa minha classe de conexão com o banco para dentro do nosso main
import db_connection as dbcon

dbc = dbcon.SQLServerConnection()

def executa_carga_tabelas():
    #Monta o Diretorio dos arquivos 
    PATH_ARQUIVOS = Path(__file__).parent.parent / 'arquivos'

    #monta o caminho das planilha de carga
    planilha_produto = PATH_ARQUIVOS / 'Produtos.xlsx'
    planilha_item = PATH_ARQUIVOS / 'Itens.xlsx'
    planilha_ordem = PATH_ARQUIVOS / 'Ordens.xlsx'
    planilha_cliente = PATH_ARQUIVOS / 'Clientes.csv'


    #ler dados dos arquivos em DataFrame do Pandas 
    df_produto = pd.read_excel(planilha_produto)

    df_item = pd.read_excel(planilha_item)

    df_ordem = pd.read_excel(planilha_ordem)

    df_cliente = pd.read_csv(planilha_cliente)



    # `if_exists='replace'` sobrescreve a tabela se ela já existir
    # Use `if_exists='append'` para adicionar os dados sem sobrescrever
    #Insere dados na tebela Produto
    nome_tabela = 'TB_PRODUTO'

    linhas_inseridas = df_produto.to_sql(name=nome_tabela, con=dbcon.engine, if_exists='replace', index=False)
    if linhas_inseridas > 0:
        print(f"{linhas_inseridas} Registros Incluidos na Tabela {nome_tabela}")
    else:
        print("Erro ao Inserir dados na tabela " + nome_tabela)


    #Insere dados da tabela Item
    nome_tabela = 'TB_ITEM'

    linhas_inseridas = df_item.to_sql(nome_tabela, dbcon.engine,  if_exists='replace', index=False)

    if linhas_inseridas > 0:
        print(f"{linhas_inseridas} Registros Incluidos na Tabela {nome_tabela}")
    else:
        print("Erro ao Inserir dados na tabela " + nome_tabela)



    #Insere dados da tabela Ordens
    nome_tabela = 'TB_ORDEM'

    linhas_inseridas = df_ordem.to_sql(nome_tabela, dbcon.engine,  if_exists='replace', index=False)

    if linhas_inseridas > 0:
        print(f"{linhas_inseridas} Registros Incluidos na Tabela {nome_tabela}")
    else:
        print("Erro ao Inserir dados na tabela " + nome_tabela)



    #Insere dados da tabela Ordens
    nome_tabela = 'TB_CLIENTE'
 

    #Exemplo de como tratar valores NaN
    df_cliente['email'] = df_cliente['email'].fillna("Sem Email")


    linhas_inseridas = df_cliente.to_sql(nome_tabela, dbcon.engine,  if_exists='replace', index=False)

    if linhas_inseridas > 0:
        print(f"{linhas_inseridas} Registros Incluidos na Tabela {nome_tabela}")
    else:
        print("Erro ao Inserir dados na tabela " + nome_tabela)



query = "Select * from tb_produto" 


#Busca Dados de uma Query usando nossa classe de conexao com o Banco
"""
dbc.connect()
lista_produto_db = dbc.execute_select_query(query)

for row in lista_produto_db:
    print(row)
"""

#Busca Dados de uma Query usando o Pandas
"""
df_produto_db = pd.read_sql(query, dbcon.engine)
print(df_produto_db)
"""

#Faz Update em registro do banco de dados 
"""
query = "Update TB_PRODUTO Set Preco=010101 Where ID = 0"

dbc.connect()
dbc.execute_update_query(query)


lista_prod_Del = input("Digite o ID do Registro para ser deletado, em mais de um separar por virgula")

query = f"Delete From TB_Produto Where ID in ({lista_prod_Del})"

dbc.connect()
dbc.execute_update_query(query)




#Seleciona todos os clientes do RJ

query = "Select * from tb_cliente where uf = 'Rio de Janeiro'"

dbc.connect()
lista_cliente_rj = dbc.execute_select_query(query)

for row in lista_cliente_rj:
    print(row)
"""


query = """
select top 500
Item.id as IdVenda
,Produro.Nome as Produto
,Categ.Categoria
,Item.preco_total
,Ordem.ds_status
,Ordem.dt_Criacao
,Cliente.nome as NomeCliente
,Cliente.email
,Cliente.telefone as Telefone
,Cliente.uf as Estado
from       TB_ITEM  as Item	
Left Join  TB_ORDEM  as Ordem on Item.Id_Ordem = Ordem.ID
Left join  TB_PRODUTO as Produro on Item.id_produto = Produro.ID
Left join  TB_CATEGORIA as Categ on Produro.ID = Categ.ID
Left join  TB_CLIENTE as Cliente on Ordem.id_cliente = Cliente.ID


order by Ordem.dt_Criacao Desc

"""


df_vendas = pd.read_sql(query, dbcon.engine)

df_vendas.to_excel('top500vendas.xlsx', index=False)










    








































