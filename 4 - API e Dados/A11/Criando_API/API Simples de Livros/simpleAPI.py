from flask import Flask, jsonify, request


app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter e a pedra filosofal',
        'autor' : 'J.K. Rowling',
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e o prisioneiro dde askaban',
        'autor' : 'J.K. Rowling',
    },
    {
        'id': 3,
        'titulo': 'Harry Potter e a ordem da fenix',
        'autor' : 'J.K. Rowling',
    }
]

@app.route('/livro', methods=['GET'])
def get_livros():
    return jsonify(livros)


@app.route('/livro/<int:id>', methods=['GET'])
def get_livro(id):
    for livro in livros:
        if(livro.get('id') == id):
            return jsonify(livro)

@app.route('/livro', methods=['POST'])
def create_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


@app.route('/livro/<int:id>', methods=['PUT'])
def update_livro(id):
    livro_alterado = request.get_json()

    for i, livro in enumerate(livros):
        if(livro.get('id') == id):
            livros[i].update(livro_alterado)
            return jsonify(livro)  



@app.route('/livro/<int:id>', methods=['DELETE'])
def delete_livro(id):
    for i, livro in enumerate(livros):
        if(livro.get('id') == id):
            del livros[i]
    
    return jsonify(livros)



app.run(port=5000, host='localhost', debug=True)
