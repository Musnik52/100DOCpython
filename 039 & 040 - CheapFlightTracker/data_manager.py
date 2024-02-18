import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

sheety_prices_url = f'{os.getenv("sheety_url")}/prices'
sheety_users_url = f'{os.getenv("sheety_url")}/users'
secret_token = os.getenv("secret_token")

class DataManager:

    def __init__(self):
        self.destinations = ""
        self.header_token = {"Authorization": f"Bearer {secret_token}"}

    def get_data(self):
        res_sheety = requests.get(url=sheety_prices_url, headers=self.header_token)
        self.destinations = res_sheety.json()["prices"]
        return self.destinations
    
    def update_iata_code(self):
        for city in self.destinations:
            iata_codes = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_res = requests.put(url=f"{sheety_prices_url}/{city["id"]}", json=iata_codes, headers=self.header_token)
            print(put_res.text)
    
    def get_contacts(self):
        res_sheety = requests.get(url=sheety_users_url, headers=self.header_token)
        return res_sheety.json()['users']
