# Na criação de uma API existem 4 etapas principais
# API é um domínio para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Ex: Criar uma API que disponibiliza a consulta, criação, edição e exclusão de um livro
# 2. URL base - Local que serão feitas as requisições - Ex: nesse caso será localhost porém com domínio comprado pode ser ex: youtube.com/api/...
# 3. Endpoints (abaixo)
# localhost/livros (GET) para consultar os livros
# localhost/livros (POST) para criar novos livros
# localhost/livros/id (GET) precisa do id do livro específico
# localhost/livros/id (PUT) para modificar o livro do id
# localhost/livros/id (DELETE) para deletar o livro do id
# 4. Quais são os recursos/funcionalidades disponibilizados - serão livros
# Flask é ótimo para iniciantes

# Flask = servidor
# jsonfy = retorna os dados no formato json
# request = fazer as requisições para acessar os dados

from flask import Flask, jsonify, request

# Servidor que está hospedando a API - cria a aplicação com o nome atual do arquivo
app = Flask(__name__)

# Fonte de dados - origem dos dados
# Pode ser utilizado arquivo, banco, etc

# Dicionários dentro da lista
livros = [
    {
        'id': 1,
        'titulo': 'Python Para Análise de Dados: Tratamento de Dados com Pandas, NumPy & Jupyter',
        'autor': 'Wes McKinney',
        'paginas': 624,
        'data_publicacao': '16/03/2023'
    },
    {
        'id': 2,
        'titulo': 'Mãos à Obra: Aprendizado de Máquina com Scikit-Learn, Keras & TensorFlow: Conceitos, Ferramentas e Técnicas Para a Construção de Sistemas Inteligentes',
        'autor': 'Aurélien Géron',
        'paginas': 640,
        'data_publicacao': '06/10/2021'
    },
    {
        'id': 3,
        'titulo': 'SQL Para Análise de Dados: Técnicas Avançadas Para Transformar Dados em Insights',
        'autor': 'Cathy Tanimura',
        'paginas': 400,
        'data_publicacao': '22/07/2022'
    },
]

# Consultar todos os livros
# Rota do o endpoint (acrescenta a url) que retornará esse resultado - localhost:5000/livros
# methods = especifica qual o tipo de método aceito nessa rota
@app.route('/livros', methods=['GET'])

# Função que retorna tudo que está na variável livros
def get_livros():
    return jsonify(livros)

# Consultar pelo id existente
# Criar a rota para acesso aos dados
# <int:id> = especifica a espera de um número inteiro e o valor passado será guardado na palavra-chave 'id'
@app.route('/livros/<int:id>', methods=['GET'])
# Recebe um id como parâmetro
def get_livros_id(id):
    # Percorre a listagem de livros
    for livro in livros:
        # Pega o id de cada livro e compara com o id passado no parâmetro da url
        if id == livro.get('id'):
            # retorna o livro correspondente ao id
            return jsonify(livro)

# Criar um novo livro
@app.route('/livros/new', methods=['POST'])
def new_livro():
    # get_json pega o conteúdo json da página
    new = request.get_json()
    # append adiciona o novo livro na lista
    livros.append(new)
    return jsonify(livros)

# Editar algum livro existente
# Rota para edição baseada no id do livro
@app.route('/livros/<int:id>/edit', methods=['PUT'])
# Função que pega o conteúdo digitado pelo usuário em JSON, pega os índices dos livros existentes e edita e exibe através desse índice
def edit_livro(id):
    # Retorna informações que o usuário inseriu para alterar na API
    livro_edit = request.get_json()
    # Faz a númeração dos índices de registros de livros
    for indice, livro in enumerate(livros):
        # Se o id do livro for igual ao id do parâmetro
        if livro.get('id') == id:
            # Ele capta o índice daquele livro (livro[0]) do id do parâmetro e faz um update com o que está na variável
            livros[indice].update(livro_edit)
            # Retorna o livro do id informado 
            return jsonify(livros[indice])

# Excluir algum livro existente
@app.route('/livros/<int:id>/delete', methods=['DELETE'])
# Função que percorre a lista, define os índices de cada registro e exclui de acordo com o índice
def delete_livro(id):
    # Enumera os livros em índices
    for indice, livro in enumerate(livros):
        # Se o id do livro for igual ao id do parâmetro
        if livro.get('id') == id:
            # Exclui o livro de acordo com o índice dele
            del livros[indice]
    # Retorna todos os livros para certificar a exclusão
    return jsonify(livros)

# Iniciando a aplicação da API
# port = porta
# host = domínio principal
# debug = para exibir o erro de forma explícita
app.run(port=5000, host='localhost', debug=True)