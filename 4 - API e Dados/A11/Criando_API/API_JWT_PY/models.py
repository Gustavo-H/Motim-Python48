from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    curso = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'curso': self.curso
        }

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#Usar nos CRUD de Produtos 
class Produto:
    def __init__(self, id, nome, descricao_curta, descricao_longa, imagem, slug, preco_marketing, preco_marketing_promocional, tipo):
        self.id = id
        self.nome = nome
        self.descricao_curta = descricao_curta
        self.descricao_longa = descricao_longa
        self.imagem = imagem
        self.slug = slug
        self.preco_marketing = preco_marketing
        self.preco_marketing_promocional = preco_marketing_promocional
        self.tipo = tipo

    def to_dict(self):
        return {
            'id': self.id,
            'descricao_curta': self.descricao_curta,
            'descricao_longa': self.descricao_longa,
            'imagem': self.imagem,
            'slug': self.slug,
            'preco_marketing': self.preco_marketing,
            'preco_marketing_promocional': self.preco_marketing_promocional,
            'tipo': self.tipo,
        }