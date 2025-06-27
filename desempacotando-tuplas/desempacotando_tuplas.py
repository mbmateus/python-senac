def calcular_total(lista_itens):
    total = 0

    print('Itens comprados:')
    for nome, quantidade, preco in lista_itens:
        subtotal = quantidade * preco
        print(f'- {quantidade}x {nome} = R${subtotal:.2f}')
        total += subtotal

    return total


def calcular_total_gasto():
    compras = [
        ("Arroz", 2, 11.50),
        ("Feijão", 1, 9.20),
        ("Macarrão", 3, 6.50),
        ("Banana", 1, 6.99)
    ]

    total_gasto = calcular_total(compras)

    print(f"\nTotal gasto: R${total_gasto:.2f}")
