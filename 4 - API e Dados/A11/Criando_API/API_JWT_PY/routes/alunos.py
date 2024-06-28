from flask import request, jsonify
from flask_jwt_extended import jwt_required
from routes import routes_bp
from models import Aluno, db

@routes_bp.route('/alunos', methods=['GET'])
#@jwt_required()
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

@routes_bp.route('/alunos/<int:aluno_id>', methods=['GET'])
@jwt_required()
def get_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        return jsonify(aluno.to_dict())
    return jsonify({'error': 'Aluno não encontrado'}), 404

@routes_bp.route('/alunos', methods=['POST'])
@jwt_required()
def create_aluno():
    data = request.json
    new_aluno = Aluno(nome=data['nome'], idade=data['idade'], curso=data['curso'])
    db.session.add(new_aluno)
    db.session.commit()
    return jsonify(new_aluno.to_dict()), 201

@routes_bp.route('/alunos/<int:aluno_id>', methods=['PUT'])
@jwt_required()
def update_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        data = request.json
        aluno.nome = data['nome']
        aluno.idade = data['idade']
        aluno.curso = data['curso']
        db.session.commit()
        return jsonify(aluno.to_dict())
    return jsonify({'error': 'Aluno não encontrado'}), 404

@routes_bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])
@jwt_required()
def delete_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'message': 'Aluno deletado com sucesso'})
    return jsonify({'error': 'Aluno não encontrado'}), 404
