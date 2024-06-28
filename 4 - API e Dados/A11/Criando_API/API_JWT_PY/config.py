import os

#Secret Key deverá ser colocado a chave SSh da API 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_jwt_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://pyApp:python#motim@GH_SERVER/db_py_motim?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#    SQLALCHEMY_BINDS = {
#        'produtos_db': 'mssql+pyodbc://USERNAME:PASSWORD@SERVER_NAME/PRODUTOS_DATABASE_NAME?driver=ODBC+Driver+17+for+SQL+Server'
#    }
