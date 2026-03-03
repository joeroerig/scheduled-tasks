import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
#KAD3ANSAA89DU7W4PREFDTL7
# $env:OWM_API_KEY = "133cddc69b4238b476aff37a8625aa2d"

# From Open Weather Map
api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

#From Twilio
from_number = os.environ.get("TWILIO_WHATSAPP_FROM_NUMBER")
to_number = os.environ.get("TWILIO_WHATSAPP_TO_NUMBER")


weather_params = {
    "lon" : -93.5268986,
    "lat" : 44.7980186,
    "appid" : api_key,
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
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=from_number,
        body="Bring an Umbrella fella. ☂️ ",
        to=to_number
    )

    print(message.status)

