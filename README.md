# Movimentações Financeiras


### Rodando projeto com docker-compose:
 - `docker-compose up` ou `sudo docker-compose up`

### Preparar ambiente local:
 - `pip install pipenv`
 - `pipenv install`
 - `pipenv run ./manage.py migrate`

### Rodar testes localmente
 - `pipenv run ./manage.py test`

### Rodar projeto localmente
 - `pipenv run ./manage.py runserver`

## Acessando via navegador:
- abrir `localhost:8000`, inserir arquivo `CNAB.txt`, enviar e ver as movimentações inseridas sendo listadas na tela.

## Uso da API:
### Inserção de movimentações:
  - `POST` para localhost:8000/api/v1/movimentacoes, enviando via `form-data` com key `cnab_file`(tipo arquivo) com o valor sendo o arquivo.
### Listagem de movimentações:
  - `GET` para `localhost:8000/api/v1/movimentacoes`
Exemplo de resultado:
```
{
    "transactions": [
        {
            "id": 1,
            "tipo": "Financiamento",
            "data_e_hora": "01/03/2019 18:34:53",
            "valor": "-142.00",
            "cpf": "09620676017",
            "cartao": "4753****3153",
            "dono_da_loja": "JOÃO MACEDO",
            "nome_loja": "BAR DO JOÃO",
            "saldo_em_conta": "-142.00"
        },
        {
            "id": 5,
            "tipo": "Débito",
            "data_e_hora": "02/03/2019 02:30:00",
            "valor": "152.00",
            "cpf": "09620676017",
            "cartao": "1234****7890",
            "dono_da_loja": "JOÃO MACEDO",
            "nome_loja": "BAR DO JOÃO",
            "saldo_em_conta": "10.00"
        }
    ]
}
```
## Postman collection para auxiliar nos testes da API:
 - `desafio-dev.postman_collection.json`
