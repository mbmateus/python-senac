estoque_veiculos = []

def cadastrar_veiculos():
    while True:
        print('\nPara cadastrar um veiculo, deve ser informado: marca, modelo, ano, preco')
        veiculo = input('Digite as informações do veículo ou sair: ').strip()

        if veiculo.lower() == 'sair':
            break

        separar_campos = veiculo.split(', ')

        if len(separar_campos) != 4:
            print('As informações estão incorretas, deve conter: marca, modelo, ano, preco')
            continue

        marca = separar_campos[0].strip()
        modelo = separar_campos[1].strip()
        ano = separar_campos[2].strip()
        preco = separar_campos[3].strip()

        veiculo_cadastrado = {
            'marca': marca,
            'modelo': modelo,
            'ano': int(ano),
            'preco': float(preco)
        }

        estoque_veiculos.append(veiculo_cadastrado)
        print(f"Veículo {veiculo_cadastrado['modelo']} cadastrado com sucesso!")


def lista_veiculos():
    print('\n Lista de Veículos:')
    if not estoque_veiculos:
        print('\nNenhum veículo cadastrado!')

    for i, veiculo in enumerate(estoque_veiculos, start=1):
        print(f"{i} - Marca: {veiculo['marca']} | Modelo: {veiculo['modelo']} | Ano: {veiculo['ano']} | Preço: R${veiculo['preco']:.3f}")


def atualizar_veiculo():
    try:
        index = int(input('Informe o índice do veículo que deseja atualizar: ')) - 1
        if index < 0 or index >= len(estoque_veiculos):
            print('Índice inválido!')
            return
    except ValueError:
        print('Por favor, informe um número inteiro válido para o índice.')
        return
    
    print('\nPara atualizar um veículo, deve informar exatamente o conteúdo ao lado: marca, modelo, ano, preco')
    veiculo = input('Digite a marca, modelo, ano, preco separados por vírgula: ').strip()

    separar_campos = veiculo.split(', ')

    if len(separar_campos) != 4:
        print('As informações estão incorretas, deve conter: marca, modelo, ano, preco')
        return

    marca = separar_campos[0].strip()
    modelo = separar_campos[1].strip()
    ano = separar_campos[2].strip()
    preco = separar_campos[3].strip()

    veiculo_atualizado = {
        'marca': marca,
        'modelo': modelo,
        'ano': int(ano),
        'preco': float(preco)
    }

    estoque_veiculos[index] = veiculo_atualizado

    print(f"\nVeículo {veiculo_atualizado['modelo']} atualizado com sucesso!")

def deletar_veiculo():
    try:
        index = int(input('Informe o índice do veículo que deseja remover: ')) - 1
        if index < 0 or index >= len(estoque_veiculos):
            print('Índice inválido.')
            return
    except ValueError:
        print('Por favor, informe um número inteiro válido para o índice.')
        return
    
    veiculo_removido = estoque_veiculos.pop(index)
    print(f"Veículo {veiculo_removido['modelo']} foi removido com sucesso!")


def main():
    while True:
        print('\nMenu:')
        print('1 - Cadastrar veículo')
        print('2 - Listar todos os veículos')
        print('3 - Atualizar informações do veículo')
        print('4 - Remover um veículo')
        print('5 - Sair')

        opcao = input('\nInforme uma das opções acima: ').lower()

        match opcao:
            case '1':
                cadastrar_veiculos()
            case '2':
                lista_veiculos()
            case '3':
                atualizar_veiculo()
            case '4':
                deletar_veiculo()
            case '5':
                print('Encerrando sistema...')
                break
            case _:
                print('Opção inválida!')


main()
