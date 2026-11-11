from flask import Flask, render_template, request
import pandas as pd

from recommendation import get_suitable_crops
from optimizer import optimize_land
from carbon_credit import carbon_credit_summary

from soil_api import soil_api
from weather_api import weather_api, get_weather_data
from weather_filter import filter_by_weather

import joblib
from ml_predict import predict_crop

app = Flask(__name__)

app.register_blueprint(soil_api)
app.register_blueprint(weather_api)

# ============================
# Load Dataset
# ============================

crop_data = pd.read_excel(
    "datasets/crop_dataset_v2.xlsx"
)

# ============================
# Load Machine Learning Model
# ============================

model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")

# ============================
# Home Page
# ============================

@app.route("/")
def home():
    return render_template("index.html")


# ============================
# Input Page
# ============================

@app.route("/input")
def input_page():
    return render_template("input.html")


# ============================
# Result Page
# ============================

@app.route("/result", methods=["POST"])
def result():

    district = request.form["district"]
    industry = request.form["industry"]

    co2 = float(request.form["co2"])
    land = float(request.form["land"])

    soil = request.form["soil"]
    water = request.form["water"]

    # ============================
    # Machine Learning Prediction
    # ============================

    predicted_crop = predict_crop(
        model,
        encoders,
        target_encoder,
        soil,
        water
    )

    print("Predicted Crop:", predicted_crop)

    # ============================
    # Rule-Based Recommendation
    # ============================

    crops = get_suitable_crops(
        crop_data,
        district,
        industry,
        soil,
        water
    )

    # Get live weather
    weather = get_weather_data(district)
    print("Weather from API:", weather)

    # Filter crops based on temperature
    crops = filter_by_weather(crops, weather)

    print("Weather sent to template:", weather)
    
    # Optimize land allocation
    recommended = optimize_land(
        crops,
        land,
        co2
    )

    # Calculate total carbon captured
    total_captured = recommended["Carbon_Captured"].sum()

    # Calculate carbon credit value
    credit_info = carbon_credit_summary(
        total_captured
    )

    return render_template(
        "result.html",
        district=district,
        industry=industry,
        co2=co2,
        land=land,
        soil=soil,
        water=water,
        weather=weather,
        crops=recommended.to_dict(orient="records"),
        carbon_credits=credit_info["Carbon_Credits"],
        credit_value=credit_info["Credit_Value_INR"]
    )


if __name__ == "__main__":
    app.run(debug=True)