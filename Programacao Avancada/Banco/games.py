from datetime import date

class Game:
    def __init__(self, title=None, developer=None, publisher=None, releaseDate=None):
        self.title = title
        self.developer = developer
        self.publisher = publisher
        self.releaseDate = releaseDate
        
    def newGame(db, title, developer, publisher, releaseDate, user):
        conn = db.connection.cursor()
        sql = "insert into games (title, developer, publisher, releaseDate, userId) values (%s, %s, %s, %s, %s)"
        values = (title, developer, publisher, releaseDate, user.id)
        conn.execute(sql, values)
        db.connection.commit()
        
    def getGame(db, gameTitle, user):
        conn = db.connection.cursor()
        sql = "select * from games where title = %s and userId = %s"
        values = (gameTitle, user.id)
        conn.execute(sql, values)
        
        arr = []
        try:
            for (gameId, title, developer, publisher, release, userId) in conn:
                arr.append(Game(title, developer, publisher,  release.strftime("%Y-%m-%d")))
            return arr[0]
        except:
            return None
        
    def deleteGame(db, title, user):
        conn = db.connection.cursor()
        sql = "delete from games where title = %s and userId = %s"
        values = (title, user.id)
        conn.execute(sql, values)
        db.connection.commit()
        
    def updateGame(db, id, title, developer, publisher, releaseDate):
        conn = db.connection.cursor()
        sql = "update games set title = %s, developer = %s, publisher = %s, releaseDate = %s where gameId = %s"
        values = (title, developer, publisher, releaseDate, id)
        conn.execute(sql, values)
        db.connection.commit()
        
    def getId(db, gameTitle, user):
        conn = db.connection.cursor()
        sql = "select gameId from games where title = %s and userId = %s"
        values = (gameTitle, user.id)
        conn.execute(sql, values)
        
        for (gameId) in conn:
            return gameId
        
    def getGraph(db):
        conn = db.connection.cursor()
        sql = "select u.login, count(g.userId) as Count from games g inner join usuarios as u on g.userId = u.userId group by g.userId"
        conn.execute(sql)
        
        logins = []
        nums = []
        
        for (login, n) in conn:
            logins.append(login)
            nums.append(n)
        return logins, nums
    
    def getGameList(db, user):
        conn = db.connection.cursor()
        sql = "select gameId, title from games where userId = %s"
        values = (user.id,)
        conn.execute(sql, values)
        
        arr = []
        
        for (gameId, title) in conn:
            arr.append((gameId, title))
            
        return arr