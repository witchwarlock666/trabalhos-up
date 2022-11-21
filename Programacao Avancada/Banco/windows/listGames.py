import tkinter as tk
import windows.menu as menu
from games import Game

class SelectList:
    def __init__(self, usuario, db, master=None):
        
        self.master = master
        self.usuario = usuario
        
        self.db = db
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 10
        self.body.pack()

        self.gameContainer = tk.Frame(master)
        self.gameContainer["padx"] = 20
        self.gameContainer.pack()
        
        self.voltarContainer = tk.Frame(master)
        self.voltarContainer["pady"] = 20
        self.voltarContainer.pack()
        
        arr = self.getLista()
        
        self.games = tk.Text(self.gameContainer, font=self.fontePadrao)
        
        for (id, title) in arr:
            self.games.insert(tk.INSERT, "Id: " + str(id) + "   Titulo: " + title + "\n")
            
            
        self.games.pack(side=tk.LEFT)

        
        self.voltar = tk.Button(self.voltarContainer)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Calibri", "8")
        self.voltar["width"] = 12
        self.voltar["command"] = self.back
        self.voltar.pack(side=tk.LEFT)
        
    def back(self):
        self.clearWindow()
        self.master.title("Menu")
        menu.Menu(self.usuario, self.db, self.master)
    
    def getLista(self):
        return Game.getGameList(self.db, self.usuario)
    
    def clearWindow(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.gameContainer.winfo_children():
            widgets.destroy()
        self.gameContainer.destroy()
        for widgets in self.voltarContainer.winfo_children():
            widgets.destroy()
        self.voltarContainer.destroy()