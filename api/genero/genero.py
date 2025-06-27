import requests

def consultar_genero():
    nome = input('Digite um nome: ')

    if not nome:
        print('Campo nome é obrigatório!')
        return
    
    url = f'https://api.genderize.io/?name={nome}'

    try:
        response = requests.get(url)
        
        data = response.json()
        genero = data.get('gender')
        probabilidade = data.get('probability')

        if genero:
                print(f'{nome} tem o seguinte gênero estimado: {genero}')
                print(f'Probabilidade: {float(probabilidade) * 100:.2f}%')
        else:
             print(f'Não foi possível estimar o gênero para {nome}.')
    except requests.exceptions.RequestException as error:
         print('Erro interno:', error)

consultar_genero()
