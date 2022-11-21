class User():
    def newUser(self, usuario, senha, db):
        conn = db.connection.cursor()
        sql = "select login from usuarios where login = %s"
        values = (usuario)
        try:
            for (login) in conn:
                return
        except:
            sql = "insert into usuarios (login, senha) values (%s, %s)"
            values = (usuario, senha)
            conn.execute(sql, values)
            db.connection.commit()
        
    def login(self, usuario, senha, db):
        conn = db.connection.cursor()
        sql = "select userId, login from usuarios where login = %s and senha = %s"
        values = (usuario, senha)
        conn.execute(sql, values)
        
        for (userId, login) in conn:
            self.usuario = login
            self.id = userId
            return True
        return False
    
        