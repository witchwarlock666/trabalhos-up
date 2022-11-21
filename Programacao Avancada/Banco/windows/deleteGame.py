import tkinter as tk
import windows.menu as menu
from games import Game
from windows.presentGame import Present
from log import Log

class Delete:
    def __init__(self, usuario, db, master=None):
        
        self.master = master
        self.usuario = usuario
        
        self.db = db
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 10
        self.body.pack()

        self.titleContainer = tk.Frame(master)
        self.titleContainer["padx"] = 20
        self.titleContainer.pack()
        
        self.confirmContainer = tk.Frame(master)
        self.confirmContainer["pady"] = 20
        self.confirmContainer.pack()

        self.titleLabel = tk.Label(self.titleContainer,text="Titulo", font=self.fontePadrao)
        self.titleLabel.pack(side=tk.LEFT)

        self.title = tk.Entry(self.titleContainer)
        self.title["width"] = 30
        self.title["font"] = self.fontePadrao
        self.title.pack(side=tk.RIGHT)
        
        self.voltar = tk.Button(self.confirmContainer)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Calibri", "8")
        self.voltar["width"] = 12
        self.voltar["command"] = self.back
        self.voltar.pack(side=tk.LEFT)
        
        self.confirmar = tk.Button(self.confirmContainer)
        self.confirmar["text"] = "Confirmar"
        self.confirmar["font"] = ("Calibri", "8")
        self.confirmar["width"] = 12
        self.confirmar["command"] = self.confirm
        self.confirmar.pack(side=tk.RIGHT)
        
    def back(self):
        self.clearWindow()
        self.master.title("Menu")
        menu.Menu(self.usuario, self.db, self.master)
    
    def confirm(self):
        title = self.title.get()
        Game.deleteGame(self.db, title, self.usuario)
        
        Log.createLog(self.db, "User " + self.usuario.usuario + " Deleted Game " + title)
        
        self.back()
    
    def clearWindow(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.titleContainer.winfo_children():
            widgets.destroy()
        self.titleContainer.destroy()
        for widgets in self.confirmContainer.winfo_children():
            widgets.destroy()
        self.confirmContainer.destroy()