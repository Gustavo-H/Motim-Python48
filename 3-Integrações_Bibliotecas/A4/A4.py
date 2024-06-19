#PASSO 1 - Importar as bibliotecas necessárias
import os 
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


#PASSO 2 - Percorrer todos os arquivos (planilhas) existentes dentro de uma diretorio

#Obtem o Caminho Absoluto do script
script_path = os.path.abspath(__file__)

#Obtem apenas o diretorio do script
scrip_dir = os.path.dirname(__file__)

#guarda o diretorio de nossas planilhas 
planilhas_dir = os.path.join(scrip_dir, 'dataSets', 'projeto2')

#lista com os nomes de todos os arquivos dentro do diretorio
lista_planilhas = os.listdir(planilhas_dir)


#PASSO 3 - Importar todos os arquivos (planilhas) de vendas e unificá-las numa única tabela (DataFrame) no Pandas

total_vendas = pd.DataFrame()

for planilha in lista_planilhas:
    if('Vendas' in planilha):
        tabela = pd.read_csv(f"{planilhas_dir}/{planilha}")
        total_vendas = pd.concat([total_vendas, tabela])


#PASSO 4 - Importar todos os arquivos (planilhas) de devoluções e unificá-las numa única tabela (DataFrame) no Pandas

total_devolucao = pd.DataFrame()

for planilha in lista_planilhas:
    if('Devolucoes' in planilha):
        tabela = pd.read_csv(f"{planilhas_dir}/{planilha}")
        total_devolucao = pd.concat([total_devolucao, tabela])


### INDICADORES -------------------------------------------------------------------------
#1.0 - QUANTIDADE DE VENDAS LÍQUIDAS:
#Identificar os 3 produtos e as 3 lojas que estão gerando mais vendas.

quantidade_produto_vl = total_vendas[['SKU', 'Produto', 'Quantidade']].groupby(['SKU', 'Produto']).sum()
quantidade_produto_vl = quantidade_produto_vl.sort_values(by='Quantidade', ascending=False)


quantidade_loja_vl = total_vendas[['Loja', 'Quantidade']].groupby(['Loja']).sum()
quantidade_loja_vl = quantidade_loja_vl.sort_values(by='Quantidade', ascending=False)

#print(quantidade_produto_vl)
#print(quantidade_loja_vl.head(3))


#1.1 - QUANTIDADE DE VENDAS BRUTAS:**
#Objetivo:** Identificar os 3 produtos e as 3 lojas que estão gerando mais vendas.

quantidade_produto_vb = pd.DataFrame(pd.concat([total_vendas, total_devolucao]).groupby(['SKU', 'Produto'])['Quantidade'].sum())
quantidade_produto_vb = quantidade_produto_vb.sort_values(by='Quantidade', ascending=False)

#print(quantidade_produto_vb.head(3))


quantidade_loja_vb = pd.DataFrame(pd.concat([total_vendas, total_devolucao]).groupby(['Loja'])['Quantidade'].sum())
#Comentando para testar ordenamento no grafico
#quantidade_loja_vb = quantidade_loja_vb.sort_values(by='Quantidade', ascending=False)

#print(quantidade_loja_vb.head(3))

#1.2 - QUANTIDADE DE DEVOLUÇÕES:**
#Objetivo:** Identificar os 3 produtos e as 3 lojas que estão gerando mais devoluções.
quantidade_produto_dv = total_devolucao[['Produto', 'Quantidade']].groupby(['Produto']).sum()
quantidade_produto_dv = quantidade_produto_dv.sort_values(by='Quantidade', ascending=False)

#print(quantidade_produto_dv.head(10))

quantidade_loja_dv = total_devolucao[['Loja', 'Quantidade']].groupby(['Loja']).sum()
quantidade_loja_dv = quantidade_loja_dv.sort_values(by='Quantidade', ascending=False)

#print(quantidade_loja_dv.head(3))

#2.0 - ANÁLISE DE SAZONALIDADE:**
#Objetivo:** Calcular a variação das vendas dos produtos por mês.

data_formatada = pd.to_datetime(total_vendas['Data'], format='%m/%d/%Y')



#Montar um novo dataFrame usando colunas de dataFrame diferentes 
venda_mensais = pd.DataFrame(
    {
        'Data': data_formatada,
        'Quantidade': total_vendas['Quantidade'] 
    }
)

#resample agrupa por mes ('M')
venda_mensais = venda_mensais.set_index('Data').resample('M').sum()

#Agrupe as data por mes no formato > jan/2023
venda_mensais.index = venda_mensais.index.strftime('%b/%Y')

#Criar um nova coluna variacao

venda_mensais['Varicao'] = venda_mensais['Quantidade'].diff()

