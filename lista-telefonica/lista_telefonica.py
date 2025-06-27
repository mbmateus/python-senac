agenda = {}


def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print(f"Contato '{nome}' adicionado com sucesso!")


def buscar_contato(nome):
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print(f"Contato '{nome}' não encontrado.")


def lista_contatos():
    if not agenda:
        print('A agenda está vazia.')
    else:
        print('Contatos na agenda:')
        for i, (nome, telefone) in enumerate(agenda.items(), start=1):
            print(f"{i} - {nome}: {telefone}")


def lista_telefonica():
    while True:
        print('\nMenu')
        print('1 - Adicionar contato')
        print('2 - Buscar contato')
        print('3 - Listar contatos')
        print('4 - Sair')
        
        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':
            nome = input('\nNome do contato: ')
            telefone = input('Número do contato: ')
            adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input('\nNome do contato: ')
            buscar_contato(nome)
        elif opcao == '3':
            lista_contatos()
        elif opcao == '4':
            print('Sair')
            break
        else:
            print('Opção inválida, digite novamente.')
