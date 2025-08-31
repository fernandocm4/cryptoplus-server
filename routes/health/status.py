from flask import Blueprint, jsonify
import requests
import os
from dotenv import load_dotenv
import psutil

load_dotenv()

status_route = Blueprint('status', __name__)

@status_route.route('/status')
def check_health():

    server_data = check_server()
    api_data = api_check()
    
    
    return jsonify({
        'Server': server_data,
        'Api': api_data
    })


def check_server():
    return {
        'cpu_percent': psutil.cpu_percent(),
        'memory_percent': psutil.virtual_memory().percent
    }
    


def api_check():
    try:

        api_key = os.getenv('API_KEY')

        if not api_key:
            return {
                'API_COINGECKO': 'CHAVE DA API NÃO DEFINIDA'
            }
        
        response = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&x_cg_demo_api_key={os.getenv('API_KEY')}")

        if (response.status_code == 200):
            return {
                'API_COINGECKO': 'OK'
            }
        else:
            return {
                'API_COINGECKO': 'ERRO AO FAZER A REQUISIÇÃO NA API'
            }
    
    except Exception as e:
        return {
            'API_COINGECKO': f'Erro: {e}'
        }