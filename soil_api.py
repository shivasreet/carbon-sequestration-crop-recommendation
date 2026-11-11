from flask import Blueprint, request, jsonify

soil_api = Blueprint("soil_api", __name__)

SOIL_DATA = {

    "Black": {
        "soil_type": "Black",
        "ph_range": "6.5 - 8.0",
        "fertility": "High",
        "water_retention": "High",
        "drainage": "Moderate",
        "description": "Rich in clay and nutrients. Suitable for crops requiring good moisture retention."
    },

    "Red Loam": {
        "soil_type": "Red Loam",
        "ph_range": "5.5 - 7.5",
        "fertility": "Medium",
        "water_retention": "Medium",
        "drainage": "Good",
        "description": "Well-drained soil with moderate fertility."
    },

    "Loam": {
        "soil_type": "Loam",
        "ph_range": "6.0 - 7.5",
        "fertility": "Very High",
        "water_retention": "High",
        "drainage": "Excellent",
        "description": "Balanced soil containing sand, silt and clay. Ideal for most crops."
    },

    "Sandy": {
        "soil_type": "Sandy",
        "ph_range": "5.5 - 7.0",
        "fertility": "Low",
        "water_retention": "Low",
        "drainage": "Very Good",
        "description": "Light soil with fast drainage. Suitable for drought-tolerant crops."
    }

}


@soil_api.route("/soil", methods=["POST"])
def get_soil():

    data = request.get_json()

    soil = data.get("soil_type")

    if soil not in SOIL_DATA:
        return jsonify({
            "status": "error",
            "message": "Invalid soil type"
        }), 400

    return jsonify({
        "status": "success",
        "soil": SOIL_DATA[soil]
    })