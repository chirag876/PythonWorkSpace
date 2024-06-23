import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def time_zone(city_name):
    try:
        # initialize Nominatim API
        geolocator = Nominatim(user_agent="geoapiExercises")

        # getting Latitude and Longitud
        location = geolocator.geocode(city_name)

        # pass the Latitude and Longitud
        # into a timezone_at
        # and it return timezone
        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        PARAMS = {
            'timezone': result,
            'token': 'aqulyBKQEzgWiZUdVmKp'
            }
        headers = {'Content-Type': 'application/json'}
        url = "https://timezoneapi.io/api/timezone/"
        response = requests.get(url, params = PARAMS, headers= headers).json()

        if response['meta']['code'] == "200":
            return f"""Time Zone: {result}\r\nDay : {response['data']['datetime']['day_full']}\r\nDate: {response['data']['datetime']['date']}\r\nTime: {response['data']['datetime']['time']}"""
        else:
            return "Please enter the correct location !"
    except:
        return "We are unable to process your request. Please try again in sometime"
        