import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
import datetime as dt

STOCK = "GLBE"
COMPANY_NAME = "Global-E Online Ltd"
today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
before_yesterday = dt.date.today() - dt.timedelta(days=2)

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

news_api_key = os.getenv("news_api_key")
stock_api_key = os.getenv("stock_api_key")

news_api_url = os.getenv("news_api_url")
stock_api_url = os.getenv("stock_api_url")

parameters_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
    "pageSize": 3,
    "page": 1,
}
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

res_news = requests.get(url=news_api_url, params=parameters_news)
res_stock = requests.get(url=stock_api_url, params=parameters_stock)

data_news = res_news.json()["articles"]
data_stock = res_stock.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in data_stock.items()]

yesterday_stock = stock_data_list[0]["4. close"]
before_yesterday_stock = stock_data_list[1]["4. close"]

stock_delta = (
    round(
        abs(float(yesterday_stock) - float(before_yesterday_stock))
        / float(yesterday_stock)
    )
    * 100
)

change_symbol = "🔺" if stock_delta > 0 else "🔻"

news_push = [
    f'{STOCK}: {change_symbol}{abs(stock_delta)}%\nHeadline: {article["title"]}\nBrief: {article["description"]} '
    for article in data_news
]


if abs(stock_delta) >= 3:
    client = Client(account_sid, auth_token)
    for push in news_push:
        message = client.messages.create(
            body=push,
            from_="+12014688388",
            to=os.getenv("my_phone_number"),
        )
        print(message.status)
