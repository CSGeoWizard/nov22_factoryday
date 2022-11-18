import requests
import datetime
import pandas as pd

def api_call():
    API_KEY = '3faf1d1d4c95245aff49d70ebaf587b9'
    lat = '40.4406'
    lon = '79.9959'
    number_of_days = 30
    current_time = 1668798184
    start_time = current_time - number_of_days * 86400
    dates = []
    temps = []

    for i in range(number_of_days):
        request = 'http://api.openweathermap.org/data/3.0/onecall/timemachine?lat=' + lat + '&lon=' + lon + '&dt=' + str(start_time + i * 86400) + '&appid=' + API_KEY
        response = requests.get(request)
        temps.append(response.json()['data'][0]['temp'])
        dates.append(datetime.datetime.fromtimestamp(start_time + i * 86400))

    df = pd.DataFrame(zip(dates, temps))

    return df
