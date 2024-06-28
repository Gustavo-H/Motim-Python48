# %%
#Espaco para imports
import requests #Pip install requests ou no codigo > !Pip install requests


# %%
#Cria varivel com a URL da API
base_url = "https://jsonplaceholder.typicode.com"

# %%
# Função para obter todos os posts
def get_posts():
    response = requests.get(f"{base_url}/posts")
    if 200 >= response.status_code < 299:  #Esta forma de usar o if funciona igual a > response.status_code >= 200 & response.status_code <= 299
        return response.json()
    else:
        print(f"Erro ao obter posts: {response.status_code}")
        return None


# %%
# Função para obter um post por ID
def get_post(post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    if 200 >= response.status_code < 299:  #Esta forma de usar o if funciona igual a > response.status_code >= 200 & response.status_code <= 299
        return response.json()
    else:
        print(f"Erro ao obter o post: {response.status_code}")
        return None


# %%
# Função para criar um novo post
def create_post(title, body, user_id):
    new_post = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(f"{base_url}/posts", json=new_post)
    if response.status_code == 201:  #201 status para created
        return response.json()
    else:
        print(f"Erro ao criar o post: {response.status_code}")
        return None

# %%
# Função para atualizar um post existente
def update_post(post_id, title, body, user_id):
    updated_post = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.put(f"{base_url}/posts/{post_id}", json=updated_post)
    if 200 >= response.status_code < 299:  #Esta forma de usar o if funciona igual a => response.status_code >= 200 & response.status_code <= 299
        return response.json()
    else:
        print(f"Erro ao atualizar o post: {response.status_code}")
        return None

# %%
# Função para deletar um post por ID
def delete_post(post_id):
    response = requests.delete(f"{base_url}/posts/{post_id}")
    if response.status_code == 200:
        return True
    else:
        print(f"Erro ao deletar o post: {response.status_code}")
        return False


# %%
# Obter todos os posts
posts = get_posts()
if posts:
    print("Posts obtidos:")
    for post in posts[:5]:  # Imprime apenas os 5 primeiros posts
        print(post)
    

# %%
# Obter um post específico
post_id = 1
post = get_post(post_id)
if post:
    print(f"\nPost {post_id} obtido:")
    print(post)


# %%
# Criar um novo post
new_post = create_post("Novo Post", "Este é o conteúdo do novo post", 1)
if new_post:
    print("\nNovo post criado:")
    print(new_post)
   

# %%
# Atualizar um post existente
updated_post = update_post(1, "Post Atualizado", "Este é o conteúdo atualizado do post", 1)
if updated_post:
    print("\nPost atualizado:")
    print(updated_post)

# %%
# Deletar um post
if delete_post(1):
    print("\nPost deletado com sucesso.")


