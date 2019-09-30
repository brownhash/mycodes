import requests


def weather(lat, lon, api_key):
    url = "https://api.forecast.io/forecast/"

    weather_url = url + api_key + "/" + str(lat) + "," + str(lon) + "?callback=?"

    data = requests.get(weather_url)
    weather_report = ""
    for i in list(data.text.split("/**/ typeof  === 'function' && ")[1]):
        if i != ";" and i != "\n":
            weather_report += str(i)

    data = eval(weather_report)

    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timezone = data.get('timezone')
    weather = data.get('currently').get('summary')
    temperature = data.get('currently').get('temperature')
    apparent_temperature = data.get('currently').get('apparentTemperature')
    humidity = data.get('currently').get('humidity')*100
    pressure = data.get('currently').get('pressure')
    wind_speed = data.get('currently').get('windSpeed')
    visibility = data.get('currently').get('visibility')

    result = {
        'latitude': latitude,
        'longitude': longitude,
        'timezone': timezone,
        'weather': weather,
        'temp': round(((temperature - 32) * 5) / 9, 1),
        'apparent_temp': round(((apparent_temperature - 32) * 5) / 9, 1),
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'visibility': visibility
    }

    return result


#apiKey = "f536d4c3330c0a1391370d1443cee848"
#print(weather('28.45', '77.07', apiKey))

requests.get("http://35.244.53.82/28.45&77.07")