import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv(".env")

    MY_LAT = 52.362990
    MY_LON = 4.873220
    OWM_API_KEY = os.environ.get("OWM_API_KEY")
    OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"

    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

    params = {
        "appid": OWM_API_KEY,
        "lat": MY_LAT,
        "lon": MY_LON,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(url=OWM_API_ENDPOINT, params=params)
    response.raise_for_status()

    does_rain = False
    weather_data = response.json()

    if "hourly" in weather_data and len(weather_data["hourly"]) > 0:
        weather_next_12h = weather_data["hourly"][:12]
        for h in weather_next_12h:
            if "weather" in h:
                for w in h["weather"]:
                    if w["id"] < 700:
                        does_rain = True

    if does_rain:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body="Bring an umbrella. It's going to rain! ☔",
            from_='+16692051295',
            to='+31621636111'
        )
        print(f"rain alert sent: {message.status}")
    else:
        print("it does not rain")
