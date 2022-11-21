import tkinter as tk
from windows.createGame import Create
from windows.selectGame import Select
from windows.deleteGame import Delete
from windows.updateGame import Update
from games import Game
from matplotlib import pyplot

class Menu:
    def __init__(self, usuario, db, master=None):
        
        self.master = master
        self.usuario = usuario
        
        self.db = db
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 10
        self.body.pack()

        self.menuContainer = tk.Frame(master)
        self.menuContainer["padx"] = 20
        self.menuContainer.pack()

        self.select = tk.Button(self.menuContainer)
        self.select["text"] = "Lista"
        self.select["font"] = ("Calibri", "8")
        self.select["width"] = 12
        self.select["command"] = self.selectGame
        self.select.pack()
        
        self.create = tk.Button(self.menuContainer)
        self.create["text"] = "Novo"
        self.create["font"] = ("Calibri", "8")
        self.create["width"] = 12
        self.create["command"] = self.createGame
        self.create.pack()
        
        self.delete = tk.Button(self.menuContainer)
        self.delete["text"] = "Deletar"
        self.delete["font"] = ("Calibri", "8")
        self.delete["width"] = 12
        self.delete["command"] = self.deleteGame
        self.delete.pack()
        
        self.update = tk.Button(self.menuContainer)
        self.update["text"] = "Atualizar"
        self.update["font"] = ("Calibri", "8")
        self.update["width"] = 12
        self.update["command"] = self.updateGame
        self.update.pack()
        
        self.grafico = tk.Button(self.menuContainer)
        self.grafico["text"] = "Jogos/Usuario"
        self.grafico["font"] = ("Calibri", "8")
        self.grafico["width"] = 12
        self.grafico["command"] = self.graph
        self.grafico.pack()
        
    def selectGame(self):
        self.clearWindow()
        self.master.title("Create")
        Select(self.usuario, self.db, self.master)
    
    def createGame(self):
        self.clearWindow()
        self.master.title("Select")
        Create(self.usuario, self.db, self.master)
    
    def deleteGame(self):
        self.clearWindow()
        self.master.title("Delete")
        Delete(self.usuario, self.db, self.master)
    
    def updateGame(self):
        self.clearWindow()
        self.master.title("Update")
        Update(self.usuario, self.db, self.master)
        
    def graph(self):
        x, y = Game.getGraph(self.db)
        
        pyplot.bar(x=x, height=y)
        pyplot.show()
    
    def clearWindow(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.menuContainer.winfo_children():
            widgets.destroy()
        self.menuContainer.destroy()