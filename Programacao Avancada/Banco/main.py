import tkinter as tk
from windows.login import Login
from mydb import Banco

db = Banco()

root = tk.Tk()
root.title("Login")
Login(db, root)

root.mainloop()

db.connection.close()