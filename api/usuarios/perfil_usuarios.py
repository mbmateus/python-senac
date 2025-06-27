import requests

# Dicionario com nome como chave e outro dicionário com cidade e empresa como valor

usuarios = requests.get('https://jsonplaceholder.typicode.com/users').json()

nomes = {}
info_user = {}
# print(f"Nome: {usuarios[0]['name']}")
# print(f"Cidade: {usuarios[0]['address']['city']}")
# print(f"Empresa: {usuarios[0]['company']['name']}")
for user in usuarios:
    nome = user['name']
    nomes[nome] = {
        'Cidade:': user['address']['city'],
        'Empresa:': user['company']['name']
    }

print(nomes)
