import requests

api_url = "https://opentdb.com/api.php"
parameters = {"amount": 10, "type": "boolean"}
res = requests.get(api_url, params=parameters)
question_data = res.json()["results"]
