from app.routes import geral_bp
from app import db, app 
from flask import render_template, jsonify, request, redirect
from app.models import Universidade, Estudante
import uuid

@geral_bp.route("/cadastro-estudante", methods=["POST", "GET"])
def cadastroEstudante():
   
    if request.method == "POST":
        email = request.form.get("email")
        nome = request.form.get("nome")
        senha = request.form.get("senha")

        if email == None or nome == None or senha == None:
            return "Deu erro ao cadastrar, preencha todos os campos corretamente!"
        
        new_estudante = Estudante(
            id=str(uuid.uuid4()),
            nome=nome,
            email=email,
            senha=senha
        )

        db.session.add(new_estudante)
        db.session.commit()

        return redirect("/")
    
  
    return render_template("cadastro.html")
    
@geral_bp.route("/")
def index():
    return render_template("index.html")

@geral_bp.route("/universidade/<id>")
def universidade(id):
    if universidade:
        return render_template("universidade.html")
    else:
        return "Universidade não encontrada", 404