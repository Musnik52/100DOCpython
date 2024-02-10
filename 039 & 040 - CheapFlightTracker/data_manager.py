import requests
import os
from dotenv import load_dotenv

load_dotenv()

sheety_url = os.getenv("sheety_url")


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destinations = ""

    def get_data(self):
        res_sheety = requests.get(url=sheety_url)
        self.destinations = res_sheety.json()["prices"]
        return self.destinations
    
    def update_iata_code(self):
        for city in self.destinations:
            iata_codes = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_res = requests.put(url=f"{sheety_url}/{city["id"]}", json=iata_codes)
            print(put_res.text)
