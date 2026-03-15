from app.routes import universidade_bp
from app import db, app
from flask import render_template, jsonify, request, redirect
from app.models import Universidade, Estudante
import uuid

@universidade_bp.route("/universidade/<sigla>")
def universidade(sigla):
    universidade = Universidade.query.filter_by(sigla=sigla).first()
    if universidade:
        return render_template("universidade.html", universidade=universidade)
    else:
        return "Universidade não encontrada", 404
    
@universidade_bp.route("/cadastro-universidade", methods=['GET', 'POST'])
def cadastrarUniversidade():
    if request.method == "POST":
        nome = request.form.get("nome")
        sigla = request.form.get("sigla")
        descricao = request.form.get("descricao")
        link_oficial = request.form.get("link_oficial")
        localizacao = request.form.get("localizacao")
        repositorio = request.form.get("repositorio")
        fundacao = request.form.get("fundacao")
        logo = request.form.get("logo")
        foto = request.form.get("foto")
        universidade_id = str(uuid.uuid4())  # Gerar um ID único para a universidade
        nova_universidade = Universidade(id=universidade_id, nome=nome, sigla=sigla, descricao=descricao, link_oficial=link_oficial, localizacao=localizacao, repositorio=repositorio, fundacao=fundacao, logo=logo, foto=foto)
        db.session.add(nova_universidade)
        db.session.commit()
        
        return redirect(f"/universidade/{sigla}")
    return render_template("cadastro-universidade.html")