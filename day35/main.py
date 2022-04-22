"""
App for sending SMS warning when it is going to rain that day
"""

import requests
from twilio.rest import Client

api_key = "***"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = ""
auth_token = ""

MY_LAT = 45.815010
MY_LNG = 15.981919

parameters = {
    "lat": MY_LAT,
    "long": MY_LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

will_rain = False

next_12_hours = weather_data["hourly"][:12]
for hour_data in next_12_hours:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today, bring an umbrella",
        from="",
        to=""
    )
    print(message.status)
