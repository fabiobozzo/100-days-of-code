import requests

MY_LAT = 52.362990
MY_LON = 4.873220
OWM_API_KEY = "3260a87b309f1ab3f1c1ce5a60f51b60"
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"

if __name__ == '__main__':
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
        print("Bring an umbrella. It's gonna rain.")
        # TODO: send a SMS w/ Twilio API
