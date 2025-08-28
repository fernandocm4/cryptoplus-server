import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from flask import request, jsonify, Blueprint
from database.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash


auth_route = Blueprint('auth', __name__)
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

@auth_route.route('/register', methods=["POST"])
def auth():
    data = request.json
    pwd = data['password']

    User.create(
        name = data['name'],
        username = data['username'],
        password = generate_password_hash(pwd, method='pbkdf2:sha256')
    )
    return jsonify(message="Usuário criado com sucesso"), 201



@auth_route.route('/login', methods=["POST"])
def login():
    data = request.get_json()

    try:
        user = User.get(User.username == data['username'])
    except:
        return jsonify(message="Username não encontrado!"), 404

    if not data:
        return jsonify(message="Dados de login não fornecidos!"), 400
    
    if "username" not in data or "password" not in data:
        return jsonify(message="Campos 'username' e 'password' são obrigatórios"), 400
    
    if data["username"] == user.username and check_password_hash(user.password, data['password']) == True:
        token = jwt.encode(
            {"user": data["username"], "exp": datetime.now(timezone.utc)+timedelta(minutes=30)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify(token=token)
    return jsonify(message='Verifique suas credenciais!'), 401


@auth_route.route('/protected', methods=["GET"])
def protected():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify(message="Token é necessário!"), 403
    
    parts = auth_header.split()
    if parts[0].lower() != 'baerer' or len(parts) != 2:
        return jsonify(message="Cabeçalho de autorização mal formatado!"), 401
    token = parts[1]

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify(message=f"Bem-vindo, {decoded['user']}!")
    except jwt.ExpiredSignatureError:
        return jsonify(message="Token expirado! Faça o login novamente."), 401
    except jwt.InvalidTokenError:
        return jsonify(message="Token inválido"), 403