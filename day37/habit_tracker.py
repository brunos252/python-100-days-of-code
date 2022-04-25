import requests
import datetime as dt

USERNAME = "brunci"
TOKEN = "kpajgoropqw9retq"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# ----------------------register user---------------------
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ----------------------create graph----------------------
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPHID,
#     "name": "Running Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ----------------------post pixel------------------------
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = dt.datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.0",
}

requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# ----------------------update pixel----------------------

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)


# -----------------------delete pixel---------------------

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
