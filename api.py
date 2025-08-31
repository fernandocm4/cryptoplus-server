import requests
from dotenv import load_dotenv
import os

load_dotenv()



def get_api_info():
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&x_cg_demo_api_key={os.getenv('API_KEY')}")
    api_data = response.json()
    return api_data

def get_info_of_a_coin(moeda):
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&ids={moeda}&x_cg_demo_api_key={os.getenv('API_KEY')}")
    api_data = response.json()
    return api_data

def get_days_prices(moeda, days):
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/{moeda}/market_chart?vs_currency=brl&days={days}&x_cg_demo_api_key={os.getenv('API_KEY')}")
    api_data = response.json()
    return api_data