import requests

def consultar_cep():
    cep = input('Digite seu CEP: ')

    if not cep.isdigit() or len(cep) != 8:
        print('CEP inválido, tente novamente!')
        return

    url = f'https://brasilapi.com.br/api/cep/v2/{cep}'


    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"CEP: {data.get('cep', 'Não informado')}")
            print(f"Rua: {data.get('street', 'Não informado')}")
            print(f"Bairro: {data.get('neighborhood', 'Não informado')}")
            print(f"Cidade: {data.get('city', 'Não informado')}")
            print(f"Estado: {data.get('state', 'Não informado')}")
        elif response.status_code == 404:
            print('CEP não encontrado!')
        else:
            print(f'Erro inesperado: {response.status_code}')
    except requests.exceptions.RequestException as error:
        print(f'Erro interno: {error}')

consultar_cep()
