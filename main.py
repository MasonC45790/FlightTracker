
from dotenv import dotenv_values
import requests


dotenv=dotenv_values('.env')

import requests
response=requests.get('https://api.aviationstack.com/v1/flights?access_key='+dotenv["API"])
for flight in response.json()['data']:
    if flight['flight_status']=='active':
        print('airline'+flight['airline']['name']+flight['departure']['airport'])

