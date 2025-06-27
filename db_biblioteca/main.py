from services import db_connection as db

db.cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(145) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    data_publicacao DATETIME NOT NULL
)
""")


def cadastrar_livro(titulo, autor, data_publicacao):
    sql = 'INSERT INTO livros (titulo, autor, data_publicacao) VALUES (%s, %s, %s)'
    db.cursor.execute(sql, (titulo, autor, data_publicacao))
    db.connection.commit()
    print(f'Livro {titulo} cadastrado com Sucesso!')


def listar_livros():
    db.cursor.execute('SELECT * FROM livros')
    livros = db.cursor.fetchall()
    for livro in livros:
        print(livro)


def atualizar_livros(id, titulo, autor, data_publicacao):
    sql = 'UPDATE livros SET titulo = %s, autor = %s, data_publicacao = %s WHERE id = %s'
    db.cursor.execute(sql, (titulo, autor, data_publicacao, id))
    db.connection.commit()
    print('Livro atualizado com Sucesso!')


def deletar_livro(id):
    sql = 'DELETE FROM livros WHERE id = %s'
    db.cursor.execute(sql, (id,))
    db.connection.commit()
    print(f'Livro deletado com Sucesso!')


def menu():
    while True:
        print("\n--- MENU CRUD MYSQL ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Deletar livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            data_publicacao = input("Data publicação: ")
            cadastrar_livro(titulo, autor, data_publicacao)
        elif escolha == '2':
            listar_livros()
        elif escolha == '3':
            id = int(input("ID do livro: "))
            titulo = input("Novo titulo: ")
            autor = input("Novo autor: ")
            data_publicacao = int(input("Nova data publicação: "))
            atualizar_livros(id, titulo, autor, data_publicacao)
        elif escolha == '4':
            id = int(input("ID do livro a deletar: "))
            deletar_livro(id)
        elif escolha == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


menu()

db.cursor.close()
db.connection.close()
