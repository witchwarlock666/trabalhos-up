import tkinter as tk
import windows.menu as menu

class Present:
    def __init__(self, usuario, db, game, master=None):
        
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

        self.titleLabel = tk.Label(self.titleContainer,text="Titulo: " + game.title, font=self.fontePadrao)
        self.titleLabel.pack(side=tk.LEFT)
        
        self.developerLabel = tk.Label(self.developerContainer,text="Desenvolvedora: " + game.developer, font=self.fontePadrao)
        self.developerLabel.pack(side=tk.LEFT)
        
        self.publisherLabel = tk.Label(self.publisherContainer,text="Publicadora: " + game.publisher, font=self.fontePadrao)
        self.publisherLabel.pack(side=tk.LEFT)
        
        self.releaseLabel = tk.Label(self.releaseContainer,text="Data de Lançamento: " + game.releaseDate, font=self.fontePadrao)
        self.releaseLabel.pack(side=tk.LEFT)
        
        self.voltar = tk.Button(self.confirmContainer)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Calibri", "8")
        self.voltar["width"] = 12
        self.voltar["command"] = self.back
        self.voltar.pack(side=tk.LEFT)
        
    def back(self):
        self.clearWindow()
        self.master.title("Menu")
        menu.Menu(self.usuario, self.db, self.master)
    
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