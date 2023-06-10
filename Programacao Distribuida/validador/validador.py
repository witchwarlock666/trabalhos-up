from flask import Flask, redirect, jsonify
import sqlite3
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

def getTime():
    db = sqlite3.connect("validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    url = conn.execute("select url from url where id = ?", (1,)).fetchone()
    url = url[0] + "/hora"
    r = requests.get(url = url)
    time = r.json()
    print(time)
    return time

@app.route("/seturl/<string:url>")
def seturl(url):
    db = sqlite3.connect("validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    url = "http://" + url
    
    conn.execute("update url set url = ?", (url,))
    db.commit()
    return redirect("/")

@app.route("/")
def root():
    return "aaa"

@app.route("/createdb", methods = ['GET'])
def createDatabase():
    db = sqlite3.connect("validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    conn.execute("""create table transactions(
                    id integer not null primary key autoincrement,
                    id_pay integer not null,
                    id_get integer not null,
                    value integer not null,
                    amount integer not null,
                    approved integer not null,
                    time timestamp not null
                )""")
    
    conn.execute("""create table users(
                    id integer not null primary key autoincrement,
                    id_user integer not null,
                    blocked integer not null,
                    time timestamp
                )""")
    
    conn.execute("""create table url(
                    id integer not null primary key autoincrement,
                    url text
                )""")
    conn.execute("insert into url (url) values (?)", ("",))
    db.commit()
    
    conn.close()
    return redirect("/")

@app.route("/teste", methods = ['GET'])
def teste():
    db = sqlite3.connect("validador.db")
    conn = db.cursor()
        
    t = datetime.now()
    tstr = datetime.strftime(t, "%a, %d %b %Y %H:%M:%S %Z")
    diff = t - timedelta(seconds=1)
    
    for i in range(0, 1000):
        conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 1, t))
        db.commit()
        select = conn.execute("select time from transactions where id_pay = ? and time between ? and ?", (1, diff, t)).fetchall()
    
        if len(select) >= 1000:
            conn.execute("update users set blocked = 1, time = ? where id_user = ?", (t + timedelta(minutes=1), 1))
            conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 0, t))
            db.commit()
    
    userblock = conn.execute("select blocked, time from users where id_user = ?", (1,)).fetchone()
        
    if not userblock == None:
        if userblock[0] == 1:
            if tstr > userblock[1]:
                conn.execute("update users set blocked = 0 where id_user = ?", (1,))
                db.commit()
            else:
                conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 1, t))
                db.commit()
                return jsonify({"status": 2, "key": 123})
    else:
        conn.execute("insert into users (id_user, blocked) values (?, ?)", (1, 0))
        db.commit()
    
    select = conn.execute("select time from transactions where id_pay = ? and time between ? and ?", (1, diff, t)).fetchall()
    
    if len(select) >= 1000:
        conn.execute("update users set blocked = 1, time = ? where id_user = ?", (t + timedelta(minutes=1), 1))
        conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 0, t))
        db.commit()
        return jsonify({"status": 2, "key": 123})
    
    if 10 <= 10:
        conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 1, t))
        db.commit()
        
        return jsonify({"status": 1, "key": 123})
    
    conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 0, t))
    db.commit()
    return jsonify({"status": 2, "key": 123})
        
    

@app.route("/validar/<int:pay>/<int:get>/<int:value>/<int:amount>/<int:key>", methods = ['GET'])
def validar(pay, get, value, amount, key):
    try:
        db = sqlite3.connect("validador.db")
        conn = db.cursor()
        
        t = datetime.strptime(getTime(), "%a, %d %b %Y %H:%M:%S %Z")
        tstr = datetime.strftime(t, "%a, %d %b %Y %H:%M:%S %Z")
        
        userblock = conn.execute("select blocked, time from users where id_user = ?", (pay,)).fetchone()
        
        if not userblock == None:
            if userblock[0] == 1:
                if tstr > userblock[1]:
                    conn.execute("update users set blocked = 0 where id_user = ?", (pay,))
                    db.commit()
                else:
                    conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (pay, get, value, amount, 0, t))
                    db.commit()
                    return jsonify({"status": 2, "key": key})
        else:
            conn.execute("insert into users (id_user, blocked) values (?, ?)", (pay, 0))
            db.commit()
        
        diff = t - timedelta(seconds=1)
        
        select = conn.execute("select time from transactions where id_pay = ? and time between ? and ?", (pay, diff, t)).fetchall()
        
        if len(select) >= 1000:
            conn.execute("update users set blocked = 1, time = ? where id_user = ?", (t + timedelta(minutes=1), pay))
            conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (pay, get, value, amount, 0, t))
            db.commit()
            return jsonify({"status": 2, "key": key})
        
        if value <= amount:
            conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (pay, get, value, amount, 1, t))
            db.commit()
            
            return jsonify({"status": 1, "key": key})
        
        conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (pay, get, value, amount, 0, t))
        db.commit()
        return jsonify({"status": 2, "key": key})
    
    except Exception as e:
        return jsonify({"status": 0, "key": key, "exception": str(e)})
    

if __name__ == "__main__":
    app.run()