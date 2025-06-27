import requests

# response = requests.get('https://jsonplaceholder.typicode.com/users')
# data = response.json()

# users = {}

# for i in data:
#     nome = i['name']
#     email = i['email']
#     users[nome]=email

# print(f'Usuários: {users}')

# for i in data:
#     print(i['address']['geo']['lat'])



response = requests.get('https://jsonplaceholder.typicode.com/todos')
tarefas = response.json()

def tarefas_concluida():
    concluidas = {}

    for tarefa in tarefas:
        if tarefa['completed']:
            user_id = tarefa['userId']
            concluidas[user_id] = concluidas.get(user_id, 0) +1
    print(concluidas)

tarefas_concluida()