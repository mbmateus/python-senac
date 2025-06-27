estoque_produtos = []

def cadastrar_produtos():
    while True:
        print('\nPara cadastrar um produto, deve informar exatamente o conteúdo ao lado: nome, quantidade, preço unitário')
        produto = input('Digite as informações do produto ou sair: ').strip()

        if produto.lower() == 'sair':
            break
        
        separar_campos = produto.split(', ')

        if len(separar_campos) != 3:
            print('As informações estão incorretas, deve conter: nome, quantidade, preço unitário')
            continue

        name = separar_campos[0].strip()
        amount = separar_campos[1].strip()
        unit_price = separar_campos[2].strip()

        produto = {
            'name': name,
            'amount': int(amount),
            'unit_price': float(unit_price)
        }

        estoque_produtos.append(produto)
        print('Produto cadastrado com sucesso!')


def lista_produtos():
    print('\nProdutos:')
    if not estoque_produtos:
        print('\nNenhum produto cadastrado!')

    for i, produto in enumerate(estoque_produtos, start=1):
        valor_total = produto['amount'] * produto['unit_price']
        print(f"{i} - Nome: {produto['name']} | Quantidade: {produto['amount']} | Preço Unitário: {produto['unit_price']:.2f} | Total: R${valor_total:.2f}")


def atualizar_produto():
    try:
        index = int(input('Informe o índice do produto que deseja atualizar: ')) - 1
        if index < 0 or index >= len(estoque_produtos):
            print('Índice inválido!')
            return
    except ValueError:
        print('Por favor, informe um número inteiro válido para o índice.')
        return
    
    print('\nPara atualizar um produto, deve informar exatamente o conteúdo ao lado: nome, quantidade, preço unitário')
    produto = input('Digite o nome, quantidade e preço unitário separados por vírgula: ').strip()

    separar_campos = produto.split(', ')

    if len(separar_campos) != 3:
        print('As informações estão incorretas, deve conter: nome, quantidade, preço unitário')
        return

    name = separar_campos[0].strip()
    amount = separar_campos[1].strip()
    unit_price = separar_campos[2].strip()

    try:
        amount = int(amount)
        unit_price = float(unit_price)
    except ValueError:
        print('Quantidade deve ser um número inteiro e preço unitário um número decimal.')
        return

    produto_atualizado = {
        'name': name,
        'amount': amount,
        'unit_price': unit_price
    }

    estoque_produtos[index] = produto_atualizado

    print(f"\nProduto {produto_atualizado['name']} atualizado com sucesso!")


def remover_produto():
    try:
        index = int(input('Informe o índice do produto que deseja remover: ')) - 1
        if index < 0 or index >= len(estoque_produtos):
            print('Índice inválido.')
            return
    except ValueError:
        print('Por favor, informe um número inteiro válido para o índice.')
        return
    
    produto_removido = estoque_produtos.pop(index)
    print(f"Produto {produto_removido['name']} foi removido com sucesso!")


def calcular_valor_total_estoque():
    valor_total = 0
    for produto in estoque_produtos:
        valor_total += produto['amount'] * produto['unit_price']
    
    print(f'Valor total em estoque: R${valor_total:.2f}')


def main():
    while True:
        print('\nMenu:')
        print('1 - Cadastrar produto')
        print('2 - Listar todos os produtos')
        print('3 - Atualizar informações do produto')
        print('4 - Remover um produto')
        print('5 - Calcular e mostrar valor total em estoque')
        print('6 - Sair')

        opcao = input('\nInforme uma das opções acima: ').lower()

        match opcao:
            case '1':
                cadastrar_produtos()
            case '2':
                lista_produtos()
            case '3':
                atualizar_produto()
            case '4':
                remover_produto()
            case '5':
                calcular_valor_total_estoque()
            case '6':
                print('Encerrando sistema...')
                break
            case _:
                print('Opção inválida!')


main()


# """
# Cadastrar produto (nome, quantidade, preço unitário);
# Listar produtos;
# Atualizar quantidade ou preço de um produto;
# Remover produto pelo nome;
# Calcular e mostrar o valor total do estoque (quantidade * preço de todos os produtos).
# """
