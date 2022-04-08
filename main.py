import requests
from datetime import datetime

# import os
# API_KEY_NUTRITION = #SUA API Key
# CRIAR VARIAVES NO SISTEMA PARA SEGURANÇA, É NECESSARIO DECLARAR NO WINDOWS

API_KEY_NUTRITION = #SUA Chave API
API_ID_NUTRITION = # Seu API ID
TODAY = datetime.now().strftime("%d/%m/%Y")
HOUR = datetime.now().strftime("%X")
SHEETY_ENDPOINT = 'https://api.sheety.co/613d9b544f653b8e31d7cc8904f068e8/myWorkouts/workouts'
SHEETY_USER = "Day38"
SHEETY_PASSWORD = "0123456789"

# ------------------------------------------------------------------------------------------------

nutrition_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-key": API_KEY_NUTRITION,
    "x-app-id": API_ID_NUTRITION,
}
entry = input("Tell me which exercises you did: ")
#example: I ran 3 miles and walked 2 km
params = {
    "query": entry,
    "gender": "female",
    "weight_kg": 92.0,
    "height_cm": 170.00,
    "age": 26,
}

response = requests.post(nutrition_endpoint, json=params, headers=headers)
result = response.json()
print(result)

# ------------------------------------------------------------------------------------------

for row in result['exercises']:
    params_add = {
        "workout": {
            "date": TODAY,
            "time": HOUR,
            "exercise": row['name'].title(),
            "duration": row['duration_min'],
            "calories": row['nf_calories'],
        }
    }

    resource_add = requests.post(SHEETY_ENDPOINT, json=params_add, auth=(SHEETY_USER, SHEETY_PASSWORD))
    print(resource_add.text)
