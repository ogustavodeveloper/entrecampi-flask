from app import db, app 

class Adm(db.Model):
    email = db.Column(db.String(), primary_key=True)
    senha = db.Column(db.String())

    def __init__(self, email, senha):
        self.email = email 
        self.senha = senha 

class Estudante(db.Model):
    id = db.Column(db.String(), primary_key=True)
    nome = db.Column(db.String())
    email = db.Column(db.String())
    senha = db.Column(db.String())

    def __init__(self, id, nome, email, senha):
        self.id = id 
        self.nome = nome 
        self.email = email 
        self.senha = senha 

class Universidade(db.Model):
    nome = db.Column(db.String(), primary_key=True)
    sigla = db.Column(db.String())
    descricao = db.Column(db.Text)
    link_oficial = db.Column(db.String())
    localizacao = db.Column(db.String())
    repositorio = db.Column(db.String())
    fundacao = db.Column(db.String())


    def __init__(self, id, nome, sigla, descricao, link_oficial, localizacao, repositorio, fundacao):
        self.nome = nome
        self.sigla = sigla 
        self.descricao = descricao 
        self.link_oficial = link_oficial
        self.localizacao = localizacao
        self.repositorio = repositorio
        self.fundacao = fundacao

class Vestibular(db.Model):
    nome = db.Column(db.String(), primary_key=True)
    universidade = db.Column(db.String()) # sigla da universidade 
    datas = db.Column(db.String())
    link = db.Column(db.String())
    descricao = db.Column(db.Text)

    def __init__(self, nome, universidade,  datas, link, descricao):
        self.nome = nome 
        self.universidade = universidade
        self.datas = datas 
        self.link = link
        self.descricao = descricao 

class Bibliotecas(db.Model):
    universidade = db.Column(db.String(), primary_key=True)
    link = db.Column(db.String())
    nome = db.Column(db.String())

    def __init__(self, universidade, link, nome):
        self.universidade = universidade 
        self.link = link 
        self.nome = nome 

with app.app_context():
    db.create_all()