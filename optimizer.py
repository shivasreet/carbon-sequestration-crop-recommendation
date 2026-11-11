import pandas as pd

from carbon_calculator import total_carbon


def optimize_land(crops, land, co2_target):

    """
    Allocate available land among top recommended crops
    and calculate carbon sequestration.
    """

    recommendations = []

    # Sort crops based on carbon sequestration
    crops = crops.sort_values(
        by="Carbon_Seq_Avg",
        ascending=False
    )

    # Remove duplicate crops
    crops = crops.drop_duplicates(
        subset=["Crop_Name"]
    )

    # Take top 3 crops
    crops = crops.head(3)

    # Equal land allocation
    area_per_crop = land / len(crops)


    for _, crop in crops.iterrows():

        carbon_captured = total_carbon(
            area_per_crop,
            crop["Carbon_Seq_Avg"]
        )

        recommendations.append({

            "Crop_Name": crop["Crop_Name"],

            "Allocated_Area": round(
                area_per_crop,
                2
            ),

            "Carbon_Captured": round(
                carbon_captured,
                2
            ),

            "Water_Requirement":
                crop["Water_Requirement"],

            "Carbon_Seq_Avg":
                crop["Carbon_Seq_Avg"]

        })


    return pd.DataFrame(recommendations)