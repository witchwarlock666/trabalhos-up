from flask import Flask, redirect, jsonify
import sqlite3
from datetime import datetime, timedelta
import requests
from hashlib import sha1
from random import choices

app = Flask(__name__)

def getTime():
    db = sqlite3.connect("seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    url = conn.execute("select url from url where id = ?", (1,)).fetchone()
    url = url[0] + "/hora"
    r = requests.get(url = url)
    time = r.json()
    conn.close()
    return time

def chooseValidador():
    try:
        db = sqlite3.connect("seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn = db.cursor()
        
        t = datetime.strptime(getTime(), "%a, %d %b %Y %H:%M:%S %Z")
        t = t + timedelta(minutes=1)
        
        t2 = datetime.strptime(getTime(), "%a, %d %b %Y %H:%M:%S %Z")
        
        while t2 < t:
        
            res = conn.execute(
                "select ip, amount from validador where active = 1 and blocked = 0"
            ).fetchall()
            
            if len(res) > 2:
                ips, amounts = zip(*res)
                sum = conn.execute(
                    "select sum(amount) from validador where active = 1 and blocked = 0"
                ).fetchall()
                sum = sum[0]
                
                saldos = list(map(lambda s: max(5, min(s/sum[0], 40)), amounts))
                val = choices(population=ips, weights=saldos, k=3)
                return val
        return list
    except Exception as e:
        print(e)
        return list

def validation(ip, id):
    try:
        db = sqlite3.connect("seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn = db.cursor()
        
        url = "http://" + ip + "/validar/" + str(id)
        res = requests.get(url=url)
        res = res.json()
        
        print(res)
        
        select = conn.execute("select key from validador where ip = ?", (ip,)).fetchone()
        
        if res["chave"] == select[0]:
            print("ccc")
            return res["status"]
        else:
            print("bbb")
            return 0
            
    except Exception as e:
        print(e)
        return 0

@app.route("/")
def root():
    return "aaa"

@app.route("/seturlbanco/<string:url>")
def seturlbanco(url):
    db = sqlite3.connect("seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    url = "http://" + url
    
    conn.execute("update url set url = ? where id = 1", (url,))
    db.commit()
    conn.close()
    db.close()
    return redirect("/")

@app.route("/createdb", methods = ['GET'])
def createDatabase():
    db = sqlite3.connect("seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    conn.execute("""create table validador (
                    ip text primary key,
                    key text not null,
                    amount integer not null,
                    total_validations integer not null default 0,
                    flag_count integer not null default 0,
                    flags integer not null default 0,
                    blocked integer not null default 0,
                    active integer not null default 1
                );""")
    
    conn.execute("""create table url(
                    id integer not null primary key autoincrement,
                    url text
                )""")
    conn.execute("insert into url (url) values (?)", ("",))
    db.commit()
    
    conn.close()
    return redirect("/")

@app.route("/validador/<string:ip>/<int:amount>")
def register(ip, amount):
    db = sqlite3.connect("seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    if amount < 100:
        return jsonify({"status": 0})
    
    select = conn.execute("select blocked from validador where ip = ?", (ip,)).fetchone()

    if not select:
        key = sha1(bytes(ip, 'utf-8')).hexdigest()
        conn.execute("insert into validador (ip, key, amount, active) values (?, ?, ?, 1)", (ip, key, amount))
        db.commit()
        return jsonify({
            "status": 1,
            "chave": key
        })
    
    if select[0]:
        return jsonify({"status": 0})

    return jsonify({"status": 2})

@app.route("/validador/<int:id>")
def validate(id):
    db = sqlite3.connect("seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()
    
    val: list = chooseValidador()
    if not len(val):
        return jsonify({"status": 0, "aaa": "aaa"})
    
    for v in val:
        print(v)
        conn.execute("update validador set active = 0 where ip = ?", (v,))
        db.commit()
    
    r = [0, 0, 0]
    
    for i in range(3):
        ip = val[i]
        res = validation(ip, id)
        if res == 0:
            for v in val:
                conn.execute("update validador set active = 1 where ip = ?", (v,))
                db.commit()
            return jsonify({"status": 0, "aaa": "bbb"})
        select = conn.execute("select total_validations from validador where ip = ? ", (val[i],)).fetchone()
        conn.execute("update validador set total_validations = ? where ip = ?", (select[0] + 1, ip))
        db.commit()
        r[i] = res
        
    a = 0
    b = 0
    
    for i in r:
        if i == 1:
            a +=1
        else:
            b += 1
    if a == 3 or b == 3:
        return jsonify({"status": r[0]})
    
    elif a == 2:
        for i in range(3):
            select = conn.execute("select flags, flag_count, total_validations from validador where ip = ? ", (val[i],)).fetchone()
            if r[i] == 2:
                flags = select[0] + 1
                blocked = 0
                if flags == 3:
                    blocked = 1
                conn.execute("update validador set flag_count = 0, flags = ?, blocked = ? where ip = ?", (flags, blocked, val[i]))
                db.commit()
            else:
                flags = select[0]
                if flags > 0:
                    fc = select[1] + 1
                    if select[1] == 10000:
                        flags = flags - 1
                        fc = 0
                    conn.execute("update validador set flag_count = ?, flags = ? where ip = ?", (fc, flags, val[i]))
                    db.commit()
            conn.execute("update validador set active = 1 where ip = ?", (val[i],))
            db.commit()
        return jsonify({"status": 1})
    
    else:
        for i in range(3):
            select = conn.execute("select flags, flag_count, total_validations from validador where ip = ? ", (val[i],)).fetchone()
            if r[i] == 1:
                flags = select[0] + 1
                blocked = 0
                if flags == 3:
                    blocked = 1
                conn.execute("update validador set flag_count = 0, flags = ?, blocked = ? where ip = ?", (flags, blocked, val[i]))
                db.commit()
            else:
                flags = select[0]
                if flags > 0:
                    fc = select[1] + 1
                    if select[1] == 10000:
                        flags = flags - 1
                        fc = 0
                    conn.execute("update validador set flag_count = ?, flags = ? where ip = ?", (fc, flags, val[i]))
                    db.commit()
            conn.execute("update validador set active = 1 where ip = ?", (val[i],))
            db.commit()
        return jsonify({"status": 2})

if __name__ == "__main__":
    app.run()