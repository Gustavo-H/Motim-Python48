#pip install Flask Flask-JWT-Extended Flask-SQLAlchemy pyodbc

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity 


app = Flask(__name__)

#Configuração do Banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://pyApp:python#motim@GH_SERVER/db_py_motim?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['JWT_SECRET_KEY'] = os.environ.get('MINHA_SECRET_KEY') or  'sua_jwt_chave_secreta'

jwt = JWTManager(app)

db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    curso = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return{
            "id" : self.id,
            "nome": self.nome,
            "idade": self.idade,
            "curso": self.curso
        }


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return{
            "id" : self.id,
            "username": self.username
        }



#Inicia o banco de dados
with app.app_context():
    db.create_all()

#Cria tabelas no banco de dados
with app.app_context():
    db.create_all()


#----------------------------------------------------------------------------------
#Rotas Para Usuarios

@app.route('/usuario', methods=['POST'])
def create_usuario():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        
        password_hash = generate_password_hash(password)

        novo_usuario = Usuario(username=username, password_hash=password_hash)

        db.session.add(novo_usuario)

        db.session.commit()

        return jsonify(novo_usuario.to_dict()), 201
    
    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify({"error": str(ex)}), 400

@app.route('/usuario/auth', methods=['POST'])
def authenticate_usuario():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        
        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and check_password_hash(usuario.password_hash, password):
            access_token = create_access_token(identity={'username':username}, expires_delta=False)
            return jsonify({'access_token': access_token}), 200 

        return jsonify({'error': "Credenciais Inválidas!!!"}), 200 
    
    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify({"error": str(ex)}), 400





#Rotas Para Usuarios
#----------------------------------------------------------------------------------







#----------------------------------------------------------------------------------
#Rotas Para Alunos


#End Point
@app.route('/aluno', methods=['GET'])
@jwt_required()
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])


@app.route('/aluno/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        return jsonify(aluno.to_dict()), 200
    return jsonify({"error": "Aluno não encontrado"}), 418



@app.route('/aluno', methods=['POST'])
def create_aluno():
    try:
        data = request.json
        novo_aluno = Aluno(nome=data['nome'], idade = data['idade'], curso = data['curso'])
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify(novo_aluno.to_dict()), 201
    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify({"error": str(ex)}), 400


@app.route('/aluno/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    
    aluno = Aluno.query.get(aluno_id)
    if aluno:           
        try:
            data = request.json
            aluno.nome = data['nome']
            aluno.idade = data['idade']
            aluno.curso = data['curso']
            
            db.session.commit()
            return jsonify(aluno.to_dict()), 200
        except SQLAlchemyError as ex:
            db.session.rollback()
            return jsonify({"error": str(ex)}), 400
    return jsonify({"error": "Aluno não encontrado"}), 404


@app.route('/aluno/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    
    aluno = Aluno.query.get(aluno_id)
    if aluno:           
        try:
            db.session.delete(aluno)
            
            db.session.commit()
            return jsonify({"mensage": "Aluno Deletado"}), 200
        except SQLAlchemyError as ex:
            db.session.rollback()
            return jsonify({"error": str(ex)}), 400
    return jsonify({"error": "Aluno não encontrado"}), 404


#Rotas Para Alunos 
#----------------------------------------------------------------------------------








if __name__ == '__main__':
    app.run(debug=True)