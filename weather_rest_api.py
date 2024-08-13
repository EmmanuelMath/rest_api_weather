from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from api_data_retriever import WeatherApiRetriver 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

class WeatherCache(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    date = db.Column(db.String(10), nullable=False)
    data = db.Column(db.JSON, nullable=False)

    __table_args__ = (db.UniqueConstraint('city', 'date', name='    '),)


# validate incoming request data.
weather_args = reqparse.RequestParser()
weather_args.add_argument('city', type=str, required=True, help="City cannot be blank")
weather_args.add_argument('date', type=str, required=True, help="Date cannot be blank, format should be YYYY-MM-DD")


class Weather(Resource):
    def get(self):
        city = request.args.get('city')
        date = request.args.get('date')

        if not city or not date:
            return jsonify({"error": "City and date parameters are required"}), 400

        cached_data = WeatherCache.query.filter_by(city=city, date=date).first()

        if cached_data:
            return jsonify(cached_data.data)

        try:
            weather_data = WeatherApiRetriver(city_name=city, date=date).get_json_info()
            # new data
            new_cache = WeatherCache(city=city, date=date, data=weather_data)
            db.session.add(new_cache)
            db.session.commit()
            return jsonify(weather_data)
        except Exception as exc:
            return jsonify({"error": str(exc)}), 500


api.add_resource(Weather, "/weather/city")


if __name__ == "__main__":
    app.run(port=5000, debug=True)