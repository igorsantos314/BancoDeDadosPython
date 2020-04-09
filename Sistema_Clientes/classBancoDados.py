import sqlite3

class bd:

    def __init__(self):
        #cria o banco de dados caso não exista
        self.connection = sqlite3.connect('/home/igor/Área de trabalho/Banco de Dados Python/user.db')
        self.cur = self.connection.cursor()

    def insertDataUser(self, ids, nome, cpf, Data_Nascimento):
        table = "INSERT INTO users (nome, cpf, Data_Nascimento, Saldo_Devedor) VALUES('{}', '{}', '{}', 0)".format(nome, cpf, Data_Nascimento)
        self.cur.execute(table)

        #consolidat base de dados
        self.connection.commit()

    def insertDataProduct(self, cod, nome, valor, stock):
        table = "INSERT INTO product (cod, nome, valor, stock) VALUES('{}', '{}', {}, {})".format(cod, nome, valor, stock)
        self.cur.execute(table)

        #consolidat base de dados
        self.connection.commit()

