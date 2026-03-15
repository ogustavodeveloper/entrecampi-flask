from flask import Blueprint

geral_bp = Blueprint('geral', __name__)
universidade_bp = Blueprint('universidade', __name__)

from app.routes import geral, universidade 