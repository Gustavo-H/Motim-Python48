import pandas as pd  # Para Installar o pandas > pip install pandas        
import matplotlib.pyplot as plt  
import plotly.express as px 
import seaborn as sns
import smtplib
import os
from babel.numbers import format_currency
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



#Criando variavel para armazenar a pasta que está o arquivo .py
script_dir = os.path.dirname(__file__)


print(script_dir)

#Criando variavel para armazenar o caminho do arquivo de tb_vendas
file_path = script_dir + 'projeto1/dataSets/vendas.xlsx'


print(f"Iniciando processamento do arquivo <{os.path.basename(file_path)}>")
