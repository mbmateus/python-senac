estoque = {
    "Macarrão": (20, 6.99),
    "Arroz": (35, 9.99),
    "Feijão": (15, 8.99),
    "Frango Sadia": (55, 17.99)
}


def produtos_disponiveis():
    print('Produtos disponíveis:')
    for produto, (quantidade, preco) in estoque.items():
        print(f'- {produto}: {quantidade} unidades, R${preco:.2f} a unidade.')


def calcular_valor_total():
    valor_total = 0
    for quantidade, preco in estoque.values():
        valor_total += quantidade * preco
    
    print(f'\nValor total em estoque: R${valor_total:.2f}')
