import os

import random as rd 
import math
import shutil
import json
import csv
from pathlib import Path
#https://docs.python.org/3/library/pathlib.html


from itertools import count 

#Ser
#Serve para passar comando direto para o terminal do S.O.
# cls serve para limpar o console em mquinas windows
# Linux e MAC usar o comando Clear 
os.system("cls")
#Usar o comando o ech
#os.system('echo "Hello World"')

#os.path() 


path_files =  'G:\Python48-Motim\A5\dataSets'

path_files = os.path.join( os.path.expanduser("~"), 'Desktop')
#caminho_script = os.path.join('')

#cls
# caminho, file = os.path.split(caminho_script)

#os.path.basename retorna o ultimo item de caminho, podendo ser uma pasta ou o nome do arquivo 
#print(os.path.basename(caminho_script))

#Retorma a pasta onde está o arquivo
#print(os.path.dirname(caminho_script))

#Lista todos os itens a partir de um path
#print(os.listdir(caminho_script))
"""
for item in os.listdir(path_files):
    caminho_completo = os.path.join(path_files, item)
    print(item)
    if not os.path.isdir(item):
        continue
    for sub_item in os.path.listdir(caminho_completo):
        print('   ', sub_item)
"""
     


counter = count()

#os.walk usamos para caminhar recursivamente no caminho
"""
for root, dirs, files in os.walk(path_files):
    the_counter = next(counter)
    for dir_ in dirs:
        print('  ', the_counter, 'Dir: ', dir_ )
    for file_ in files:
        caminho_completo = os.path.join(root, file_)        
        print('  ', the_counter, 'File: ', caminho_completo)
        
        #Cuidado isso apagará o arquivo, sem opção de recuperar
        #os.unlink(caminho_completo)        
"""

__file__


#Pausa para ver as clausulas #continue e #break
"""
for i in range(10):
    if(i == 6):
        print("Igual 6")
        continue
    
    if(i == 8):
        print("Igual 8")
        break
        
    print(i)

print("Fim")
"""



def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


#Lista os arquivos de um path e mostra o tamanho de forma formatada

"""
for root, dirs, files in os.walk(path_files):
    the_counter = next(counter)
    for dir_ in dirs:
        print('  ', the_counter, 'Dir: ', dir_ )
    for file_ in files:
        caminho_completo = os.path.join(root, file_) 
        stats = os.stat(caminho_completo)
        size = stats.st_size
               
        print('  ', the_counter, 'File: ', caminho_completo, ' ' , formata_tamanho(size))
        
        #Cuidado isso apagará o arquivo, sem opção de recuperar
        #os.unlink(caminho_completo)        
"""


# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy


"""
HOME = os.path.expanduser("~")
DESKTOP = os.path.join(HOME, 'Desktop')

PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')

NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')



os.makedirs(NOVA_PASTA, exist_ok=True)


for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir)
        
        os.makedirs(caminho_novo_diretorio)
                    
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
        
"""



#Shutil movendo 

# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename


#shutil.copytree(src=PASTA_ORIGINAL, dst=NOVA_PASTA, dirs_exist_ok=True)
#Move um arquivo renomeando
#shutil.move(src=PASTA_ORIGINAL, dst=os.path.join(DESKTOP, 'NOVA_PASTA_2'))

#CUIDADO Remove todos os arquivos de uma diretorio 
###shutil.rmtree(NOVA_PASTA)

#-------------------------------------------------------------------------------------------------
#Usando pathlib
#-------------------------------------------------------------------------------------------------
"""
caminho = Path()

print(caminho.absolute())

#Aqui pega o caminho do meu script
caminho = Path(__file__)

#pasta_teste

#print(caminho)

#Aqui mos pegamos a pasta onde esta o meu arquivo
#print(caminho.parent)

pasta_teste = caminho.parent / 'paste de teste'

#Cria uma pasta 
#pasta_teste.mkdir(exist_ok=True)

#Pega Diretorio Home
home = Path.home()

arquivo_teste = Path.home() / 'Desktop' / 'teste.txt' 

#cria o arquivo no caminhp da variavel path
arquivo_teste.touch()

#remove o arquivo criado
#arquivo_teste.unlink()

with arquivo_teste.open('a+') as file:
    file.write("Ola Mundo \n")
    file.write("Ola Mundo 2\n")
    
print(arquivo_teste.read_text())

"""

#-------------------------------------------------------------------------------------------------
#Abrindo Arquivo Json
#-------------------------------------------------------------------------------------------------

"""
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

from typing import TypedDict

class Movie(TypedDict) :
    title: str
    original_title: str 
    is_movie : bool
    imdb_rating : float
    year : int
    characters : list[str]
    budget : None | float


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''


filme: Movie = json.loads(string_json)


#print(filme["title"])

#print(filme["year"])

#print(filme["year"] + 10)

JSON_FILE_PATH = Path(__file__).parent / 'A5.json'

#

#Escrevendo o conteudo em um json
with open(JSON_FILE_PATH, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)
    
#Lendo de um arquivo json
with open(JSON_FILE_PATH, 'r') as arquivo:
    filme_json: Movie = json.load(arquivo)
    print(filme_json)
 
"""    

#-------------------------------------------------------------------------------------------------
#Lendo Arquivo csv
#-------------------------------------------------------------------------------------------------

#Gravado uma lista

lista_dados_csv =  [
    ['Nome', 'Idade', 'Cidade', 'Profissão'],
    ['Alice', 28, 'São Paulo', 'Engenheira'],
    ['Bruno', 35, 'Rio de Janeiro', 'Advogado'],
    ['Carla', 23, 'Belo Horizonte', 'Designer'],
    ['Daniel', 40, 'Porto Alegre', 'Médico'],
    ['Eva', 30, 'Curitiba', 'Arquiteta'],
    ['Fernando', 45, 'Salvador', 'Professor'],
    ['Gabriela', 26, 'Brasília', 'Analista'],
    ['Henrique', 32, 'Fortaleza', 'Desenvolvedor'],
    ['Isabela', 29, 'Manaus', 'Consultora'],
    ['Jorge', 50, 'Recife', 'Empresário']
]


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


CAMINHO_CSV = Path(__file__).parent / 'A5.csv'


"""
# Grava uma csv a partir de uma lista
with open(CAMINHO_CSV, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
        
    escritor.writerows(lista_dados_csv)
"""
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



#Lendo um csv 
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Cidade'], ['Profissão'])
































    









