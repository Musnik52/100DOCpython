import requests
import os
from dotenv import load_dotenv

load_dotenv()

sheety_users_url = f'{os.getenv("sheety_url")}/users'
secret_token = os.getenv("secret_token")


def insert_data(data):
    header_token = {"Authorization": f"Bearer {secret_token}"}
    sheety_res = requests.post(url=sheety_users_url, headers=header_token, json=data)
