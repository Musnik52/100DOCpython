import requests
import os
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

sheety_url = os.getenv("sheety_url")
nutri_url = os.getenv("nutri_url")
nutri_api_key = os.getenv("nutri_api_key")
nutri_app_id = os.getenv("nutri_app_id")
security_token = os.getenv("security_token")

today = dt.datetime.now()

nutri_parameters = {
    "query": input("What did you do today?\n"),
    "weight_kg": 85,
    "height_cm": 183,
    "age": 32,
}

header = {"x-app-id": nutri_app_id, "x-app-key": nutri_api_key}

res_nutri = requests.post(url=nutri_url, json=nutri_parameters, headers=header)
exercises = res_nutri.json()["exercises"]

for activity in exercises:
    sheety_parameters = {
        "workout": {
            "date": str(today.date().strftime("%d/%m/%Y")),
            "time": str(today.time().strftime("%H:%M:%S")),
            "exercise": activity["name"].title(),
            "duration": round(activity["duration_min"]),
            "calories": round(activity["nf_calories"]),
        }
    }
    header_token = {"Authorization": f"Bearer {security_token}"}

    # res_sheety = requests.get(url=sheety_url)
    res_sheety = requests.post(
        url=sheety_url, json=sheety_parameters, headers=header_token
    )
    print(res_sheety.text)
