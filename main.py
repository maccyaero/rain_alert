import requests
import datetime
import time
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials Read more at http://twil.io/secure

# TODO: The Environment variables are not working for the below Twilio variables, check later on how to make them
#  work.  #

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

api_key = os.environ.get("OPEN_WEATHER_MAP_API_KEY")
OWM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
weather_parameters = {
    'lat': 24.8607,
    'lon': 67.0011,
    'app_id': api_key
}
# Variables

will_rain = False

# Get the current time
current_time = datetime.datetime.now()
# print(current_time)
today = datetime.date.today()

# Check if the current time is 7 am
if current_time.hour == 7:
    # Run the script
    response = requests.get(OWM_endpoint, params=weather_parameters)
    response.raise_for_status()
    new_list = response.json()['list']
    # print(new_list)
    for item in new_list:
        date = item["dt_txt"].split(" ", 1)
        if date[0] == today.strftime('%Y-%m-%d'):
            # print(item['weather'][0]['description'])
            if "rain" in item['weather'][0]['description']:
                will_rain = True

    if will_rain:
        print("Please carry an umbrella")
        message = client.messages.create(
            body="Please carry an umbrella today",
            from_="",  # Type the to and from numbers here.
            to=""
        )
        print(message.status)

    else:
        print("Looks Clear, no rain !")

    # print(response.json())
