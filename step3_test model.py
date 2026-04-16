# STEP 3: TEST MODEL

import joblib
import pandas as pd

# Load trained model
model = joblib.load(
    "E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\models\\pricing_model.pkl"
)

print("✅ Model loaded successfully\n")

# Sample test input
test_data = pd.DataFrame([{
    "time_hour": 19,
    "voltage_V": 225,
    "current_A": 1.40,
    "power_factor": 0.95,
    "power_W": 315,
    "energy_kWh": 0.45,
    "cumulative_energy_kWh": 5.20,
    "demand_level": 9,
    "grid_load": 0.21,
    "peak_hour": 1
}])

# Predict
prediction = model.predict(test_data)

print("🔹 Test Input:")
print(test_data)

print("\n💰 Predicted Price (Rs/kWh):", round(prediction[0], 2))