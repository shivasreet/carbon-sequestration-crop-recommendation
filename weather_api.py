
from flask import Blueprint, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

weather_api = Blueprint("weather_api", __name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

SUPPORTED_DISTRICTS = [
    "Coimbatore",
    "Tiruppur"
]


def get_weather_data(district):

    if district not in SUPPORTED_DISTRICTS:
        return None

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={district},IN&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    weather = response.json()

    print(weather)

    return {
        "temperature": weather["main"]["temp"],
        "humidity": weather["main"]["humidity"],
        "weather": weather["weather"][0]["description"],
        "wind_speed": weather["wind"]["speed"]
    }


@weather_api.route("/weather", methods=["POST"])
def get_weather():

    data = request.get_json()

    district = data.get("district")

    weather = get_weather_data(district)

    if weather is None:
        return jsonify({
            "status": "error",
            "message": "Unable to fetch weather."
        }), 400

    return jsonify({
        "status": "success",
        "district": district,
        "weather": weather
    })
