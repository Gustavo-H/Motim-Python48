# %%
#Nesta aula vamos consumir uma API Node JS que armazena dados de Alunos 

# %%
#Espaco Resevado para imports
import requests
from get_token import token

#Import para tratar arquivos
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes



# %%
base_url = "http://160.238.134.183:3001"

ep_user = "/users/"

ep_token = "/tokens/"

ep_aluno = "/alunos/"

ep_foto = "/fotos"





# %%
#Criando novo usuario na API via Metodo POST
user_data = {    
    "nome": "Gustavo Henrique",
    "password": "py@motim",
    "email": "gustavo2@motim.com"
}

response = requests.post(url=base_url + ep_user, json=user_data)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)

# %%
#Solicitando um token JWT na API via Metodo POST

user_data = {   
    "email": "gustavo.h@motim.com",
    "password": "py@motim"
}

response = requests.post(url=base_url + ep_token, json=user_data)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    print(response.status_code)
    print(response.reason)
    print(response.json())


    response_data = response.json()
    token = response_data['token']

    with open('token.txt', 'w') as file:
        file.write(token)

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)


# %%
#Cria um novo aluno na API via metodo POST

headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "Jose2",
    "sobrenome": "de Jose",
    "email": "jose2@email.com",
    "idade": "80",
    "peso": "100.04",
    "altura": "1.70"
}

#print(headers)

response = requests.post(url=base_url + ep_aluno, json=aluno_data, headers=headers)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)


# %%
#Busca uma aluno na API via metodos GET e passando o ID do aluno como filtro na URL

id_aluno = 3

response = requests.get(url=base_url + ep_aluno + str(id_aluno))

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    #print(response.status_code)
    #print(response.reason)

    response_data = response.json()

    print(response_data)
    print(response_data['nome'])
    print(response_data['email'])    
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)


# %%
#Busca todos os alunos na API via metodos GET 

response = requests.get(url=base_url + ep_aluno)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    #print(response.status_code)
    #print(response.reason)
    #print(response.json())

    for aluno in response.json():
        print(aluno)

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)

# %%
#Atualiza um aluno via metodo PUT passando um ID como parametro na URL 

id_aluno = 2

headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "Luana",
    "sobrenome": "de Paula",
    #"email": "jose@email.com",
    #"idade": "80",
    #"peso": "100.04",
    #"altura": "1.70"

}

response = requests.put(url=base_url + ep_aluno + str(id_aluno), json=aluno_data, headers=headers)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    print(response.status_code)
    print(response.reason)
    print(response.json())

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)

# %%
#Deletar um Aluno via metodo DELETE

id_aluno = 2

headers = {
    'Authorization': token
}

response = requests.delete(url=base_url + ep_aluno + str(id_aluno), json=aluno_data, headers=headers)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    print(response.status_code)
    print(response.reason)
    print(response.json())

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
 

# %%
#Envia uma foto para o aluno via metodo POST

id_aluno = 2

mimeTypes = MimeTypes()

nome_arquivo = 'py-logo.png'

mimeType_arquivo = mimeTypes.guess_type(nome_arquivo)[0]

multipart = MultipartEncoder(fields= {
    'aluno_id': "3",
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimeType_arquivo) 
})

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=base_url + ep_foto, headers=headers, data=multipart)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    print(response.status_code)
    print(response.reason)
    print(response.json())

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)


# %%
#Baixando qualquer arquivo da Web


url = "http://localhost:3001/images/1718931251803_10677.png"

nome_arquivo = url.split('/')[-1]


response = requests.get(url=url)

if( 200 >= response.status_code <= 299):  #Igual a > if(reponse.status_code >= 200 & reponse.status_code <= 299):
    print(response.status_code)
    print(response.reason)
    
    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)






