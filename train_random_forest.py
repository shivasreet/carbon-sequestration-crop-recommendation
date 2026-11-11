import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("TRAINING RANDOM FOREST MODEL")
print("=" * 60)

# ------------------------------------
# Load Dataset
# ------------------------------------
df = pd.read_excel("datasets/crop_dataset_v2.xlsx")

print("\nDataset Loaded Successfully!")
print("Total Records:", len(df))

# ------------------------------------
# Data Preprocessing
# ------------------------------------

# Split multiple soil values into separate records
df["Suitable_Soil"] = df["Suitable_Soil"].str.split(";")

# Create separate rows for each soil type
df = df.explode("Suitable_Soil")

# Remove extra spaces
df["Suitable_Soil"] = df["Suitable_Soil"].str.strip()


# ------------------------------------
# Features (Remove Suitable_District)
# ------------------------------------
features = [
    "Suitable_Soil",
    "Water_Requirement"
]

X = df[features].copy()


# ------------------------------------
# Target
# ------------------------------------
y = df["Crop_Name"]


# ------------------------------------
# Encode Features
# ------------------------------------
encoders = {}

for column in X.columns:
    encoder = LabelEncoder()
    X[column] = encoder.fit_transform(X[column].astype(str))
    encoders[column] = encoder


# ------------------------------------
# Encode Target
# ------------------------------------
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)


# ------------------------------------
# Train Random Forest
# ------------------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


# ------------------------------------
# Save Model
# ------------------------------------
joblib.dump(model, "model.pkl")
joblib.dump(encoders, "encoders.pkl")
joblib.dump(target_encoder, "target_encoder.pkl")


print("\nModel trained successfully!")
print("Files saved:")
print("model.pkl")
print("encoders.pkl")
print("target_encoder.pkl")