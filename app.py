from flask import Flask, request, jsonify
from config import config
from flask_status import FlaskStatus
import os
import requests
from database.config import db
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
flask_status = FlaskStatus(app, url='/status')
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])


def check_database():
    return True

def check_coin_gecko():
    if (requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&x_cg_demo_api_key={os.getenv('API_KEY')}")):
        return True
    else:
        return False
    


flask_status.add_field("database", check_database)
flask_status.add_field("coinGecko", check_coin_gecko)

config(app)
app.run(debug=True)