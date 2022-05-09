import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5dc350f13d776fa1368ca595dbdf4665/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destionation_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.destination_data = response.json()["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
