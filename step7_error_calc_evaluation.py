# MAIN2 — MODEL ACCURACY EVALUATION

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("📊 Model Accuracy Evaluation Started")
print("-----------------------------------")

# ----------------------------------------
# Load Dataset
# ----------------------------------------
data = pd.read_csv(
    r"E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\ev_dynamic_pricing_60days.csv"
)

# ----------------------------------------
# Features and Target
# ----------------------------------------
X = data[[
    "time_hour",
    "voltage_V",
    "current_A",
    "power_factor",
    "power_W",
    "energy_kWh",
    "cumulative_energy_kWh",
    "demand_level",
    "grid_load",
    "peak_hour"
]]

y = data["price_rs_per_kWh"]

# ----------------------------------------
# Split Data (Train/Test)
# ----------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("✅ Dataset split into training & testing")
print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ----------------------------------------
# Load Trained Model
# ----------------------------------------
model = joblib.load(
    r"E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\models\\pricing_model.pkl"
)

print("✅ Model loaded successfully")

# ----------------------------------------
# Predict on Test Data
# ----------------------------------------
y_pred = model.predict(X_test)

# ----------------------------------------
# Calculate Metrics
# ----------------------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# ----------------------------------------
# Display Results
# ----------------------------------------
print("\n📈 MODEL PERFORMANCE METRICS")
print("-----------------------------------")

print("MAE  (Mean Absolute Error):", round(mae, 3))
print("MSE  (Mean Squared Error):", round(mse, 3))
print("RMSE (Root Mean Squared Error):", round(rmse, 3))
print("R² Score (Accuracy):", round(r2 * 100, 2), "%")

# ----------------------------------------
# Compare Actual vs Predicted
# ----------------------------------------
comparison_df = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print("\n🔹 Actual vs Predicted Prices:")
print(comparison_df.head(10))

# ----------------------------------------
# Feature Importance
# ----------------------------------------
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n🔹 Feature Importance:")
print(feature_importance)

print("\n✅ Evaluation Complete")