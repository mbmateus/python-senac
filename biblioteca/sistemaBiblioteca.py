biblioteca = []


def cadastrar_livros():
    while True:
        print('\nPara cadastrar um livro, deve informar exatamente o conteúdo ao lado!: titulo, autor, ano')
        livro = input('Digite as informações do livro ou sair para parar: ').strip()

        if livro.lower() == 'sair':
            break

        separar_campos = livro.split(',')

        if len(separar_campos) != 3:
            print('As informações estão incorretas, deve conter: titulo, autor, ano')
            continue
        
        titulo = separar_campos[0].strip()
        autor = separar_campos[1].strip()
        ano = separar_campos[2].strip()

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano
        }

        biblioteca.append(livro)
        print('Livro cadastrado com sucesso!')


def listar_livros():
    print('\nLivros cadastrados:')
    if not biblioteca:
        print('Nenhum livro cadastrado!')

    for i, livro in enumerate(biblioteca, start=1):
        print(f"{i} - Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']}")


def buscar_livros_autor():
    nome_autor = input('\nInforme o nome do autor: ').strip().lower()

    livros_encontrados = [livro for livro in biblioteca if livro['autor'].lower() == nome_autor]
    if livros_encontrados:
        print('\nLivro(s) encontrado(s):')
        for i, livro in enumerate(livros_encontrados, start=1):
            print(f"{i} - {livro['titulo']} ({livro['ano']})")
    else:
        print('\nEste autor não possui nenhum livro cadastrado!')


def main():
    while True:
        print('\nMenu:')
        print('1 - Cadastrar livro(s)')
        print('2 - Listar todos os livro(s)')
        print('3 - Buscar livro(s) pelo autor')
        print('4 - Sair')

        opcao = input('\nEscolha uma das opções: ').upper()
        match opcao:
            case '1':
                cadastrar_livros()
            case '2':
                listar_livros()
            case '3':
                buscar_livros_autor()
            case '4':
                print('Saindo...')
                break
            case _:
                print('Opção inválida!')
