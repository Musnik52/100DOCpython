from flight_data import FlightData
import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

origin = os.getenv("origin_location")
tequila_api_url = os.getenv("tequila_api_url")
tequila_api_key = os.getenv("tequila_api_key")


class FlightSearch:
    def __init__(self):
        self.today = dt.date.today()
        pass

    def iata_coder(self, city):
        url = f"{tequila_api_url}/locations/query"
        data = {"term": city, "location_types": "city"}
        header = {"apikey": tequila_api_key}
        res = requests.get(url=url, params=data, headers=header)
        iata_code = res.json()["locations"][0]["code"]
        return iata_code

    def get_flights(self, city):
        data = {
            "fly_from": origin,
            "fly_to": city,
            "date_from": self.today,
            "date_to": self.today + dt.timedelta(days=180),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }
        header = {"apikey": tequila_api_key}
        res = requests.get(
            url=f"{tequila_api_url}/v2/search", headers=header, params=data
        )

        try:
            data_json = res.json()["data"][0]
        except IndexError:
            try:
                data["max_stopovers"] = 1
                res = requests.get(
                    url=f"{tequila_api_url}/v2/search", headers=header, params=data
                )
                data_json = res.json()["data"][0]
                flight_data = FlightData(
                    price=data_json["price"],
                    currency=data["curr"],
                    origin_city=data_json["route"][0]["cityFrom"],
                    origin_airport=data_json["route"][0]["flyFrom"],
                    destination_city=data_json["route"][1]["cityTo"],
                    destination_airport=data_json["route"][1]["flyTo"],
                    departure_date=data_json["route"][0]["local_departure"].split("T")[
                        0
                    ],
                    return_date=data_json["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=["route"][0]["cityTo"],
                )
                return flight_data
            except:
                return None
        else:
            flight_data = FlightData(
                price=data_json["price"],
                currency=data["curr"],
                origin_city=data_json["route"][0]["cityFrom"],
                origin_airport=data_json["route"][0]["flyFrom"],
                destination_city=data_json["route"][0]["cityTo"],
                destination_airport=data_json["route"][0]["flyTo"],
                departure_date=data_json["route"][0]["local_departure"].split("T")[0],
                return_date=data_json["route"][1]["local_departure"].split("T")[0],
            )
            # print(f'{flight_data.destination_city}: {flight_data.price} {data['curr']}')
        return flight_data
