from flask import Blueprint, request, jsonify
from database.models.coin import Coin
import api
from auth.auth import authRoute

coins_route = Blueprint('coins', __name__)

@coins_route.route('/importar', methods=['POST'])
@authRoute
def save_api_data():
    data = api.get_api_info()

    for item in data:
        
        Coin.create(
            name = item['name'],
            symbol = item['symbol'],
            image = item['image'],
            current_price = item['current_price']
        )
    return jsonify(message="Success"), 201
        

@coins_route.route('/importar')
@authRoute
def get_database_api_data():
    coins = Coin.select()
    data = []

    for coin in coins:
        coin_object = {
            'name': coin.name,
            'symbol': coin.symbol,
            'image': coin.image,
            'current_price': coin.current_price,
            'save_data': coin.save_data
        }

        data.append(coin_object)
    
    return jsonify(data), 200


@coins_route.route('/indicadores')
@authRoute
def get_indicators():

    api_data = api.get_api_info()
    data = []

    for item in api_data:
        filtered_item = {
            'image': item['image'],
            'name': item['name'],
            'high_24h': item['high_24h'],
            'low_24h': item['low_24h'],
            'price_change_percentage_24h': item['price_change_percentage_24h'],
            'ath': item['ath'],
            'atl': item['atl']
        }

        data.append(filtered_item)
    
    return jsonify(data), 200


@coins_route.route('/indicadores/<string:coin_id>')
@authRoute
def get_indicators_for_a_coin(coin_id):
    
    days = request.args.get('days', 7)
    api_data_prices = api.get_days_prices(coin_id, days)
    api_data = api.get_info_of_a_coin(coin_id)
    data = api_data_prices['prices']
    prices = []
    filtered_item = {}
    
    try:
        days = int(days)
    except (ValueError, TypeError):
        return jsonify(message="O parâmetro 'days' precisa ser um número inteiro")
    
    for timestamp, price in data:
        prices.append(price)

    average = sum(prices)/len(prices)

    response_average = round(average, 2)


    price_length = len(prices)

    price_change_percentage_x_d = ((prices[price_length-1] - prices[0]))

    price_change_percentage_x_d = (price_change_percentage_x_d/prices[0])*100

    price_change_percentage_x_d = round(price_change_percentage_x_d, 2)

    x_time_high = max(prices)
    x_time_high = round(x_time_high, 2)
    
    x_time_low = min(prices)
    x_time_low = round(x_time_low, 2)
    for item in api_data:


        filtered_item = {
            'price_change_percentage_x_d': price_change_percentage_x_d,
            'average': response_average,
            'x_time_high': x_time_high,
            'x_time_low': x_time_low,
            'average_range_days': days,
            'current_price': item['current_price']
        }

    
    return jsonify(filtered_item), 200