def check_bad_weather(weather): 
    temperature = weather.get("temperature")
    wind_speed = weather.get("wind_speed")
    precipitation_probability = weather.get("precipitation_probability")
    humidity = weather.get("humidity")

    if temperature < 0 or temperature > 35:
        return "Плохая погода: экстремальная температура"
    if wind_speed > 50:
        return "Плохая погода: сильный ветер"
    if precipitation_probability > 70:
        return "Плохая погода: высокая вероятность дождя"
    if humidity > 80:
        return "Плохая погода: высокая влажность"

    return "Все хайп"

