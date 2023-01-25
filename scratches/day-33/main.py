import smtplib
import time

import requests
from datetime import datetime

MY_LATITUDE = 52.370216
MY_LONGITUDE = 4.895168


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    print(f"iss_latitude: {iss_latitude}")
    print(f"iss_longitude: {iss_longitude}")

    # Your position is within +5 or -5 degrees of the iss position
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    print(f"now:{time_now} sunrise:{sunrise} sunset:{sunset}")

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.freesmtpservers.com")
        # connection.starttls()
        # connection.login("email", "password")
        connection.sendmail(
            from_addr="iss@freesmtpservers.com",
            to_addrs="fabio@freesmtpservers.com",
            msg="Subject: Look Up☝️\n\nThe ISS is above you in the sky."
        )
