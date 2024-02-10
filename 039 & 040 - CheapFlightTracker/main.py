import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv()


secret_token = os.getenv("secret_token")

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheety_data = data_manager.get_data()

if not sheety_data[0]["iataCode"]:
    for destination in sheety_data:
        destination["iataCode"] = flight_search.iata_coder(destination["city"])
    data_manager.destinations = sheety_data
    data_manager.update_iata_code()

for destination in sheety_data:
    flight_data = flight_search.get_flights(destination["iataCode"])
    if flight_data and (int(flight_data.price) <= int(destination["lowestPrice"])):
        msg = f"$ - Only {flight_data.price}{flight_data.currency} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}. Dates: {flight_data.departure_date} till {flight_data.return_date}"
        notification_manager.send_msg(msg)
