# Relacionar nome do usuário com número de posts Objetivo:
# Trabalhar com duas APIs e cruzar dados.
# Crie um dicionário com nome do usuário como chave e quantidade de posts como valor
import requests 

usuarios = requests.get("https://jsonplaceholder.typicode.com/users").json()
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()

qtd_posts = {}
pegar_usuarios = {}
for post in posts:
    if post['userId']:
        user_id = post['userId']
        qtd_posts[user_id] = qtd_posts.get(user_id, 0) + 1

    for usuario in usuarios:
        if usuario['id']:
            nome = usuario['name']
            pegar_usuarios[nome] = qtd_posts.get(user_id)
print(pegar_usuarios)

# Atividade Diego, exibir o userId como chave e como valor uma lista com os títulos de posts separados por usuário
titulos = {}
lista_titulos = []

for titulo in posts:
    if titulo['userId']:
        user_id = titulo['userId']
        title = titulo['title']
        titulos[user_id] = titulos.get(user_id, lista_titulos) + [title]

print(titulos)
