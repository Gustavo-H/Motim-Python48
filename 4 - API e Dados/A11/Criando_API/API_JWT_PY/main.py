"""
Esta é uma API REST que force um CRUD simples para Objetos Alunos, Produtos e Usuarios
Esta API usa 2 bancos e dados o padrão que está no arquivo config 
e para os produtos ela usa outra banco de dados, neste os intrumentos sql são feitos manualmente 


para usar a API primeiro deverá criar o usuario na rota de usuarios {POST}

e em seguida criar o JWT Token na rota usuarios/auth {POST}


Autor: Gustavo Henrique
"""


from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from auth import auth_bp
from routes import routes_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt = JWTManager(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(routes_bp)

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se não existirem

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) # Remover parametro debug=True para deploy em produção
