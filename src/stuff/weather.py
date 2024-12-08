import requests



def get_data(latitude, longitude) :
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,  
        "hourly": "relative_humidity_2m,precipitation_probability",  
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
   
        # Извлекаем данные в формате JSON
        data = response.json()  
        return data
    else:
        print(f'Ошибка: {response.status_code}')   


def normalize_data(data) :
    current_weather = data.get("current_weather", {})
    hourly_data = data.get("hourly", {}) 
    humidity = hourly_data.get("relative_humidity_2m", [None])[0]  #Первый час
    precipitation_probability = hourly_data.get("precipitation_probability", [None])[0]
    result =  {
        "temperature": current_weather.get("temperature"),
        "humidity": humidity,  
        "wind_speed": current_weather.get("windspeed"),
        "precipitation_probability": precipitation_probability,  
    }
    return result