print(venda_mensais)

#2.1 - ANÁLISE DE FATURAMENTO TRIMESTRAL:**
#Objetivo:** Calcular o faturamento trimestral do ano.

faturamento_trimestral = pd.DataFrame(
    {
        'Data': data_formatada,
        'Quantidade' : total_vendas['Quantidade'], 
        'Valor Unitário' : total_vendas['Valor Unitário'],
        'Faturamento' : total_vendas['Quantidade'] * total_vendas['Valor Unitário'] 
    }
)

#Exemplos de Valores Possiveis:
# 'D' para dias
# 'M' para mes
# 'Y' para anos
# 'Q' para trimestres  > 'Quarter'
# 'W' para semanas

faturamento_trimestral['Trimestre'] = faturamento_trimestral['Data'].dt.to_period("Q")
faturamento_trimestral = pd.DataFrame(faturamento_trimestral.groupby('Trimestre').sum(numeric_only=True))

#print(faturamento_trimestral)


#Graficos

#Fazendo um grafico pizza/torta com ploty 
#Exibe Quantidade de Vendas Liquidas por Produto

grafico1 = px.pie(quantidade_produto_vl.reset_index(),
                  names='Produto', values='Quantidade',
                  title='Quantidade de Vendas Liquidas por Produto')

grafico1.update_traces(textposition='inside', textinfo='label+percent')
#grafico1.show()

#Fazendo um grafico de barras com ploty

#Fizemos um grafico com ploty que exibe Vendas Liquidas por Loja dando cores pela quantidade
grafico2 = px.bar(quantidade_loja_vl.reset_index(), 
                  x='Loja', 
                  y='Quantidade', 
                  title='Vendas Liquidas por Loja',
                  color='Quantidade')
#Fizemos um grafico com ploty que exibe Vendas Liquidas por Loja dando cores pela loja
grafico2 = px.bar(quantidade_loja_vl.reset_index(), 
                  x='Loja', 
                  y='Quantidade', 
                  title='Vendas Liquidas por Loja',
                  color='Loja')

#grafico2.show()

#Fizemos um grafico de barras que mostra Vendas Brutas por Produto dando cores pelo Produto
grafico3 = px.bar( quantidade_produto_vb.reset_index(),
                  x='Produto', 
                  y='Quantidade',
                  title='Vendas Brutas por Produto',
                  color='Produto')

#grafico3.show()

grafico4 = px.bar(
    quantidade_loja_vb.reset_index(),
    x='Loja',
    y='Quantidade',
    title='Vendas Brutas por Loja',
    color='Loja')

grafico4.update_xaxes(categoryorder='total descending')

#grafico4.show()


#Cria um grafico de barras com Seaborn com "Quantidade de Devoluções por Produto e por Loja"

quantidade_produto_dv_grafico = pd.DataFrame(
    {
        'Categoria': quantidade_produto_dv.index,
        'Quantidade' : quantidade_produto_dv['Quantidade'],
        'Tipo': ['Produto'] * len(quantidade_produto_dv)
    }
)


quantidade_loja_dv_grafico = pd.DataFrame(
    {
        'Categoria': quantidade_loja_dv.index,
        'Quantidade' : quantidade_loja_dv['Quantidade'],
        'Tipo': ['Loja'] * len(quantidade_loja_dv)
    }
)

#print(quantidade_produto_dv_grafico)

#print(quantidade_loja_dv_grafico)


cores = {'Produto': 'green', 'Loja': 'yellow'}

df_grafico_concatenado = pd.concat([quantidade_loja_dv_grafico, quantidade_produto_dv_grafico])

grafico5 = sns.barplot(data=df_grafico_concatenado, x='Quantidade', y='Categoria', hue='Tipo', orient='h', palette=cores)
grafico5.set_title("Quantidade de Devoluções por Produto e por Loja")
#plt.show()


# Para treinar em casa enviar os grafico gerados por email
# Tambem pode enviar as tabelas que voce quiser 
# e se quiser fazer os grafico de sazonalidae  


#Construindo um grafico de sazonalidade usando grafico de linha do ploty 

#array com nomes das cores para cada mes vermelho negativo; azul positivo 
text_color = np.where(venda_mensais['Varicao'] < 0, 'red', 'blue')

#print(text_color)

#Gerando o grafico 
grafico6 = px.line(venda_mensais.reset_index(),
                   x='Data',
                   y='Quantidade',
                   title='Vendas Mensais',
                   markers=True,
                   text=venda_mensais['Quantidade'])

#update no grafico para colocar valores de cor
grafico6.update_traces(textposition='top center',
                       textfont=dict( color=text_color, size=15),
                       marker=dict(color=text_color))

#grafico6.show() 








