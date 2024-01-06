import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

my_lat = os.getenv("my_lat")
my_lng = os.getenv("my_lng")
my_api_key = os.getenv("my_api_key")
api_url = os.getenv("api_url")
parameters = {"lat": my_lat, "lon": my_lng, "cnt": 4, "appid": my_api_key}

res = requests.get(url=api_url, params=parameters)
data = res.json()

is_raining = False
for i in data["list"]:
    weather_cond_id = i["weather"][0]["id"]
    is_raining = True if weather_cond_id < 700 else is_raining
    # code_ids below 700 mean bad weather, according to the doc.

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Bring an ☔" if is_raining else "No ☔ needed",
    from_="+12014688388",
    to=os.getenv("my_phone_number"),
)
print(message.status)
