import requests
from pprint import pprint

def extrair_usuario():
    try:
        url = 'https://jsonplaceholder.typicode.com/users'
        usuarios = []

        response = requests.get(url)
        data = response.json()

        for usuario in data:
            usuarios.append({
                'id': usuario.get('id'),
                'name': usuario.get('name'),
                'email': usuario.get('email'),
                'company': usuario.get('company', {}).get('name')
            })

        pprint(usuarios)
    except Exception as error:
        print(f'Ocorreu um erro: {error}')


def buscar_usuario_id():
    try:
        id = int(input('Digite o id do usuário: '))
        url = f'https://jsonplaceholder.typicode.com/users/{id}'

        response = requests.get(url)
        data = response.json()

        if data:
            # usuario = data (exibe todos os dados do usuário)
            usuario = {
                'name': data.get('name'),
                'email': data.get('email'),
                'company': data.get('company', {}).get('name')
            }
            print(usuario)
        else:
            print('Usuário não encontrado!')
    except Exception as error:
        print(f'Ocorreu um erro: {error}')
        return []


# extrair_usuario()
buscar_usuario_id()
