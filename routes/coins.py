from flask import Blueprint
from database.models.coin import Coin
import api

coins_route = Blueprint('coins', __name__)


@coins_route.route('/importar')
def save_api_data():
    data = api.get_api_info()

    for item in data:
        
        Coin.create(
            name = item['name'],
            symbol = item['symbol'],
            image = item['image'],
            current_price = item['current_price']
        )
    return {
        "status_code":200
    }

