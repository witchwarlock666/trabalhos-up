class Log:
    def createLog(db, txt):
        conn = db.connection.cursor()
        sql = "insert into logs (logText) values (%s)"
        values = (txt,)
        conn.execute(sql, values)
        db.connection.commit()