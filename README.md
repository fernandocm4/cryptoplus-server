
# Crypto+

Esta é a documentação para a API de cotação de criptomoedas **Crypto+**.

## Sobre o Projeto

Este projeto é uma API REST desenvolvida em Python 3.12+ e Flask. Ela tem como objetivo visualizar informações sobre a cotação das criptomoedas mais conhecidas do mercado atualmente. A aplicação completa está hospedada e pode ser testada no link.
* [Crypto+](https://sysmaia.com.br)

## Requisitos

Antes de começar, certifique-se de ter instalado:
* Python 3.12 ou superior
* Pip (gerenciador de pacotes do Python)
* Banco de dados Postgresql 16.9 ou superior

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone git@github.com:fernandocm4/cryptoplus-server.git
    cd cryptoplus-server
    git checkout dev
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o ambiente**
    1. **Copie o conteúdo do arquivo `.env.example` para um novo arquivo chamado `.env`:**

    ```bash
    cp .env.exemple .env
    ```

    2. **Abra o interpretador Python no seu terminal:**
    ```bash
    python3 #ou python para windows

    #execute esse comandos
    import secrets
    secrets.token_hex(16)
    ```
    Copie a chave gerada e cole no seu arquivo `.env` em `SECRET_KEY`

    3. **Obtenha uma chave de api da [Coingecko](https://www.coingecko.com/pt-br/api) e cole em** `API_KEY`

    4. **Cole em** `DATABASE_URL` **a url do banco com as suas credenciais:**
    ```bash
    postgresql://seu_usuário:sua_senha@seu_host:5432/seu_banco
    ```

5.  **Execute a aplicação:**
    ```bash
    python3 app.py #ou python app.py para windows
    ```
    A API estará rodando em `http://127.0.0.1:5000` por padrão.

* **Esta API pode ser utilizada com frontend disponível no repositório:** https://github.com/fernandocm4/viteapp

---

## Endpoints da API

Esta seção é crucial. Descreva cada endpoint de forma clara, incluindo o método HTTP, a URL, a descrição, os parâmetros da requisição e a estrutura da resposta.

### 1. `GET /`

* **Descrição:** Retorna a lista de 100 das criptomoedas chamadas pela api.
* **Método:** `GET`
* **URL:** `http://127.0.0.1:5000/`
* **Parâmetros da requisição:** Nenhum.
* **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <seu_jwt_token>
    ```
* **Exemplo de resposta (Sucesso - 200 OK):**
    ```json
    [
        {
            "current_price": 590484,
            "image": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
            "name": "Bitcoin",
            "symbol": "btc"
        },
        {
            "current_price": 23864,
            "image": "https://coin-images.coingecko.com/coins/images/279/large/ethereum.png?1696501628",
            "name": "Ethereum",
            "symbol": "eth"
        }
    ]
    ```

### 2. `GET /importar`

* **Descrição:** Retorna os dados de criptomoedas salvos no banco de dados.
* **Método:** `GET`
* **URL:** `http://127.0.0.1:5000/importar`
* **Parâmetros da requisição:** Nenhum
* **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <seu_jwt_token>
    ```
* **Exemplo de resposta (Sucesso - 200 OK):**
    ```json
    [
        {
            "current_price": "112843.0000",
            "image": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
            "name": "Bitcoin",
            "save_data": "Thu, 28 Aug 2025 16:36:08 GMT",
            "symbol": "btc"
        },
        {
            "current_price": "4513.9600",
            "image": "https://coin-images.coingecko.com/coins/images/279/large/ethereum.png?1696501628",
            "name": "Ethereum",
            "save_data": "Thu, 28 Aug 2025 16:36:08 GMT",
            "symbol": "eth"
        }
    ]
    ```
* **Exemplo de resposta (Erro - 403 FORBIDDEN):**
    ```json
    {
        "message": "Token é necessário!"
    }
    ```

* **Exemplo de resposta (Erro - 403 FORBIDDEN):**
    ```json
    {
        "message": "Token inválido"
    }
    ```
* **Exemplo de resposta (Erro - 401 UNAUTHORIZED):**
    ```json
    {
        "message": "Cabeçalho de autorização mal formatado!"
    }
    ```



### 2. `POST /importar`

* **Descrição:** Salva os dados de criptomoedas no banco de dados.
* **Método:** `POST`
* **URL:** `http://127.0.0.1:5000/importar`
* **Parâmetros da requisição:** Nenhum
* **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <seu_jwt_token>
    ```
* **Exemplo de resposta (Sucesso - 201 CREATED):**
    ```json
    {
        "message": "Success"
    }
    ```
* **Exemplo de resposta (Erro - 403 FORBIDDEN):**
    ```json
    {
        "message": "Token é necessário!"
    }
    ```

* **Exemplo de resposta (Erro - 403 FORBIDDEN):**
    ```json
    {
        "message": "Token inválido"
    }
    ```
* **Exemplo de resposta (Erro - 401 UNAUTHORIZED):**
    ```json
    {
        "message": "Cabeçalho de autorização mal formatado!"
    }
    ```








### 3. `GET /indicadores`

* **Descrição:** Retorna informações relevantes das criptomoedas, como o maior preço atingido em 24h.
* **Método:** `GET`
* **URL:** `http://127.0.0.1:5000/indicadores`
* **Parâmetros da requisição:** Nenhum
* **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <seu_jwt_token>
    ```
* **Exemplo de resposta (Sucesso - 200 OK):**
    ```json
    [
        {
            "ath": 685780,
            "atl": 149.66,
            "high_24h": 598542,
            "image": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
            "low_24h": 582953,
            "name": "Bitcoin",
            "price_change_percentage_24h": 0.42213
        },
        {
            "ath": 26931,
            "atl": 1.69,
            "high_24h": 24416,
            "image": "https://coin-images.coingecko.com/coins/images/279/large/ethereum.png?1696501628",
            "low_24h": 23734,
            "name": "Ethereum",
            "price_change_percentage_24h": -1.81752
        }
    ]
    ```



### 4. `GET /indicadores/<id>`

* **Descrição:** Retorna informações relevantes de apenas uma criptomoeda.
* **Método:** `GET`
* **URL:** `http://127.0.0.1:5000/indicadores/<id>`
* **Parâmetros da URL:**
    * `id` (string, obrigatório): O nome da moeda em lowercase.
* **Cabeçalho de Autorização:**
    ```
    Authorization: Bearer <seu_jwt_token>
    ```

#### Parâmetros da Requisição (Query Params)

* **`days`** (inteiro, opcional): O número de dias atrás a partir da data atual a se capturar dados.
    * **Valor padrão:** `7`

#### Exemplo de Uso
* `GET` : `http://127.0.0.1:5000/indicadores/bitcoin?days=30`
* **Exemplo de resposta (Sucesso - 200 OK):**
    ```json
    {
        "average": 597790.81,
        "average_range_days": 7,
        "current_price": 591011,
        "price_change_percentage_x_d": -2.32,
        "x_time_high": 614182.01,
        "x_time_low": 583185.23
    }
    ```


### 5. `POST /register`

* **Descrição:** Cria um novo usuário.
* **Método:** `POST`
* **URL:** `http://127.0.0.1:5000/register`
* **Corpo da requisição (JSON):**
    ```json
    {
        "username": "Amanda",
        "password": "1234"
    }
    ```
* **Exemplo de resposta (Sucesso - 201 CREATED):**
    ```json
    {
        "message": "Usuário criado com sucesso"
    }
    ```

### 5. `POST /login`

* **Descrição:** Cria um novo `jwt`, com expiração em 30 minutos, a partir do `username` e `password` de um usuário cadastrado no banco de dados.
* **Método:** `POST`
* **URL:** `http://127.0.0.1:5000/login`
* **Corpo da requisição (JSON):**
    ```json
    {
        "username": "Amanda",
        "password": "1234"
    }
    ```
* **Exemplo de resposta (Sucesso - 200 OK):**
    ```json
    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZnVsYW5vZGV0YWwiLCJleHAiOjE3NTY3MzQwNDF9.Hd4TYKyrh0NKxey9MtAQ2JhpHNtm4E_4ahOyoncc6Tc"
    }
    ```

* **Exemplo de resposta (Erro - 401 UNAUTHORIZED):**
    ```json
    {
        "message": "Verifique suas credenciais!"
    }
    ```


### 6. `GET /status`

* **Descrição:** Retorna informações sobre a API.
* **Método:** `GET`
* **URL:** `http://127.0.0.1:5000/status`
* **Parâmetros da requisição:** Nenhum.
* **Exemplo de resposta (Sucesso - 200 OK):**
    ```json
    [
        "Api": {
        "API_COINGECKO": "OK"
        },
        "Server": {
            "cpu_percent": 0.0,
            "memory_percent": 37.2
        }
    ]
---


## Autenticação

Esta API usa **Token JWT** para autenticação. Para acessar os endpoints protegidos, você deve incluir o token no cabeçalho `Authorization` da sua requisição, no formato:

`Authorization: Bearer <seu_token>`

---

## Tecnologias Utilizadas

* **Python**
* **Flask** - Framework web
* **Peewee** - ORM para banco de dados
* **Postgresql** - Banco de dados
* **Coingecko** -  API de dados de criptomoedas

## Autor

* **Fernando Candido** - [Perfil github](https://github.com/fernandocm4)
* **Email** - [maiafernando2611@gmail.com](mailto:maiafernando2611@gmail.com)