from time import time
from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dataclasses import dataclass
from datetime import date, datetime
import requests
  
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@dataclass
class Cliente(db.Model):
    id: int
    nome: str
    senha: int
    qtdMoeda: int
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), unique=False, nullable=False)
    senha = db.Column(db.String(20), unique=False, nullable=False)
    qtdMoeda = db.Column(db.Integer, unique=False, nullable=False)
    
    def getDict(self):
        return {"id": self.id, "nome": self.nome, "senha": self.senha, "qtdMoeda": self.qtdMoeda}

class Seletor(db.Model):
    id: int
    nome: str
    ip: str
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), unique=False, nullable=False)
    ip = db.Column(db.String(15), unique=False, nullable=False)
    
    def getDict(self):
        return {"id": self.id, "nome": self.nome, "ip": self.ip}
    
class Transacao(db.Model):
    id: int
    remetente: int
    recebedor: int
    valor: int
    status: int
    
    id = db.Column(db.Integer, primary_key=True)
    remetente = db.Column(db.Integer, unique=False, nullable=False)
    recebedor = db.Column(db.Integer, unique=False, nullable=False)
    valor = db.Column(db.Integer, unique=False, nullable=False)
    horario = db.Column(db.DateTime, unique=False, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=False)
    
    def getDict(self):
        return {"id": self.id, "remetente": self.remetente, "recebedor": self.recebedor, "valor": self.valor, "horario": self.horario, "status": self.status}

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def index():
    return render_template('api.html')

@app.route('/cliente', methods = ['GET'])
def ListarCliente():
    if(request.method == 'GET'):
        clientes = Cliente.query.all()
        o = {}
        for i in clientes:
            a = i.getDict()
            o[a["id"]] = a
        return jsonify(o)  

@app.route('/cliente/<string:nome>/<string:senha>/<int:qtdMoeda>', methods = ['POST'])
def InserirCliente(nome, senha, qtdMoeda):
    if request.method=='POST' and nome != '' and senha != '' and qtdMoeda != '':
        objeto = Cliente(nome=nome, senha=senha, qtdMoeda=qtdMoeda)
        db.session.add(objeto)
        db.session.commit()
        o = objeto.getDict()
        return jsonify(objeto)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/cliente/<int:id>', methods = ['GET'])
def UmCliente(id):
    if(request.method == 'GET'):
        objeto = Cliente.query.get(id)
        o = objeto.getDict()
        return jsonify(objeto)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/cliente/<int:id>/<int:qtdMoeda>', methods=["POST"])
def EditarCliente(id, qtdMoeda):
    if request.method=='POST':
        try:
            varId = id
            varqtdMoeda = qtdMoeda
            cliente = Cliente.query.filter_by(id=id).first()
            db.session.commit()
            cliente.qtdMoeda = qtdMoeda
            db.session.commit()
            o = cliente.getDict()
            return jsonify(o)
        except Exception as e:
            data={
                "message": "Atualização não realizada"
            }
            return jsonify(data)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/cliente/<int:id>', methods = ['DELETE'])
def ApagarCliente(id):
    if(request.method == 'DELETE'):
        objeto = Cliente.query.get(id)
        db.session.delete(objeto)
        db.session.commit()

        data={
            "message": "Cliente Deletado com Sucesso"
        }

        return jsonify(data)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/seletor', methods = ['GET'])
def ListarSeletor():
    if(request.method == 'GET'):
        produtos = Seletor.query.all()
        o = {}
        for i in produtos:
            a = i.getDict()
            o[a["id"]] = a
        return jsonify(o)

@app.route('/seletor/<string:nome>/<string:ip>', methods = ['POST'])
def InserirSeletor(nome, ip):
    if request.method=='POST' and nome != '' and ip != '':
        objeto = Seletor(nome=nome, ip=ip)
        db.session.add(objeto)
        db.session.commit()
        o = objeto.getDict()
        return jsonify(o)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/seletor/<int:id>', methods = ['GET'])
def UmSeletor(id):
    if(request.method == 'GET'):
        produto = Seletor.query.get(id)
        o = produto.getDict()
        return jsonify(o)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/seletor/<int:id>/<string:nome>/<string:ip>', methods=["POST"])
def EditarSeletor(id, nome, ip):
    if request.method=='POST':
        try:
            varNome = nome
            varIp = ip
            validador = Seletor.query.filter_by(id=id).first()
            db.session.commit()
            validador.nome = varNome
            validador.ip = varIp
            db.session.commit()
            o = validador.getDict()
            return jsonify(o)
        except Exception as e:
            data={
                "message": "Atualização não realizada"
            }
            return jsonify(data)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/seletor/<int:id>', methods = ['DELETE'])
def ApagarSeletor(id):
    if(request.method == 'DELETE'):
        objeto = Seletor.query.get(id)
        db.session.delete(objeto)
        db.session.commit()

        data={
            "message": "Validador Deletado com Sucesso"
        }

        return jsonify(data)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/hora', methods = ['GET'])
def horario():
    if(request.method == 'GET'):
        objeto = datetime.now()
        return jsonify(objeto)

@app.route('/transacoes', methods = ['GET'])
def ListarTransacoes():
    if(request.method == 'GET'):
        transacoes = Transacao.query.all()
        o = {}
        for i in transacoes:
            a = i.getDict()
            o[a["id"]] = a
        return jsonify(o)
    
    
@app.route('/transacoes/<int:rem>/<int:reb>/<int:valor>', methods = ['POST'])
def CriaTransacao(rem, reb, valor):
    if request.method=='POST':
        objeto = Transacao(remetente=rem, recebedor=reb,valor=valor,status=0,horario=datetime.now())
        print(objeto)
        db.session.add(objeto)
        db.session.commit()
        o = objeto.getDict()
        id = o["id"]
        seletor = requests.get("http://127.0.0.1:1234/seletor/1").json()
        url = "http://" + seletor["ip"] + "/validador/" + str(id)
        status = requests.get(url).json()["status"]
        res = requests.post(f"http://127.0.0.1:1234/transactions/{id}/{status}").json()
        return jsonify(res)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/transacoes/<int:id>', methods = ['GET'])
def UmaTransacao(id):
    if(request.method == 'GET'):
        objeto = Transacao.query.get(id)
        o = objeto.getDict()
        return jsonify(o)
    else:
        return jsonify(['Method Not Allowed'])

@app.route('/transactions/<int:id>/<int:status>', methods=["POST"])
def EditaTransacao(id, status):
    if request.method=='POST':
        try:
            objeto = Transacao.query.filter_by(id=id).first()
            db.session.commit()
            objeto.id = id
            objeto.status = status
            db.session.commit()
            o = objeto.getDict()
            print(o)
            return jsonify(o)
        except Exception as e:
            data={
                "message": "transação não atualizada"
            }
            return jsonify(data)
    else:
        return jsonify(['Method Not Allowed'])

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=1234)