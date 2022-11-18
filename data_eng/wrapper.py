import requests
import datetime
import pandas as pd

API_KEY = '3faf1d1d4c95245aff49d70ebaf587b9'
lat = '40.4406'
lon = '79.9959'
number_of_days = 30
current_time = 1668785584
start_time = current_time - number_of_days * 86400
dates = []
temps = []

for i in range(number_of_days):
    request = 'http://api.openweathermap.org/data/3.0/onecall/timemachine?lat=' + lat + '&lon=' + lon + '&dt=' + str(start_time + i * 86400) + '&appid=' + API_KEY
    # request = 'https://api.openweathermap.org/data/3.0/weather?lat=' + lat + '&lon=' + lon + '&appid=' + API_KEY
    response = requests.get(request)
    temps.append(response.json()['data'][0]['temp'])
    dates.append(datetime.datetime.fromtimestamp(start_time + i * 86400))
    # print(response.json()['main']['temp_max'])


df = pd.DataFrame(zip(dates, temps))
# request2 = 'https://public.opendatasoft.com/api/records/1.0/search/?dataset=noaa-daily-weather-data&q=&rows=10&facet=date&facet=name&facet=country_code&timezone=America%2FNew_York'

# print(df.head())

# print(response.json()['records'][0].keys())
