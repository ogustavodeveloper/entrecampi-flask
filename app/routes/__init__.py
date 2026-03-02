from flask import Blueprint

geral_bp = Blueprint('geral', __name__)

from app.routes import geral