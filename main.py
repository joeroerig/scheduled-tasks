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
account_sid = "AC2fd327e74faa77e1be2199eefd56f96b"
auth_token = "3935f908f7e91f1d7716beda56a698e0"
#From Twilio
PHONE = "+18666217128"
TWILIO_WHATSAPP_FROM_NUMBER = "whatsapp:+14155238886"
TWILIO_WHATSAPP_TO_NUMBER = "whatsapp:+16126008645"

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
        from_=TWILIO_WHATSAPP_FROM_NUMBER,
        body="Bring an Umbrella fella. ☂️ ",
        to=TWILIO_WHATSAPP_TO_NUMBER
    )

    print(message.status)

