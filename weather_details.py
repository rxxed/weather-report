import json, requests

API_KEY = ""

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def weather_report(city_name):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    # convert json format data into
    # python format data
    weather_report = response.json()
    if weather_report["cod"] != "404":
        temperature = weather_report["main"]["temp"] - 273.15
        humidity = weather_report["main"]["humidity"]
        description = weather_report["weather"][0]["main"]
        pressure = weather_report["main"]["pressure"]
        elaborate = weather_report["weather"][0]["description"]
        name = weather_report["name"]
        error_code = weather_report["cod"]
        weather_dict = {"name":name, "temp":round(temperature,1), "humidity":humidity,
                        "desc":description, "pressure":pressure, "elaborate": elaborate,
                        "code": error_code}
        return weather_dict
    else:
        pass
        # city not found


weather = weather_report("Seattle")
print(weather["desc"])
