from flask import request,jsonify
from functools import wraps
import api, jwt, os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def authRoute(data):
    @wraps(data)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify(message="Token é necessário!"), 403
        
        parts = auth_header.split()
        if parts[0].lower() != 'bearer' or len(parts) != 2:
            return jsonify(message="Cabeçalho de autorização mal formatado!"), 401
        token = parts[1]

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
   
        except jwt.ExpiredSignatureError:
            return jsonify(message="Token expirado! Faça o login novamente."), 401
        except jwt.InvalidTokenError:
            return jsonify(message="Token inválido"), 403
        return data(*args, **kwargs)
    return decorated