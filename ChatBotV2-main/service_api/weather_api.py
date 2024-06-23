import requests

def weather_by_city_name(city_name):
    try:
        PARAMS = {'q': city_name, 
            'appid': ""
            }
        headers = {'Content-Type': 'application/json'}
        url = "http://api.openweathermap.org/data/2.5/weather"
        response = requests.get(url, params = PARAMS, headers= headers).json()
        if response["cod"] == 200:
            degree_sign = u"\N{DEGREE SIGN}"
            temperature_in_kelvin = response ['main']['temp']
            temperature_in_celsius = round(temperature_in_kelvin - 273.73)
            temperature_in_fahrenheit = round(temperature_in_celsius * 1.8 +32)
            
            return f"Temperature : {temperature_in_celsius} {degree_sign}C / {temperature_in_fahrenheit} {degree_sign}F" 
        else:
            return "Please enter the correct location !"
    except:
        return "We are unable to process your request. Please try again in sometime"