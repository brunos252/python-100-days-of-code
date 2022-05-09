import smtplib
from flight_data import FlightData

MY_EMAIL = "*****@gmail.com"
MY_PASSWORD = "*****"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(self, flight_data: FlightData):
        message = "Subject: Low price alert\n\n" \
                  f"There is a low budget flight available! Only {flight_data.price} kn to fly from " \
                  f"{flight_data.from_city}-{flight_data.from_iata_code} to " \
                  f"{flight_data.to_city}-{flight_data.to_iata_code}, " \
                  f"from {flight_data.out_date}."

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="****@gmail.com", msg=message)

