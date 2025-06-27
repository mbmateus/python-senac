from services import db_connection as db

db.cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT,
    curso VARCHAR(100)
)
""")


def criar_aluno(nome, idade, curso):
    sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"
    db.cursor.execute(sql, (nome, idade, curso))
    db.connection.commit()
    print('Aluno cadastrado com Sucesso!')


def listar_alunos():
    db.cursor.execute("SELECT * FROM alunos")
    alunos = db.cursor.fetchall()
    for aluno in alunos:
        print(aluno)


def atualizar_aluno(id, nome, idade, curso):
    sql = "UPDATE alunos SET nome = %s, idade = %s, curso = %s WHERE id = %s"
    db.cursor.execute(sql, (nome, idade, curso, id))
    db.connection.commit()
    print('Aluno atualizado com sucesso!')


def deletar_aluno(id):
    sql = "DELETE FROM alunos WHERE id = %s"
    db.cursor.execute(sql, (id,))
    db.connection.commit()
    print('Aluno deletado com Sucesso!')


def menu():
    while True:
        print("\n--- MENU CRUD MYSQL ---")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Atualizar aluno")
        print("4. Deletar aluno")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")
            criar_aluno(nome, idade, curso)
        elif escolha == '2':
            listar_alunos()
        elif escolha == '3':
            id = int(input("ID do aluno: "))
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            curso = input("Novo curso: ")
            atualizar_aluno(id, nome, idade, curso)
        elif escolha == '4':
            id = int(input("ID do aluno a deletar: "))
            deletar_aluno(id)
        elif escolha == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


menu()

db.cursor.close()
db.connection.close()
