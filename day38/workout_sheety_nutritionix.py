import requests
from datetime import datetime

APP_ID = "****"
API_KEY = "****"

nutritionix_base_api = "https://trackapi.nutritionix.com"
exercise_endpoint = "/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/<myID>/myWorkouts/workouts"

query = input("Tell me which exercises you did: ")

exercise_body = {
    "query": query,
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 185,
    "age": 24
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=f"{nutritionix_base_api}{exercise_endpoint}", json=exercise_body, headers=headers)
response.raise_for_status()
result = response.json()
today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

    # No Authentication
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        # auth=(YOUR USERNAME, YOUR PASSWORD)
    )

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": "Bearer YOUR_TOKEN"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )