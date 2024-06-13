# Passo 0 - Entender o desafio que você quer resolver.

#--------------------------------------------------------------------------------------------------
#Espaço Reservado para importação de bibliotecas---------------------------------------------------
#--------------------------------------------------------------------------------------------------
import pandas as pd  # Para Installar o pandas > pip install pandas        
import matplotlib.pyplot as plt  
import plotly.express as px 
import seaborn as sns
import smtplib
from babel.numbers import format_currency
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Instalar pip install -U kaleido

#--------------------------------------------------------------------------------------------------
# Passo 1 - Importar a base de dados (Pasta Vendas) 
#--------------------------------------------------------------------------------------------------

#Criando variavel para armazenar a pasta que está o arquivo .py
script_dir = os.path.dirname(__file__)

#Criando variavel para armazenar o caminho do arquivo de tb_vendas
file_path = script_dir + '/dataSets/vendas.xlsx'


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

#Criando e salvando um grafico de barras do faturamento das lojas usando ploty <Passo 4>
grafico_px = px.bar(tb_loja_faturamento, y='Faturamento', x=tb_loja_faturamento.index)

#grafico_px.show()   #Mostra Dashborad interativo no navegador 

# Caminho completo para salvar o gráfico
grafico_loja_faturamento_path = os.path.join(script_dir, 'FaturamentoLojas.png')

# Definir a resolução desejada (largura e altura em pixels) e a escala
width = 1920
height = 1080
scale = 2

# Salvar o gráfico
grafico_px.write_image(grafico_loja_faturamento_path, width=width, height=height, scale=scale)
#--------------------------------------------------------------------------------------------------


#Criando e salvando um grafico de barras da venda de produtos por unidade usando Matplot <Passo 2>

grafico_vendas_produto_quantidade_path = os.path.join(script_dir, 'ProdutosPorUnidade.png')

plt.bar(tb_vendas_produto_quantidade.index, tb_vendas_produto_quantidade['Quantidade'])

plt.title('Venda de Produtos por Unidade')
plt.xlabel('Produtos')
plt.ylabel('Unidades Vendidas')

plt.subplots_adjust(bottom=0.300)  #Coloca mais espaço na margem de baixo da imagem 

plt.xticks(rotation=90)
#plt.show()  #Exibe Grafico

#Salva o Grafico na pasta 
plt.savefig(grafico_vendas_produto_quantidade_path)
#--------------------------------------------------------------------------------------------------


#Criando e salvando um grafico de barras da venda de produtos por unidade usando Seaborn <Passo 3> 

grafico_vendas_produto_faturamento_path = os.path.join(script_dir, 'ProdutosPorFaturamento.png')

plt.bar(tb_vendas_produto_faturamento.index, tb_vendas_produto_faturamento['Faturamento'])

plt.figure(figsize=(10, 6))  # Define o tamanho da figura

sns.barplot(x=tb_vendas_produto_faturamento.index, y='Faturamento', data=tb_vendas_produto_faturamento, palette='viridis')

plt.title('Venda de Produtos Por Faturamento')
plt.xlabel('Produtos')
plt.ylabel('Faturamento em M')

#Salva o Grafico na pasta 
plt.savefig(grafico_vendas_produto_faturamento_path)


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
 

#TODO Implementar TryCath

email_body = f"""
<!DOCTYPE html>
  <html>
    <body>
      <p>Prezados, tudo bem?</p>
      <p>Segue Analise de Vendas</p>
      <p> <h3>Produto Mais Vendido (Faturamento)</h1>
      {tb_vendas_produto_faturamento_f.to_html(index=False, justify='center')}</p>
    <p>Em Anexo Segue Graficos Gerados</p>
  </body>
</html>
"""

# Configurações do email
email_from = 'rotinabackup58@gmail.com'   
email_to = 'servico.backup.status@gmail.com'
email_subject = 'Analise da Tabela de Vendas'

msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = email_subject

# Anexando o corpo do email
msg.attach(MIMEText(email_body, 'html'))

# Função para anexar arquivos
def anexar_arquivo(msg, file_path):
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file_path)}')
    msg.attach(part)

# Anexando os arquivos
anexar_arquivo(msg, grafico_loja_faturamento_path)
anexar_arquivo(msg, grafico_vendas_produto_faturamento_path)
anexar_arquivo(msg, grafico_vendas_produto_quantidade_path)

# Enviando o email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, 'ccwrprxrwfumnkbl')  # Use uma senha de app do Gmail
    text = msg.as_string()
    server.sendmail(email_from, email_to, text)
    server.quit()
    print('Email Contendo Tabelas Enviado com Sucesso')
except Exception as e:
    print(f'Falha ao enviar email: {e}')
