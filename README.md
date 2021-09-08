# Movimentações Financeiras

### Como rodar projeto:
 - `docker-compose up` ou `sudo docker-compose up`

### Acessando página principal no navegador:
- abrir `localhost:8000`, inserir arquivo `CNAB.txt` e enviar.

### API:
Listagem de movimentações:
  - `GET` para `localhost:8000/api/v1/movimentacoes`
Inserção de movimentações:
  - `POST` para localhost:8000/api/v1/movimentacoes, enviando via `form-data` com key `cnab_file`(tipo arquivo) com o valor sendo o arquivo.

Postman collection para auxiliar nos testes da API: `desafio-dev.postman_collection.json`
