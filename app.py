from flask import Flask, jsonify
from config import config
import os
from database.config import db
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
origins = os.environ.get('CORS_ORIGINS', '')
origins_list = [origin.strip() for origin in origins.split(',') if origin.strip()]
CORS(app, origins=origins_list)

config(app)
app.run(debug=True)