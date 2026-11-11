industry_weights = {

    "Thermal Power Plant": {
        "carbon": 0.80,
        "credit": 0.20
    },

    "Cement Industry": {
        "carbon": 0.80,
        "credit": 0.20
    },

    "Steel Industry": {
        "carbon": 0.75,
        "credit": 0.25
    },

    "Chemical Industry": {
        "carbon": 0.70,
        "credit": 0.30
    },

    "Textile Industry": {
        "carbon": 0.65,
        "credit": 0.35
    },

    "Paper Industry": {
        "carbon": 0.70,
        "credit": 0.30
    },

    "Food Processing": {
        "carbon": 0.60,
        "credit": 0.40
    }

}


def get_suitable_crops(
        crop_data,
        district,
        industry,
        soil,
        water):

    # -----------------------------
    # Filter by District
    # -----------------------------
    district_crops = crop_data[
        (
            crop_data["Suitable_District"]
            .str.contains(district, case=False, na=False)
        )
        |
        (
            crop_data["Suitable_District"]
            .str.lower() == "both"
        )
    ]

    if len(district_crops) == 0:
        district_crops = crop_data

    # -----------------------------
    # Filter by Soil
    # -----------------------------
    soil_crops = district_crops[
        district_crops["Suitable_Soil"]
        .str.contains(
            soil,
            case=False,
            na=False
        )
    ]

    if len(soil_crops) == 0:
        soil_crops = district_crops

    # -----------------------------
    # Filter by Water
    # -----------------------------
    water_crops = soil_crops[
        soil_crops["Water_Requirement"]
        .str.lower()
        ==
        water.lower()
    ]

    if len(water_crops) == 0:
        water_crops = soil_crops

    # -----------------------------
    # Convert Carbon Credit Potential
    # -----------------------------
    credit_score = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    water_crops = water_crops.copy()

    water_crops["Credit_Score"] = (
        water_crops["Carbon_Credit_Potential"]
        .map(credit_score)
        .fillna(1)
    )

    # -----------------------------
    # Get Industry Weights
    # -----------------------------
    weights = industry_weights.get(
        industry,
        {
            "carbon": 0.60,
            "credit": 0.40
        }
    )

    # -----------------------------
    # Calculate Recommendation Score
    # -----------------------------
    water_crops["Recommendation_Score"] = (
        water_crops["Carbon_Seq_Avg"] * weights["carbon"]
        +
        water_crops["Credit_Score"] * weights["credit"]
    )

    # -----------------------------
    # Sort by Recommendation Score
    # -----------------------------
    water_crops = water_crops.sort_values(
        by="Recommendation_Score",
        ascending=False
    )

    # Select top recommended crops
    top_crops = (
        water_crops
        .drop_duplicates(subset=["Crop_Name"])
        .head(3)
    )

    return top_crops

