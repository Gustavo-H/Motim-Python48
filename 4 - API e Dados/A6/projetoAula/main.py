#Aula 6 - 18/06/2024
#Nesta aula aprederemos a conectar no banco de dados 
#Fazer Inser de dados no SQL de partir de arquivos 
#Recuperar estes dados do banco e exibir-los
#Recuperar estes dados e manipular 

from pathlib import Path 
import pandas as pd
#importa minha classe de conexão com o banco para dentro do nosso main
import db_Connection as dbcon

dbc = dbcon.SQLServerConnection()

#Monta o Diretorio dos arquivos 
PATH_ARQUIVOS = Path(__file__).parent.parent / 'arquivos'

#monta o caminho da planilha de produtos
planilha_produto = PATH_ARQUIVOS / 'Produtos.xlsx'

#leio a planilha produtos com o pandas
df_produto = pd.read_excel(planilha_produto)


# `if_exists='replace'` sobrescreve a tabela se ela já existir
# Use `if_exists='append'` para adicionar os dados sem sobrescrever

dbc.insere_data_frame_com_pd(df=df_produto, nome_tabela='TB_PRODUTO', if_exists='replace')




































