from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_cors import CORS
import os
from dotenv import load_dotenv

app = Flask(__name__)
 
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project-4.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'
app.config['SESSION_PERMANENT'] = True  # Sessão permanente
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=14)

db = SQLAlchemy(app)

CORS(app)

# Importe e registre as blueprints (rotas) da sua aplicação
from app.routes import geral_bp, universidade_bp
app.register_blueprint(geral_bp)
app.register_blueprint(universidade_bp)
