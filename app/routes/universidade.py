from app.routes import universidade_bp
from app import db, app
from flask import render_template, jsonify, request, redirect
from app.models import Universidade, Estudante
import uuid

@universidade_bp.route("/universidade/<id>")
def universidade(id):
    universidade = Universidade.query.get(id)
    if universidade:
        return render_template("universidade.html", universidade=universidade)
    else:
        return "Universidade não encontrada", 404
    
