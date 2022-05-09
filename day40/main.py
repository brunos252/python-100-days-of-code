"""
Idea is to make day39 into a service, storing subscribers' emails, and sending them messages
- incomplete, but easy to complete
"""

import requests

SHEETY_ENDPOINT_POST = "https://api.sheety.co/5dc350f13d776fa1368ca595dbdf4665/flightDeals/users"

print("Welcome to Bruno's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
if email == input("Type your email again. "):
  print("You're in the club.")
  data = {
    "price": {
      "first name": first_name,
      "last name": last_name,
      "email": email,
    }
  }
  response = requests.post(
    url=SHEETY_ENDPOINT_POST,
    json=data
  )
  print(response.text)