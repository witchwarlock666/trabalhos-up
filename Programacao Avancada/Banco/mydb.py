import mysql.connector

class Banco():
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", user="gamesAdmin", passwd="123456", database="games")
