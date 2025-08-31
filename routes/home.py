from flask import Blueprint, jsonify, request
import api
import jwt
from dotenv import load_dotenv
import os
from auth.auth import authRoute

home_route = Blueprint('home', __name__)
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

@home_route.route('/', methods=['GET'])
@authRoute
def home():
    api_data = api.get_api_info()
    data = []

    for item in api_data:
        filtered_item = {
            'name': item['name'],
            'current_price': item['current_price'],
            'symbol': item['symbol'],
            'image': item['image']
        }

        data.append(filtered_item)

    return data





