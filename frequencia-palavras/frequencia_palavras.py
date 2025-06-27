def contar_frequencia(frase):
    palavras = frase.split()
    frequencia = {}

    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


def verificar_frequancia_palavras():
    frase = input('Digite uma frase: ')
    resultado = contar_frequencia(frase)

    print('\nFrequência das palavras:')
    for palavra, quantidade in resultado.items():
        print(f"'{palavra}': {quantidade} vez(es)")
