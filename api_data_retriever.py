import datetime
import time
import json
import requests
from credentials import API_KEY


class WeatherApiRetriver:

    def __init__(self, city_name, date): #date format => 1996-02-17
        self.city_name = city_name
        self.date = date

    def get_weather_data(self) -> json:
        celsius = "metric"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={API_KEY}&units={celsius}"
        data_json = requests.get(api_url).json()
        return data_json

    def get_historical_data(self) -> json:
        cordinates = self.get_weather_data()["coord"]
        lat = cordinates["lat"]
        lon = cordinates["lon"]
        celsius = "metric"
        api_url_historical = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={self.date}&appid={API_KEY}&units={celsius}"
        data_json = requests.get(api_url_historical).json()
        return data_json
    
    def __calculate_avergae_temp(self):
        temp_data = self.get_historical_data()["temperature"]
        avg_temp = (
            temp_data["afternoon"] + 
            temp_data["morning"] + 
            temp_data["evening"] + 
            temp_data["night"]
            ) / 4

        return round(avg_temp, 2)

    
    def get_json_info(self) -> dict:
        date = self.date
        humidity_data = self.get_historical_data()["humidity"]
        temp_data = self.get_historical_data()["temperature"]
        city = self.city_name
        humidity = humidity_data["afternoon"]
        max_temp = temp_data["max"]
        min_temp = temp_data["min"]
        avg_temp = self.__calculate_avergae_temp()

        weather_model = {
            "city_name" : city,
            "min_temp" : min_temp,
            "max_temp" : max_temp,
            "avg_temp" : avg_temp,
            "humidity" : humidity,
        }
        return weather_model