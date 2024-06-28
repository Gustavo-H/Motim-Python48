from flask import request, jsonify
from flask_jwt_extended import jwt_required
from . import routes_bp
import db_connection as conn
from models import Produto

dbc = conn.SQLServerConnection()

@routes_bp.route('/produto', methods=['GET'])
@jwt_required()
def get_produto():

    try:
        query = "Select * From produto_produto"
        dbc.connect()
        dict_produtos = dbc.execute_select_query_to_dict(query)    

        print(dict_produtos)

        return jsonify(dict_produtos)
    except:
        return jsonify({'error': 'Não foi possivel listar produtos'}), 404


@routes_bp.route('/produto/<int:produto_id>', methods=['GET'])
@jwt_required()
def get_produtos(produto_id):

    try:
        query = f"Select * From produto_produto where id = {produto_id}"
        dbc.connect()
        dict_produtos = dbc.execute_select_query_to_dict(query)    

        #print(dict_produtos)

        return jsonify(dict_produtos)
    except:
        return jsonify({'error': 'Não foi possivel encontrar o produto'}), 404