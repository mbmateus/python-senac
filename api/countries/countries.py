import requests

sigla = input('Digite a sigla do país (BR, US): ').upper()
url = f'https://restcountries.com/v3.1/alpha/{sigla}'


def consultar_pais_sigla():
    response = requests.get(url).json()

    for pais in response:
        nome_pais = pais['name']['common']
        capitais = ', '.join(pais['capital'])
        populacao = pais['population']
        print(f"País: {nome_pais}")
        print(f"Capital: {capitais}")
        print(f"População: {populacao}")
        fronteiras = pais['borders']
        print(f"Fronteira(s): {', '.join(fronteiras)}")
        consultar_fronteira(fronteiras)


def consultar_fronteira(fronteiras):
    for p in fronteiras:
        response = requests.get(f'https://restcountries.com/v3.1/alpha/{p}').json()
        for i in response:
            nome_pais = i['name']['common']
            capitais = ', '.join(i['capital'])
            populacao = i['population']
            print('\n')
            print(f"País: {nome_pais}")
            print(f"Capital: {capitais}")
            print(f"População: {populacao}")


consultar_pais_sigla()
