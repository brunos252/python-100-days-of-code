class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, from_city, from_iata_code, to_city, to_iata_code, out_date):
        self.price = float(price)
        self.from_city = from_city
        self.from_iata_code = from_iata_code
        self.to_city = to_city
        self.to_iata_code = to_iata_code
        self.out_date = out_date
