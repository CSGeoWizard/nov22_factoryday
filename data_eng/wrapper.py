import requests

def api_request():
    API_KEY = '3faf1d1d4c95245aff49d70ebaf587b9'
    lat = '40.4406'
    lon = '79.9959'
    start = '1666119016'
    end = '1668801016'
    request = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + API_KEY

    response = requests.get(request)

    return response.json()['main']['temp_max']
