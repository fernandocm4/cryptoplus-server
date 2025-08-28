import requests
from dotenv import load_dotenv
import os

load_dotenv()



def get_api_info():
    response = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&x_cg_demo_api_key={os.getenv('API_KEY')}")
    api_data = response.json()
    return api_data