alunos = []

def create(name, age):
    alunos.append({ 'name': name, 'age': age })


def read():
    for aluno in alunos:
        print(aluno)


def update(index, name, age):
    alunos[index]['name'] = name
    alunos[index]['age'] = age


def delete(index):
    alunos.pop(index)


create('Mateus', 22)
create('Stefany', 25)
read()

update(0, 'Mateus', 23)
read()

delete(1)
read()
