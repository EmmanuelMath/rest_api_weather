from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from api_data_retriever import WeatherApiRetriver 


app = Flask(__name__)
api = Api(app)


# This creates an instance of RequestParser, which 
# is used to parse and validate incoming request data.
weather_args = reqparse.RequestParser()
weather_args.add_argument('city', type=str, required=True, help="City cannot be blank")
weather_args.add_argument('date', type=str, required=True, help="Date cannot be blank, format should be YYYY-MM-DD")


class Weather(Resource):
    def get(self, city, date):
        try:
            weather_data = WeatherApiRetriver(
                city_name=city, date=date).get_json_info()
            return jsonify(weather_data)
        except Exception as exc:
            return jsonify({"error": str(exc)})

api.add_resource(Weather, "/city/city=<city>&date=<date>")


if __name__ == "__main__":
    app.run(port=5000, debug=True)