from app.routes import geral_bp
from app import db, app 
from flask import render_template, jsonify, request 

@geral_bp.route("/hello")
def hello():
    return "Olá, Gustavo."