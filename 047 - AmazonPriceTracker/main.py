import requests
import os
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("my_email")
my_password = os.getenv("my_password")


target_price = 18
item_url = "https://www.amazon.com/House-Leaves-Mark-Z-Danielewski/dp/0375703764/ref=tmm_pap_swatch_0?_encoding=UTF8&sr=8-1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7",
}

res = requests.get(url=item_url, headers=header)
soup = BeautifulSoup(res.text, "html.parser")
current_peice = float(
    soup.find(class_="a-size-base a-color-price a-color-price").getText()[2:]
)

if current_peice < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="musnik52@gmail.com",
            msg=f"Subject:PriceDrop!\n\n{item_url} price dropped! currently ${current_peice}.".encode(
                "utf-8"
            ),
        )
