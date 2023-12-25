import requests
import datetime as dt
import smtplib
import time

my_lat = 32.083549
my_lng = 34.815498
my_email = "musnik52coding@gmail.com"
my_password = "mxoh lypu mhxe syqy"

def is_iss_overhead():
    api_url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url=api_url)
    data = res.json()

    iss_lng = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    return my_lat - 5 <= iss_lat <= my_lat + 5 and my_lng - 5 <= iss_lng <= my_lng + 5


def is_night():
    parameters = {"lat": my_lat, "lng": my_lng, "formatted": 0}
    api_url = "https://api.sunrise-sunset.org/json"
    res = requests.get(url=api_url, params=parameters)
    data = res.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])  # 04
    sunset_hour = int(sunset.split("T")[1].split(":")[0])  # 14
    now = dt.datetime.now()
    return now.hour <= sunrise_hour or now.hour >= sunset_hour

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # SECURITY ENCODING!
            connection.login(user=my_email, password=my_password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:LOOK UP!\n\nISS is overhead!",
            )