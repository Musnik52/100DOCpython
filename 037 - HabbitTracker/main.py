import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

token = os.getenv("token")
username = os.getenv("user_name")
url_user = os.getenv("url_user")

## user_creation:
params_user = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# res = requests.post(url=url_user, json=params_user)
# print(res.text)

## graph_creation:
url_graph = f"{url_user}/{params_user['username']}/graphs"
params_graph = {
    "id": "graph1",
    "name": "reading",
    "unit": "pages",
    "type": "int",
    "color": "momiji",
}
header = {"X-USER-TOKEN": token}
# res = requests.post(url=url_graph, json=params_graph, headers=header)
# print(res.text)

## Pixel Post
today = dt.datetime.now()
today_formatted = today.strftime("%Y%m%d")
url_pixel_post = f"{url_user}/{params_user['username']}/graphs/{params_graph['id']}"
params_pixel_post = {
    "date": f"{today_formatted}",
    "quantity": input("How many pages did you read today? "),
}
res = requests.post(url=url_pixel_post, json=params_pixel_post, headers=header)
print(res.text)

## Pixel Put
# url_pixel_put = f"{url_user}/{params_user['username']}/graphs/{params_graph['id']}/{today_formatted}"
# params_pixel_put = {
#     "quantity": "3",
# }
# res = requests.put(url=url_pixel_put, json=params_pixel_put, headers=header)
# print(res.text)

## Pixel Delete
# url_pixel_delete = f"{url_user}/{params_user['username']}/graphs/{params_graph['id']}/{today_formatted}"
# res = requests.delete(url=url_pixel_delete, headers=header)
# print(res.text)
