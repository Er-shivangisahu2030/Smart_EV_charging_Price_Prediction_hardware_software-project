# STEP 2: TRAIN MODEL

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load dataset
data = pd.read_csv("E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\ev_dynamic_pricing_60days.csv")

print("✅ Dataset loaded successfully\n")

# Features
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

# Target
y = data["price_rs_per_kWh"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("🔹 Training Data Shape:", X_train.shape)
print("🔹 Testing Data Shape:", X_test.shape)

# Create model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

print("\n✅ Model trained successfully")

# Predict on test set
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Performance:")
print("MAE :", round(mae, 3))
print("MSE :", round(mse, 3))
print("R2 Score :", round(r2, 3))

# Feature importance
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\n🔹 Feature Importance:")
print(feature_importance)

# Save model
joblib.dump(
    model,
    "E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\models\\pricing_model.pkl"
)

print("\n💾 Model saved to models/pricing_model.pkl")