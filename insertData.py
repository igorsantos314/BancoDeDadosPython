import sqlite3

#cria o banco de dados caso não exista
connection = sqlite3.connect('/home/igor/Área de trabalho/Banco de Dados Python/user.db')

cur = connection.cursor()

def inserirDados(ids, nome, cpf, Data_Nascimento):
    table = "INSERT INTO users (id, nome, cpf, Data_Nascimento) VALUES({}, '{}', '{}', '{}')".format(ids, nome, cpf, Data_Nascimento)
    cur.execute(table)

    #consolidat base de dados
    connection.commit()

def exibirTodos():
    show = "SELECT * FROM users"
    cur.execute(show)

    listUser = cur.fetchall()   

    for user in listUser:
        print('ID:{}\nNome:{}\nCPF:{}\nData de Nascimento:{}\n'.format(user[0], user[1], user[2], user[3]))

inserirDados(1, 'igor', '12959108450', '02091999')
exibirTodos()