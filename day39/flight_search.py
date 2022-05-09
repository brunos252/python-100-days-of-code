import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "*****"

TEQUILA_LOCATIONS_ENDPOINT = "/locations/query"
TEQUILA_SEARCH_ENDPOINT = "/v2/search"

headers = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_destination_code(self, city_name):
        params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}{TEQUILA_LOCATIONS_ENDPOINT}", params=params, headers=headers)
        code = response.json()["locations"][0]["code"]

        return code

    def get_flight_data(
        self,
        from_iata_code,
        to_iata_code,
        date_from,
        date_to,
        nights_in_dst_from,
        nights_in_dst_to,
        flight_type="round"
    ):
        # fly_to can take multiple dests
        params = {
            "fly_from": from_iata_code,
            "fly_to": to_iata_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": flight_type,
            "one_for_city": 1,
            "curr": "HRK",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}{TEQUILA_SEARCH_ENDPOINT}", params=params, headers=headers)

        if not response.json()["data"]:
            return None

        data = response.json()["data"][0]
        print(data["cityTo"], data["price"])
        return FlightData(
            price=data["price"],
            from_city=data["cityFrom"],
            from_iata_code=data["flyFrom"],
            to_city=data["cityTo"],
            to_iata_code=data["flyTo"],
            out_date=data["local_departure"][:10],
        )
