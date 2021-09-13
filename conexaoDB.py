import pymysql
from datetime import datetime

conn = pymysql.connect(
    user='root',
    password='Firlastdatabase@2021',
    autocommit=True
)

cs = conn.cursor()

cs.execute('create database if not exists ConexaoDB_Jaedson')
cs.execute('use ConexaoDB_Jaedson')
cs.execute('create table if not exists clientes(id int primary key auto_increment, name varchar(50), email varchar(70), message text, message_data datetime)')

class Crud:
    conn.ping()
    def insertClient(self, name, email, message):
        cs.execute('insert into clientes(name, email, message, message_data) values(%s,%s,%s,%s)', (name, email, message, datetime.utcnow()))
        return True

    def returnAllClients(self):
        conn.ping()
        cs.execute('select id, name, email from clientes')
        clients = cs.fetchall()

        if clients is None:
            return False

        return clients

    def returnClient(self, userID):
        conn.ping()
        cs.execute('select * from clientes where id = %s', (userID))
        infoClient = cs.fetchone()

        if infoClient is None:
            return False

        return infoClient

    def deleteClient(self, userID):
        conn.ping()
        cs.execute('delete from clientes where id = %s', (userID))
        return True

    def updateClient(self, name, email, message, id):
        conn.ping()
        cs.execute('update clientes set name = %s, email = %s, message = %s where id = %s', (name, email, message, id))
        return True