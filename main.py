import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lon" : -93.5268986,
    "lat" : 44.7980186,
    "appid" : OWM_API_KEY,
    "cnt" : 4,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for forecast in weather_data["list"]:
     if int(forecast['weather'][0]['id']) < 1700:
         will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_=TWILIO_WHATSAPP_FROM_NUMBER,
        body="Bring an Umbrella fella. ☂️ ",
        to=TWILIO_WHATSAPP_TO_NUMBER
    )

    print(message.status)

