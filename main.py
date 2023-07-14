import requests
import os
from twilio.rest import Client

api_key = "a4a0bec10ba427fec3cc37fef209ed63"

MY_LAT = 31.811001 # Your latitude
MY_LONG = 119.973999  # Your longitude

account_sid = 'ACe132778fa8b005c4ad14d02699b39308'
auth_token = 'cff3428bd903af187ed82c482b2f90af'
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for i in range(0, 12):
    weather_code = weather_data["hourly"][i]["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+19402919950',
        to='+917488311171'
    )
    print(message.status)
