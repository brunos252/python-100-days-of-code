# This file will need to use the DataManager, FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destionation_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = dt.datetime.now()

notification_manager = NotificationManager()

for row in sheet_data:
    flight_data = flight_search.get_flight_data(
        from_iata_code="ZAG",
        to_iata_code=row["iataCode"],
        date_from=today.strftime("%d/%m/%Y"),
        date_to=(today + dt.timedelta(days=30*6)).strftime("%d/%m/%Y"),
        nights_in_dst_from=1,
        nights_in_dst_to=14,
        flight_type="round"
    )

    if flight_data is not None and flight_data.price < row["lowestPrice [hrk]"]:
        print("found lower!")
        notification_manager.send_email(flight_data=flight_data)
