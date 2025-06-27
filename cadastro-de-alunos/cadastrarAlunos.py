def cadastrar_aluno():
    lista_alunos = []

    while True:
        nome_aluno = input('\nInforme o nome do aluno(a) ou sair: ')
        if nome_aluno.lower() == 'sair':
            break

        lista_notas = []
        for i in range(3):
            lista_notas.append(float(input(f'\nDigite a {i + 1}º nota do(a) {nome_aluno}: ')))

        lista_alunos.append({ 'nome': nome_aluno, 'notas': lista_notas })
    
    print('\nLista de alunos:')
    for i, aluno in enumerate(lista_alunos, start=1):
        print(f"{i} - {aluno['nome']}")
    
    print('\nMédia por aluno:')
    for i, aluno in enumerate(lista_alunos, start=1):
        print(f"{i} - {aluno['nome']} | Média: {calcula_media(aluno['notas']):.2f}")
    
    print(f'\nMédia geral da turma: {calcula_media_geral(lista_alunos):.2f}')


def calcula_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)


def calcula_media_geral(lista_alunos):
    media = 0

    if not lista_alunos:
        return 0
    
    for aluno in lista_alunos:
        media += calcula_media(aluno['notas'])
    return media / len(lista_alunos)

# Crie um programa que cadastre os alunos e suas notas em um dicionário. Cada aluno deve ter um nome (chave) e uma lista de notas (valores). Ao final, exiba:
# - Todos os alunos cadastrados
# - A média de cada aluno
# - A média geral da turma