from flask import Flask, redirect, jsonify
import sqlite3
from datetime import datetime, timedelta
import requests
from hashlib import sha1
from random import choices
from numpy.random import choice
from numpy import array
from math import ceil

app = Flask(__name__)

# Função para obter o tempo atual do banco


def getTime():
    # Conectando ao banco de dados SQLite
    db = sqlite3.connect(
        "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Obtendo a URL da tabela "url" com o id 1
    url = conn.execute("select url from url where id = 1").fetchone()
    # Adicionando "/hora" ao final da URL
    url = url[0] + "/hora"
    # Fazendo uma requisição GET para a URL
    r = requests.get(url=url)
    # Obtendo o tempo como resposta em formato JSON
    time = r.json()
    # Fechando a conexão com o banco de dados
    conn.close()

    # Retornando o tempo obtido
    return time


def chooseValidador():
    try:
        # Conectando ao banco de dados SQLite
        db = sqlite3.connect(
            "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn = db.cursor()

        # Obtendo o tempo atual e adicionando 1 minuto
        t = datetime.strptime(getTime(), "%a, %d %b %Y %H:%M:%S %Z")
        t = t + timedelta(minutes=1)

        # Obtendo o tempo atual novamente
        t2 = datetime.strptime(getTime(), "%a, %d %b %Y %H:%M:%S %Z")

        # Executa o loop enquanto o tempo atual for menor que o tempo t
        while t2 < t:
            print(t - t2)
            select = conn.execute(
                "select ip, amount from validador where active = 1 and blocked = 0"
            ).fetchall()
            if len(select) > 2:
                ips, amounts = zip(*select)

                # Obtém a soma das quantidades dos validadores ativos e não bloqueados
                sum = conn.execute(
                    "select sum(amount) from validador where active = 1 and blocked = 0").fetchall()
                sum = sum[0][0]

                # Normaliza as quantidades para que a soma seja 1 e limite cada valor entre 5.0 e 40.0
                amounts = list(
                    map(lambda s: max(5.0, min((s/sum) * 100, 40.0)), amounts))

                # Converte as quantidades em um array numpy
                amounts = array(amounts)

                # Normaliza as quantidades para que a soma seja 1
                amounts /= amounts.sum()

                # Escolhe 3 IPs com base nas quantidades, sem substituição
                val = choice(ips, 3, False, amounts)
                val = list(val)
                return val
            t2 = datetime.strptime(getTime(), "%a, %d %b %Y %H:%M:%S %Z")

        return list()
    except Exception as e:
        print(e)
        return list()


def getValue(id):  # Função para obter o valor de uma transação a partir do banco

    # Conectando ao banco de dados SQLite
    db = sqlite3.connect(
        "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Obtendo a URL da tabela "url" com o id fornecido
    url = conn.execute("select url from url where id = ?", (1,)).fetchone()
    url = url[0] + "/transacoes/" + str(id)

    # Fazendo uma requisição GET para a URL
    r = requests.get(url=url)
    # Obtendo a resposta em formato JSON
    r = r.json()
    # Obtendo o valor da transação
    value = r["valor"]
    # Fechando a conexão com o banco de dados
    conn.close()

    # Retornando o valor da transação
    return value

# Função para realizar a validação de um validador em uma URL específica


def validation(ip, id):

    try:
        # Conectando ao banco de dados SQLite
        db = sqlite3.connect(
            "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        conn = db.cursor()

        # Construindo a URL com base no IP e no ID fornecidos
        url = "http://" + ip + "/validar/" + str(id)

        # Fazendo uma requisição GET para a URL
        r = requests.get(url=url)
        r = r.json()  # Obtendo a resposta em formato JSON
        print(r)

        # Obtendo a chave do validador com base no IP
        select = conn.execute(
            "select key from validador where ip = ?", (ip,)).fetchone()

        # Verificando se a chave retornada pela URL é igual à chave armazenada no banco de dados
        if r["chave"] == select[0]:
            return r["status"]  # Retorna o status retornado pela URL
        else:
            print("aaaaaaaaaa")
            return 0  # Retorna 0 se as chaves não forem iguais

    except Exception as e:
        print(e)
        return 0  # Retorna 0 em caso de exceção ou erro


@app.route("/")
def root():
    return "aaa"


@app.route("/seturlbanco/<string:url>")
# Rota para definir a URL do banco
def seturlbanco(url):

    # Conectando ao banco de dados SQLite
    db = sqlite3.connect(
        "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Adicionando o prefixo "http://" à URL fornecida
    url = "http://" + url

    # Atualizando a tabela "url" com a nova URL no registro com ID 1
    conn.execute("update url set url = ? where id = 1", (url,))
    # Salvando as alterações no banco de dados
    db.commit()
    # Fechando o cursor
    conn.close()
    # Fechando a conexão com o banco de dados
    db.close()

    # Redirecionando para a página inicial ("/") após a atualização
    return redirect("/")


@app.route("/createdb", methods=['GET'])
# Rota para criar o banco de dados
def createDatabase():

    # Conectando ao banco de dados SQLite
    db = sqlite3.connect(
        "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    # Criação da tabela "validador"
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

    # Criação da tabela "url"
    conn.execute("""create table url(
                    id integer not null primary key autoincrement,
                    url text
                )""")
    # Inserção de um registro vazio na tabela "url"
    conn.execute("insert into url (url) values (?)", ("",))

    # Salvando as alterações no banco de dados
    db.commit()
    # Fechando o cursor
    conn.close()

    # Redirecionando para a página inicial ("/") após a criação do banco de dados
    return redirect("/")


@app.route("/validador/<string:ip>/<int:amount>")
# Rota para registrar um validador com um determinado IP e saldo
def register(ip, amount):

    # Conectando ao banco de dados SQLite
    db = sqlite3.connect(
        "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    if amount < 100:
        # Retorna um JSON com o status 0 se o saldo for inferior a 100
        return jsonify({"status": 0})

    # Verifica se o IP já está registrado e se está bloqueado
    select = conn.execute(
        "select blocked from validador where ip = ?", (ip,)).fetchone()

    if not select:
        # Gera uma chave baseada no IP usando o algoritmo SHA1
        key = sha1(bytes(ip, 'utf-8')).hexdigest()

        # Insere um novo registro na tabela "validador" com o IP, a chave, o saldo e o status ativo
        conn.execute(
            "insert into validador (ip, key, amount, active) values (?, ?, ?, 1)", (ip, key, amount))
        db.commit()

        return jsonify({
            "status": 1,
            "chave": key
        })  # Retorna um JSON com o status 1 e a chave gerada

    if select[0]:
        # Retorna um JSON com o status 0 se o validador estiver bloqueado
        return jsonify({"status": 0})

    # Retorna um JSON com o status 2 se o validador já estiver registrado
    return jsonify({"status": 2})


@app.route("/validador/<string:ip>")
# Rota para remover um validador com um determinado IP
def remove(ip):
    # Conectando ao banco de dados SQLite
    db = sqlite3.connect(
        "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    select = conn.execute(
        "select * from validador where ip = ?", (ip,)).fetchone()

    # Se o validador com o IP especificado existir no banco de dados
    if select:
        conn.execute("delete from validador where ip = ?", (ip,))
        db.commit()
        # Retorna um JSON com status 1 indicando que o validador foi removido com sucesso
        return jsonify({"status": 1})

    # Retorna um JSON com status 0 indicando que o validador não foi encontrado
    return jsonify({"status": 0})


@app.route("/validador/<int:id>")
# Rota para realizar a validação de um determinado ID de transação
def validate(id):

    # Conectando ao banco de dados SQLite
    db = sqlite3.connect(
        "seletor.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    conn = db.cursor()

    val: list = chooseValidador()
    print(val)
    if not val:
        # Retorna um JSON com status 0 e uma mensagem se nenhum validador estiver disponível
        return jsonify({"status": 0, "aaa": "aaa"})

    for v in val:
        conn.execute("update validador set active = 0 where ip = ?", (v,))
        db.commit()

    r = [0, 0, 0]

    for i in range(3):
        ip = val[i]
        res = validation(ip, id)
        print(res)
        if res == 0:
            for v in val:
                conn.execute(
                    "update validador set active = 1 where ip = ?", (v,))
                db.commit()
            # Retorna um JSON com status 0 e uma mensagem se a validação falhar
            return jsonify({"status": 0, "aaa": "bbb"})
        select = conn.execute(
            "select total_validations from validador where ip = ? ", (val[i],)).fetchone()
        conn.execute(
            "update validador set total_validations = ? where ip = ?", (select[0] + 1, ip))
        db.commit()
        r[i] = res

    a = 0
    b = 0

    for i in r:
        if i == 1:
            a += 1
        else:
            b += 1
    if a == 3 or b == 3:
        # Se todas as três validações forem iguais (todas aprovadas ou todas reprovadas)
        for v in val:
            select = conn.execute(
                "select flags, flag_count, total_validations, amount from validador where ip = ? ", (val[i],)).fetchone()
            value = getValue(id)
            value = ceil(value/20)
            amount = select[3] + value
            print(amount)
            flags = select[0]
            if flags > 0:
                fc = select[1] + 1
                if select[1] == 10000:
                    flags = flags - 1
                    fc = 0
                conn.execute(
                    "update validador set flag_count = ?, flags = ? where ip = ?", (fc, flags, val[i]))
                db.commit()
            conn.execute(
                "update validador set active = 1, amount = ? where ip = ?", (amount, v))
            db.commit()
        # Retorna um JSON com o status da primeira validação
        return jsonify({"status": r[0]})

    elif a == 2:
        # Se duas das três validações forem iguais
        for i in range(3):
            select = conn.execute(
                "select flags, flag_count, total_validations, amount from validador where ip = ? ", (val[i],)).fetchone()
            value = getValue(id)
            value = ceil(value/20)
            amount = select[3]
            if r[i] == 2:
                # Se a validação for reprovada (status 2), incrementa as flags
                flags = select[0] + 1
                blocked = 0
                if flags == 3:
                    blocked = 1
                conn.execute(
                    "update validador set flag_count = 0, flags = ?, blocked = ? where ip = ?", (flags, blocked, val[i]))
                db.commit()
            else:
                # Se a validação for aprovada, atualiza o saldo e as flags, se necessário
                amount = select[3] + value
                flags = select[0]
                if flags > 0:
                    fc = select[1] + 1
                    if select[1] == 10000:
                        flags = flags - 1
                        fc = 0
                    conn.execute(
                        "update validador set flag_count = ?, flags = ? where ip = ?", (fc, flags, val[i]))
                    db.commit()
            conn.execute(
                "update validador set active = 1, amount = ? where ip = ?", (amount, val[i]))
            db.commit()
        # Retorna um JSON com status 1 se duas das três validações forem bem-sucedidas
        return jsonify({"status": 1})

    else:
        # Se nenhuma das condições anteriores for atendida (uma validação aprovada e duas reprovadas)
        for i in range(3):
            select = conn.execute(
                "select flags, flag_count, total_validations, amount from validador where ip = ? ", (val[i],)).fetchone()
            value = getValue(id)
            value = ceil(value/20)
            amount = select[3]
            if r[i] == 1:
                # Se a validação for aprovada (status 1), incrementa as flags
                flags = select[0] + 1
                blocked = 0
                if flags == 3:
                    blocked = 1

                conn.execute(
                    "update validador set flag_count = 0, flags = ?, blocked = ? where ip = ?", (flags, blocked, val[i]))
                db.commit()

            else:
                # Se a validação for reprovada, atualiza o saldo e as flags, se necessário
                amount = select[3] + value
                flags = select[0]

                if flags > 0:
                    fc = select[1] + 1
                    if select[1] == 10000:
                        flags = flags - 1
                        fc = 0
                    conn.execute(
                        "update validador set flag_count = ?, flags = ? where ip = ?", (fc, flags, val[i]))
                    db.commit()
            conn.execute(
                "update validador set active = 1, amount = ? where ip = ?", (amount, val[i]))
            db.commit()
        # Retorna um JSON com status 2 se apenas uma das três validações for bem-sucedida
        return jsonify({"status": 2})


if __name__ == "__main__":
    app.run()
