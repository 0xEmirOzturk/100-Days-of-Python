import requests

lat = 38.368626
lon = 34.029701

API_KEY = [API_KEY]

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric",
}

response = requests.get(
    url=f"https://api.openweathermap.org/data/2.5/weather",
    params= parameters
)
response.raise_for_status()
data = response.json()
print(data)