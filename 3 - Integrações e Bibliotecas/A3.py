# Passo 0 - Entender o desafio que você quer resolver.

#--------------------------------------------------------------------------------------------------
#Espaço Reservado para importação de bibliotecas---------------------------------------------------
#--------------------------------------------------------------------------------------------------
import pandas as pd  # Para Installar o pandas > pip install pandas        
import matplotlib.pyplot as plt  
import plotly.express as px 
import seaborn as sns
import smtplib
import email.message as em 
from babel.numbers import format_currency
import os

#--------------------------------------------------------------------------------------------------
# Passo 1 - Importar a base de dados (Pasta Vendas) 
#--------------------------------------------------------------------------------------------------

#Criando variavel para armazenar o caminho do arquivo de tb_vendas
file_path = os.path.dirname(__file__) + '/dataSets/vendas.xlsx'

print(f"Iniciando processamento do arquivo <{os.path.basename(file_path)}>")

#Carregando dados do arquivo na varivel tb_vendas 
tb_vendas = pd.read_excel(file_path)


#--------------------------------------------------------------------------------------------------
# Passo 2 - Calcular o produto mais vendido (em quantidade)
#--------------------------------------------------------------------------------------------------

#Agrupamos pro produto e somamos todas as colunas numericas
tb_vendas_produto_quantidade = tb_vendas.groupby('Produto').sum(numeric_only=True)

#Filtramos da tabela apenas a Colunas Index (Produto) e a Coluna Quantidade
tb_vendas_produto_quantidade = tb_vendas_produto_quantidade[['Quantidade']]

#Ordenamos nossa tabela de decrescente pela coluna Quantidade
tb_vendas_produto_quantidade = tb_vendas_produto_quantidade.sort_values(by='Quantidade', ascending=False)

print("Análise de Produtos Vendidos por Unidade Finalizada.")


#--------------------------------------------------------------------------------------------------
# Passo 3 - Calcular o produto mais vendido (em faturamento)
#--------------------------------------------------------------------------------------------------

#Primeiro criamos a coluna Faturamento 
tb_vendas['Faturamento'] = tb_vendas['Quantidade'] * tb_vendas['Valor Unitário']

#Agrupamos pro produto e somamos todas as colunas numericas
tb_vendas_produto_faturamento = tb_vendas.groupby('Produto').sum(numeric_only=True)

#Filtramos da tabela apenas a Colunas Index (Produto) e a Coluna Quantidade
tb_vendas_produto_faturamento = tb_vendas_produto_faturamento[['Faturamento']]

#Ordenamos nossa tabela de decrescente pela coluna Quantidade
tb_vendas_produto_faturamento = tb_vendas_produto_faturamento.sort_values(by='Faturamento', ascending=False)

print("Análise de Produtos Vendidos por Faturamento Finalizada.")


#--------------------------------------------------------------------------------------------------
# Passo 4 - Calcular a loja/estado que mais vendeu (em faturamento)
#--------------------------------------------------------------------------------------------------

#Agrupando dados por Loja
tb_loja_faturamento = tb_vendas.groupby('Loja').sum(numeric_only=True)

#Filtramos as colunas deixando apenas Loja (Index)
tb_loja_faturamento = tb_loja_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print("Análise de Vendas por Loja Finalizada.")

#--------------------------------------------------------------------------------------------------
# Passo 5 - Calcular o ticket médio por loja/estadom. (Somar Valor de cada item e divide pelo total de vendas)
#--------------------------------------------------------------------------------------------------

#Criar a coluna Ticket Medio
tb_vendas['Ticket Médio'] = tb_vendas['Valor Unitário']

#Agrupar por loja e fazer a media de todos os demais 
tb_ticket_medio = tb_vendas.groupby('Loja').mean(numeric_only=True)

#Remove as demais colunas deixando apenas 'Ticket Médio' e Loja (Index)
tb_ticket_medio = tb_ticket_medio[['Ticket Médio']].sort_values(by='Ticket Médio', ascending=False)

