import os
import csv
import schedule 
import time 

def job():
    main_folder = r"C:\GIT\Motim\Motim-Python48\5 - Automação\A12"

    dic_dados_csv = [
        {'Nome': 'Alice', 'Idade': 28, 'Cidade': 'São Paulo', 'Profissão': 'Engenheira'},
        {'Nome': 'Bruno', 'Idade': 35, 'Cidade': 'Rio de Janeiro', 'Profissão': 'Advogado'},
        {'Nome': 'Carla', 'Idade': 23, 'Cidade': 'Belo Horizonte', 'Profissão': 'Designer'},
        {'Nome': 'Daniel', 'Idade': 40, 'Cidade': 'Porto Alegre', 'Profissão': 'Médico'},
        {'Nome': 'Eva', 'Idade': 30, 'Cidade': 'Curitiba', 'Profissão': 'Arquiteta'},
        {'Nome': 'Fernando', 'Idade': 45, 'Cidade': 'Salvador', 'Profissão': 'Professor'},
        {'Nome': 'Gabriela', 'Idade': 26, 'Cidade': 'Brasília', 'Profissão': 'Analista'},
        {'Nome': 'Henrique', 'Idade': 32, 'Cidade': 'Fortaleza', 'Profissão': 'Desenvolvedor'},
        {'Nome': 'Isabela', 'Idade': 29, 'Cidade': 'Manaus', 'Profissão': 'Consultora'},
        {'Nome': 'Jorge', 'Idade': 50, 'Cidade': 'Recife', 'Profissão': 'Empresário'}
    ]


    CAMINHO_CSV = os.path.join(main_folder,'csv','csv.csv')


    # Grava uma csv a partir de um dicionario
    with open(CAMINHO_CSV, mode='w', newline='', encoding='utf-8') as arquivo:
        # Nomes das colunas
        colunas = dic_dados_csv[0].keys()
        
        # Criar o writer
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        
        # Escrever o cabeçalho
        escritor.writeheader()
        
        # Escrever os dados
        escritor.writerows(dic_dados_csv)

"""
    # Agendando tarefas com diferentes intervalos e horários
    schedule.every(10).minutes.do(job)                              # Executa a cada 10 minutos
    schedule.every().hour.do(job)                                   # Executa a cada hora
    schedule.every().day.at("10:30").do(job)                        # Executa diariamente às 10:30
    schedule.every().monday.do(job)                                 # Executa toda segunda-feira
    schedule.every().wednesday.at("13:15").do(job)                  # Executa toda quarta-feira às 13:15
    schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)    # Executa diariamente às 12:42 (usando fuso horário Europe/Amsterdam)
    schedule.every().day.at("12:42").do(job)                        # Executa diariamente às 12:42 (usando fuso horário Seu PC)
    schedule.every().minute.at(":17").do(job)                       # Executa' a cada minuto quando o segundo é 17
"""

schedule.every(10).seconds.do(job)

while True: #Loop Continuo
    schedule.run_pending()
    time.sleep(1)





