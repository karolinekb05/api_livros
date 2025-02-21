## Projeto API CRUD - Livros

Nesse repositório contém uma API com CRUD sobre livros.

Para criar o servidor da API utilizei o Flask, para o conteúdo usei a biblioteca jsonify e para as requisições usei a biblioteca request. Configurada para rodar localmente na porta 5000 e no modo debug.

#### Endpoints:

GET /livros = Acessa a listagem com todos os livros

GET /livros/id = Acessa o livro do id especificado

POST /livros/id/new = Cria um novo registro de livro na listagem com formato json

PUT /livros/id/edit = Edita um registro de livro existente com formato json

DELETE /livros/id/delete = Deleta o livro do id especificado
