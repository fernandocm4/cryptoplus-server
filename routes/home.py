from flask import Blueprint, jsonify
import api


home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    api_data = api.get_api_info()
    return api_data

