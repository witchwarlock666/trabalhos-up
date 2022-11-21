import tkinter as tk
import users
from windows.menu import Menu
from log import Log

class Login:
    def __init__(self, db, master=None):
        
        self.master = master
        
        self.db = db
        
        self.fontePadrao = ("Arial", "10")
        self.body = tk.Frame(master)
        self.body["pady"] = 10
        self.body.pack()

        self.nameContainer = tk.Frame(master)
        self.nameContainer["padx"] = 20
        self.nameContainer.pack()

        self.passContainer = tk.Frame(master)
        self.passContainer["padx"] = 20
        self.passContainer.pack()

        self.confirmContainer = tk.Frame(master)
        self.confirmContainer["pady"] = 20
        self.confirmContainer.pack()

        self.titulo = tk.Label(self.body, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = tk.Label(self.nameContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=tk.LEFT)

        self.nome = tk.Entry(self.nameContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=tk.RIGHT)

        self.senhaLabel = tk.Label(self.passContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=tk.LEFT)

        self.senha = tk.Entry(self.passContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=tk.RIGHT)

        self.autenticar = tk.Button(self.confirmContainer)
        self.autenticar["text"] = "Login"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.validate
        self.autenticar.pack(side=tk.LEFT)
        
        self.registrar = tk.Button(self.confirmContainer)
        self.registrar["text"] = "Registrar"
        self.registrar["font"] = ("Calibri", "8")
        self.registrar["width"] = 12
        self.registrar["command"] = self.register
        self.registrar.pack(side=tk.RIGHT)

        self.mensagem = tk.Label(self.confirmContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def validate(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        u = users.User()
        login = u.login(usuario, senha, self.db)
        
        if login:
            for widgets in self.body.winfo_children():
                widgets.destroy()
            self.body.destroy()
            for widgets in self.nameContainer.winfo_children():
                widgets.destroy()
            self.nameContainer.destroy()
            for widgets in self.passContainer.winfo_children():
                widgets.destroy()
            self.passContainer.destroy()
            for widgets in self.confirmContainer.winfo_children():
                widgets.destroy()
            self.confirmContainer.destroy()
            
            Log.createLog(self.db, "User " + u.usuario + " logged in")
            
            self.master.title("Menu")
            Menu(u, self.db, self.master)
            
    
    def register(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        u = users.User()
        if usuario != "" and senha != "":
            u.newUser(usuario, senha, self.db)
