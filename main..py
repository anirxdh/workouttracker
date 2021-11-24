import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = "39584c03"
APP_KEY = "1cd218c429d80d6f00dc8c2c2727b81e"
APP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/c2f32a04637be0abc9f7c657b41b81dd/myWorkouts/workouts"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id" : "0",

}
exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": "65",
    "height_cm": "180",
    "age": "20"
}
response = requests.post(APP_ENDPOINT,json= parameters, headers= HEADERS )
result = response.json()
print(result)

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs ,auth=(
      "Anirudh",
      "342001",
  )
                               )

print(sheet_response.text)