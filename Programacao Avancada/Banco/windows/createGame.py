import tkinter as tk
from tkcalendar import DateEntry
import windows.menu as menu
from games import Game
from datetime import date
from log import Log

class Create:
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
        
        self.developerContainer = tk.Frame(master)
        self.developerContainer["padx"] = 20
        self.developerContainer.pack()
        
        self.publisherContainer = tk.Frame(master)
        self.publisherContainer["padx"] = 20
        self.publisherContainer.pack()
        
        self.releaseContainer = tk.Frame(master)
        self.releaseContainer["padx"] = 20
        self.releaseContainer.pack()
        
        self.confirmContainer = tk.Frame(master)
        self.confirmContainer["pady"] = 20
        self.confirmContainer.pack()

        self.titleLabel = tk.Label(self.titleContainer,text="Titulo", font=self.fontePadrao)
        self.titleLabel.pack(side=tk.LEFT)

        self.title = tk.Entry(self.titleContainer)
        self.title["width"] = 30
        self.title["font"] = self.fontePadrao
        self.title.pack(side=tk.RIGHT)
        
        self.developerLabel = tk.Label(self.developerContainer,text="Desenvolvedora", font=self.fontePadrao)
        self.developerLabel.pack(side=tk.LEFT)

        self.developer = tk.Entry(self.developerContainer)
        self.developer["width"] = 30
        self.developer["font"] = self.fontePadrao
        self.developer.pack(side=tk.RIGHT)
        
        self.publisherLabel = tk.Label(self.publisherContainer,text="Publicadora", font=self.fontePadrao)
        self.publisherLabel.pack(side=tk.LEFT)

        self.publisher = tk.Entry(self.publisherContainer)
        self.publisher["width"] = 30
        self.publisher["font"] = self.fontePadrao
        self.publisher.pack(side=tk.RIGHT)
        
        self.releaseLabel = tk.Label(self.releaseContainer,text="Lançamento", font=self.fontePadrao)
        self.releaseLabel.pack(side=tk.LEFT)

        self.release = DateEntry(self.releaseContainer)
        self.release["width"] = 28
        self.release["font"] = self.fontePadrao
        self.release.pack(side=tk.RIGHT)
        
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
        developer = self.developer.get()
        publisher = self.publisher.get()
        release = self.release.get_date().strftime('%Y-%m-%d')
        Game.newGame(self.db, title, developer, publisher, release, self.usuario)
        
        Log.createLog(self.db, "User " + self.usuario.usuario + " Added Game " + title)
        
        self.back()
    
    def clearWindow(self):
        for widgets in self.body.winfo_children():
            widgets.destroy()
        self.body.destroy()
        for widgets in self.titleContainer.winfo_children():
            widgets.destroy()
        self.titleContainer.destroy()
        for widgets in self.developerContainer.winfo_children():
            widgets.destroy()
        self.developerContainer.destroy()
        for widgets in self.publisherContainer.winfo_children():
            widgets.destroy()
        self.publisherContainer.destroy()
        for widgets in self.releaseContainer.winfo_children():
            widgets.destroy()
        self.releaseContainer.destroy()
        for widgets in self.confirmContainer.winfo_children():
            widgets.destroy()
        self.confirmContainer.destroy()
