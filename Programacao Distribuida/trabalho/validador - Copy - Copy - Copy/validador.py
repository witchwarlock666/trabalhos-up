from flask import Flask, redirect, jsonify
import sqlite3
from datetime import datetime, timedelta
import requests
import socket

app = Flask(__name__)

PORT = 5003


def getTime():
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect(
        "validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Obtém a URL a partir do banco de dados com base no ID
    url = conn.execute("select url from url where id = ?", (1,)).fetchone()
    # Concatena "/hora" à URL obtida
    url = url[0] + "/hora"
    # Faz uma solicitação GET para a URL e obtém a resposta em JSON
    r = requests.get(url=url)
    time = r.json()
    # Fecha a conexão com o banco de dados
    conn.close()
    # Retorna o tempo obtido
    return time


def getTransaction(id):
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect(
        "validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Obtém a URL a partir do banco de dados com base no ID
    url = conn.execute("select url from url where id = ?", (1,)).fetchone()
    # Concatena "/transacoes/" e o ID fornecido à URL obtida
    url = url[0] + "/transacoes/" + str(id)

    # Faz uma solicitação GET para a URL e obtém a resposta em JSON
    r = requests.get(url=url)
    r = r.json()

    # Fecha a conexão com o banco de dados
    conn.close()

    # Retorna a resposta JSON obtida
    return r


def getRem(id):
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect(
        "validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Obtém a URL a partir do banco de dados com base no ID
    url = conn.execute("select url from url where id = 1").fetchone()

    # Concatena "/cliente/" e o ID fornecido à URL obtida
    url = url[0] + "/cliente/" + str(id)

    # Faz uma solicitação GET para a URL e obtém a resposta em JSON
    r = requests.get(url=url)
    r = r.json()

    # Fecha a conexão com o banco de dados
    conn.close()

    # Retorna a resposta JSON obtida
    return r


@app.route("/seturlbanco/<string:url>")
def seturlbanco(url):
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect(
        "validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Adiciona o prefixo "http://" à URL recebida como parâmetro
    url = "http://" + url

    # Atualiza a URL no banco de dados com base no ID 1
    conn.execute("update url set url = ? where id = 1", (url,))
    db.commit()

    # Fecha a conexão com o banco de dados
    conn.close()
    db.close()

    # Redireciona para a página inicial ("/")
    return redirect("/")


@app.route("/seturlseletor/<string:url>")
def seturlseletor(url):
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect(
        "validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Adiciona o prefixo "http://" à URL recebida como parâmetro
    url = "http://" + url

    conn.execute("update url set url = ? where id = 2", (url,))
    db.commit()

    # Fecha a conexão com o banco de dados
    conn.close()
    db.close()

    # Redireciona para a página inicial ("/")
    return redirect("/")


@app.route("/seletor/<int:amount>")
def cadastrar(amount):
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect(
        "validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # hostname = socket.gethostname()
    # ip = socket.gethostbyname(hostname)
    # Obtém o IP e porta do servidor atual
    ip = "127.0.0.1"
    ip = ip + ":" + str(PORT)

    # Obtém a URL a partir do banco de dados com base no ID 2
    url = conn.execute("select url from url where id = 2").fetchone()
    url = url[0] + "/validador/" + ip + "/" + str(amount)
    # Faz uma solicitação GET para a URL e obtém a resposta em JSON
    r = requests.get(url=url)
    r = r.json()

    if r["status"] == 0:
        # Se o status for 0, ocorreu um erro
        db.close()
        return "Erro! Tente novamente."
    else:
        print(r)
        # Caso contrário, atualiza a chave no banco de dados com base no ID 1
        conn.execute(
            "update validador set key = ? where id = 1", (r["chave"],))
        db.commit()
        db.close()
        return r


@app.route("/")
def root():
    return "aaa"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/createdb", methods=['GET'])
def createDatabase():
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect(
        "validador.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Cria a tabela 'transactions' com as colunas necessárias
    conn.execute("""create table transactions(
                    id integer not null primary key autoincrement,
                    id_pay integer not null,
                    id_get integer not null,
                    value integer not null,
                    amount integer not null,
                    approved integer not null,
                    time timestamp not null
                )""")

    # Cria a tabela 'users' com as colunas necessárias
    conn.execute("""create table users(
                    id integer not null primary key autoincrement,
                    id_user integer not null,
                    blocked integer not null,
                    time timestamp
                )""")

    # Cria a tabela 'url' com as colunas necessárias
    conn.execute("""create table url(
                    id integer not null primary key autoincrement,
                    url text
                )""")

    # Cria a tabela 'validador' com as colunas necessárias
    conn.execute("""create table validador(
                    id integer not null primary key autoincrement,
                    key text,
                    ip text
                )""")

    # Obtém o hostname e IP do servidor
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    # Insere o IP do servidor na tabela 'validador'
    conn.execute("insert into validador (ip) values (?)", (ip,))

    # Insere duas linhas vazias na tabela 'url'
    conn.execute("insert into url (url) values (?)", ("",))
    conn.execute("insert into url (url) values (?)", ("",))
    db.commit()

    # Fecha a conexão com o banco de dados
    conn.close()

    # Redireciona para a página inicial ("/")
    return redirect("/")


@app.route("/teste", methods=['GET'])
def teste():
    # Conecta ao banco de dados SQLite
    db = sqlite3.connect("validador.db")
    conn = db.cursor()

    # Obtém a data e hora atual
    t = datetime.now()
    tstr = datetime.strftime(t, "%a, %d %b %Y %H:%M:%S %Z")

    # Calcula uma diferença de tempo de 1 segundo
    diff = t - timedelta(seconds=1)

    for i in range(0, 1000):
        # Insere uma nova transação na tabela 'transactions'
        conn.execute(
            "insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 1, t))
        db.commit()

        # Seleciona as transações que ocorreram entre 'diff' e 't'
        select = conn.execute(
            "select time from transactions where id_pay = ? and time between ? and ?", (1, diff, t)).fetchall()

        if len(select) >= 1000:
            # Se o número de transações for maior ou igual a 1000, bloqueia o usuário
            conn.execute("update users set blocked = 1, time = ? where id_user = ?",
                         (t + timedelta(minutes=1), 1))

            # Insere uma nova transação com 'approved' igual a 0
            conn.execute(
                "insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 0, t))
            db.commit()

    # Verifica se o usuário está bloqueado
    userblock = conn.execute(
        "select blocked, time from users where id_user = ?", (1,)).fetchone()

    if not userblock == None:
        if userblock[0] == 1:
            if tstr > userblock[1]:
                # Se o tempo atual for maior do que o tempo de desbloqueio, remove o bloqueio
                conn.execute(
                    "update users set blocked = 0 where id_user = ?", (1,))
                db.commit()
            else:
                # Se o usuário ainda estiver bloqueado, insere uma nova transação e retorna um status 2 e uma chave
                conn.execute(
                    "insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 1, t))

                db.commit()
                return jsonify({"status": 2, "key": 123})
    else:
        # Se o usuário não existir, insere um novo registro na tabela 'users'
        conn.execute(
            "insert into users (id_user, blocked) values (?, ?)", (1, 0))
        db.commit()

    # Seleciona as transações que ocorreram entre 'diff' e 't'
    select = conn.execute(
        "select time from transactions where id_pay = ? and time between ? and ?", (1, diff, t)).fetchall()

    if len(select) >= 1000:
        # Se o número de transações for maior ou igual a 1000, bloqueia o usuário
        conn.execute("update users set blocked = 1, time = ? where id_user = ?",
                     (t + timedelta(minutes=1), 1))

        # Insere uma nova transação com 'approved' igual a 0
        conn.execute(
            "insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 0, t))
        db.commit()
        return jsonify({"status": 2, "key": 123})

    if 10 <= 10:
        # Se a condição for verdadeira, insere uma nova transação e retorna um status 1 e uma chave
        conn.execute(
            "insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 1, t))
        db.commit()

        return jsonify({"status": 1, "key": 123})

    # Se a condição for falsa, insere uma nova transação com 'approved' igual a 0 e retorna um status 2 e uma chave
    conn.execute(
        "insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (1, 2, 10, 10, 0, t))
    db.commit()
    return jsonify({"status": 2, "key": 123})


@app.route("/validar/<int:id>", methods=['GET'])
def validar(id):
    try:
        # Conecta ao banco de dados SQLite
        db = sqlite3.connect("validador.db")
        conn = db.cursor()

        # Obtém a chave de validação da tabela 'validador'
        key = conn.execute(
            "select key from validador where id = 1").fetchone()[0]

        # Obtém a data e hora da última transação na tabela 'transactions'
        lastTrans = conn.execute(
            "select time from transactions desc").fetchone()

        # Obtém a transação com o ID especificado
        transaction = getTransaction(id)

        # Obtém as informações do remetente
        rem = getRem(transaction["remetente"])

        pay = rem["id"]
        get = transaction["recebedor"]
        value = transaction["valor"]
        amount = rem["qtdMoeda"]

        t = datetime.strptime(getTime(), "%a, %d %b %Y %H:%M:%S %Z")
        tstr = datetime.strftime(t, "%a, %d %b %Y %H:%M:%S %Z")
        
        # Verifica se a última transação e a transação atual existem
        if lastTrans and len(lastTrans):
            hTrans = datetime.strptime(
                transaction["horario"], "%a, %d %b %Y %H:%M:%S %Z")
            hLastTrans = datetime.strptime(lastTrans[0], "%Y-%m-%d %H:%M:%S")

            # Verifica se o horario da transação atual é menor que o da ultima transação ou maior que o horario atual
            if t < hTrans or hTrans < hLastTrans:
                print("1")
                return jsonify({"status": 2, "chave": key})

        # Verifica se o usuário está bloqueado
        userblock = conn.execute(
            "select blocked, time from users where id_user = ?", (pay,)).fetchone()

        if not userblock == None:
            if userblock[0] == 1:
                if tstr > userblock[1]:
                    # Se o tempo atual for maior do que o tempo de desbloqueio, remove o bloqueio
                    conn.execute(
                        "update users set blocked = 0 where id_user = ?", (pay,))
                    db.commit()
                else:
                    # Se o usuário ainda estiver bloqueado, insere uma nova transação e retorna um status 2 e a chave
                    conn.execute(
                        "insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)", (pay, get, value, amount, 0, t))
                    db.commit()
                    print("2")
                    return jsonify({"status": 2, "chave": key})
        else:
            # Se o usuário não existir, insere um novo registro na tabela 'users'
            conn.execute(
                "insert into users (id_user, blocked) values (?, ?)", (pay, 0))
            db.commit()

        # Calcula uma diferença de tempo de 1 segundo
        diff = t - timedelta(seconds=1)

        # Seleciona as transações que ocorreram entre 'diff' e 't'
        select = conn.execute(
            "select time from transactions where id_pay = ? and time between ? and ?", (pay, diff, t)).fetchall()

        if len(select) >= 1000:
            # Se o número de transações for maior ou igual a 1000, bloqueia o usuário e insere uma nova transação com 'approved' igual a 0
            conn.execute("update users set blocked = 1, time = ? where id_user = ?",
                         (t + timedelta(minutes=1), pay))
            conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)",
                         (pay, get, value, amount, 0, t))
            db.commit()
            print("3")
            return jsonify({"status": 2, "chave": key})

        if value <= amount:
            # Se o valor for menor ou igual ao saldo do remetente, insere uma nova transação com 'approved' igual a 1 e retorna um status 1 e a chave
            conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)",
                         (pay, get, value, amount, 1, t))
            db.commit()

            return jsonify({"status": 1, "chave": key})

        # Se o valor for maior do que o saldo do remetente, insere uma nova transação com 'approved' igual a 0 e retorna um status 2 e a chave
        conn.execute("insert into transactions (id_pay, id_get, value, amount, approved, time) values (?, ?, ?, ?, ?, ?)",
                     (pay, get, value, amount, 0, t))
        db.commit()
        print("4")
        return jsonify({"status": 2, "chave": key})

    except Exception as e:
        # Retorna um objeto JSON com um status 0, a chave e a exceção gerada
        print(e)
        return jsonify({"status": 0, "chave": key, "exception": str(e)})


if __name__ == "__main__":
    app.run(port=PORT)
