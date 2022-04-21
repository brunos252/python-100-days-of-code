"""
Check whether ISS is overhead and whether it is nighttime
at my location, then send me an email to let me know
"""
import time

import requests
import smtplib
from datetime import datetime

MY_LAT = 45.815010
MY_LNG = 15.981919

MY_EMAIL = "*****@gmail.com"
MY_PASSWORD = "******"

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    is_close = False
    if abs(MY_LAT - iss_latitude) < 5 and abs(MY_LNG - iss_longitude) < 5:
        is_close = True

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 1
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 1

    time_now = datetime.now().hour

    is_night = False
    if time_now > sunset or time_now < sunrise:
        is_night = True

    if is_close and is_night:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="bruno.sacaric@gmail.com",
                msg=f"Oh Boy, the ISS is overhead"
            )

    time.sleep(60)
