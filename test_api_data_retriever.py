import pytest
from unittest.mock import patch, MagicMock
from api_data_retriever import WeatherApiRetriver

# Mock data to return for API calls
mock_weather_data = {
    "coord": {"lat": 51.5074, "lon": -0.1278}, 
    "weather": [{"description": "clear sky"}],
    "main": {"temp": 15},
}

mock_historical_data = {
    "temperature": {
        "morning": 12,
        "afternoon": 18,
        "evening": 16,
        "night": 10,
        "min": 10,
        "max": 18,
    },
    "humidity": {
        "morning": 70,
        "afternoon": 50,
        "evening": 60,
        "night": 80,
    }
}

class TestApiDataRetriever:

    @patch('requests.get')
    def test_get_weather_data(self, mock_get):
        mock_get.return_value = MagicMock(json=lambda: mock_weather_data)
        
        retriever = WeatherApiRetriver(city_name="London", date="2023-08-12")
        weather_data = retriever.get_weather_data()
        
        assert weather_data["coord"]["lat"] == 51.5074
        assert weather_data["main"]["temp"] == 15

    @patch('requests.get')
    def test_get_historical_data(self, mock_get):
        mock_get.side_effect = [
            MagicMock(json=lambda: mock_weather_data),
            MagicMock(json=lambda: mock_historical_data)
        ]
        
        retriever = WeatherApiRetriver(city_name="London", date="2023-08-12")
        historical_data = retriever.get_historical_data()
        
        assert historical_data["temperature"]["afternoon"] == 18
        assert historical_data["humidity"]["morning"] == 70

    @patch('requests.get')
    def test_get_json_info(self, mock_get):
        mock_get.side_effect = [
            MagicMock(json=lambda: mock_weather_data),
            MagicMock(json=lambda: mock_historical_data),
            MagicMock(json=lambda: mock_historical_data)
        ]
        
        retriever = WeatherApiRetriver(city_name="London", date="2023-08-12")
        json_info = retriever.get_json_info()
        
        assert json_info["city_name"] == "London"
        assert json_info["min_temp"] == 10
        assert json_info["max_temp"] == 18
        assert json_info["avg_temp"] == 14.0 
        assert json_info["humidity"] == 50
