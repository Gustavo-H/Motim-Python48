from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import Usuario, db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/usuarios/auth', methods=['POST'])
def authenticate_usuario():
    data = request.json
    username = data['username']
    password = data['password']
    usuario = Usuario.query.filter_by(username=username).first()
    if usuario and usuario.check_password(password):
        access_token = create_access_token(identity={'username': username})
        return jsonify({'access_token': access_token}), 200
    return jsonify({'error': 'Credenciais inválidas'}), 401
