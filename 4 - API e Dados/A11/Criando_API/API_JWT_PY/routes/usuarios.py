from flask import request, jsonify
from flask_jwt_extended import jwt_required
from routes import routes_bp
from models import Usuario, db

@routes_bp.route('/usuarios', methods=['GET'])
@jwt_required()
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@routes_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
@jwt_required()
def get_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        return jsonify(usuario.to_dict())
    return jsonify({'error': 'Usuario não encontrado'}), 404

@routes_bp.route('/usuarios', methods=['POST'])
#@jwt_required()
def create_usuario():
    data = request.json
    new_usuario = Usuario(username=data['username'])
    new_usuario.set_password(data['password'])
    db.session.add(new_usuario)
    db.session.commit()
    return jsonify(new_usuario.to_dict()), 201

@routes_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
@jwt_required()
def update_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        data = request.json
        usuario.username = data['username']
        if 'password' in data:
            usuario.set_password(data['password'])
        db.session.commit()
        return jsonify(usuario.to_dict())
    return jsonify({'error': 'Usuario não encontrado'}), 404

@routes_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
@jwt_required()
def delete_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuario deletado com sucesso'})
    return jsonify({'error': 'Usuario não encontrado'}), 404
