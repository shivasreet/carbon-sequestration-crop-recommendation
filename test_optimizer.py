from optimizer import recommend_crops

result = recommend_crops(
    district="Coimbatore",
    soil="Red Loam",
    water="Medium",
    land=2
)

print(result[
    [
        "Crop_Name",
        "Carbon_Seq_Avg",
        "Suitable_Soil",
        "Water_Requirement"
    ]
])