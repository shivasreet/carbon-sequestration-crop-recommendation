import pandas as pd

print("=" * 60)
print("CARBON SEQUESTRATION CROP RECOMMENDATION SYSTEM")
print("=" * 60)

# Read all datasets
industry = pd.read_excel("datasets/industry_dataset_v2.xlsx")
crop = pd.read_excel("datasets/crop_dataset_v2.xlsx")
carbon = pd.read_excel("datasets/top25_carbon_crops_dataset.xlsx")
mixed = pd.read_excel("datasets/mixed_cropping_dataset_250_rules.xlsx")
credits = pd.read_excel("datasets/carbon_credits_reference.xlsx")

datasets = {
    "Industry Dataset": industry,
    "Crop Dataset": crop,
    "Carbon Dataset": carbon,
    "Mixed Cropping Dataset": mixed,
    "Carbon Credits Dataset": credits
}

for name, data in datasets.items():
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print("\nRows and Columns:")
    print(data.shape)

    print("\nColumn Names:")
    print(list(data.columns))

    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nMissing Values:")
    print(data.isnull().sum())

print("\nAll datasets loaded successfully!")