print("Análise de Ticket Médio Finalizada.")

#--------------------------------------------------------------------------------------------------
# Passo 6 - Calcular a Quantidade de produtos Vendidos por Loja
#--------------------------------------------------------------------------------------------------

#Agrupando por produto e somando tudo
tb_produto_vendido_loja = tb_vendas.groupby('Loja').sum(numeric_only=True)

#filtrando as colunas a serem exibidas
tb_produto_vendido_loja = tb_produto_vendido_loja[['Quantidade', 'Faturamento']]

#Ordena os dados
tb_produto_vendido_loja = tb_produto_vendido_loja.sort_values(by='Quantidade', ascending=False)

print("Análise de Produtos Vendidos por Loja Finalizada.")


#--------------------------------------------------------------------------------------------------
# Passo 7 - Criar um gráfico/dashboard da loja/estado que mais vendeu (em faturamento) <Resultado do Passo 4>
#--------------------------------------------------------------------------------------------------

#Criando um grafico de barras com ploty
grafico_px = px.bar(tb_loja_faturamento, y='Faturamento', x=tb_loja_faturamento.index)
grafico_px.show()


#Criando Grafico com Matplot

plt.bar(tb_loja_faturamento.index, tb_loja_faturamento['Faturamento'])

plt.title('Faturamento por Lojas')
plt.xlabel('Loja')
plt.ylabel('Faturamento em M')

plt.subplots_adjust(bottom=0.250)  #Coloca mais espaço na margem de baixo da imagem 

plt.xticks(rotation=90)
plt.show()

""""
plt.figure(12,8)

sns.barplot(x=tb_loja_faturamento.index, y='Faturamento', data=tb_loja_faturamento, palette='viridis')

plt.title('Faturamento por Lojas')
plt.xlabel('Loja')
plt.ylabel('Faturamento em M')

plt.tight_layout()

plt.show()

"""

print("Produção de Gráficos Finalizada.")

#--------------------------------------------------------------------------------------------------
#Espaço Reservado para formação do dados-----------------------------------------------------------
#--------------------------------------------------------------------------------------------------

#Cria lambda para formatação de moeda em padrão BRL
lb_formata_real = lambda v: format_currency(v, 'BRL', locale='pt_BR')

#Cria lambda para formatação de valores inteiros
lb_formata_int = lambda x: "{:,}".format(x).replace(',', '.')


#Formatando a tabela vendas produto faturamento
tb_vendas_produto_faturamento_f = pd.DataFrame(tb_vendas_produto_faturamento['Faturamento'].apply(lb_formata_real).reset_index())

print("Formatação de Tabelas Para Envio Finalizada.")

#--------------------------------------------------------------------------------------------------
# Passo 8 - Enviar um e-mail para o setor responsável.  (Enviar Item 2, 3, 4 )
#--------------------------------------------------------------------------------------------------
 
corpo_email = f"""
<p>Prezados, tudo bem?</p>
<p>Segue Analise de Vendas</p>
<p> <b>Produto Mais Vendido (Faturamento)</b>
{tb_vendas_produto_faturamento_f.to_html(index=False, justify='center')}</p>



msg = em.Message()
msg['Subject'] = "Teste em Python" # Assunto do email

msg['From'] = 'rotinabackup58@gmail.com' #Conta de Email que irá enviar   
password = 'fceveunimwskylxg'    #Senha do email que enviará (Senha de app criada) 

msg['To'] = 'servico.backup.status@gmail.com'  #Email destino, quem vai receber   

msg.add_header('Content-Type', 'text/html')

msg.set_payload(corpo_email)

#Faz login do Servidor do gmail e envia o email.
s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()  #Ativa Criptografia TLS
s.login(msg['From'], password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
"""
print('Email Contendo Tabelas Enviado com Sucesso')