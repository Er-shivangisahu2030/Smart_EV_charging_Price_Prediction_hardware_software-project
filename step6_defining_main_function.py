# MAIN PROGRAM — SMART EV CHARGING AI SYSTEM

import joblib
from step5_defining_helper_function import display_price
from step5_defining_helper_function import *

# ----------------------------------------
# Load Trained Model
# ----------------------------------------
model = joblib.load(
    r"E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\models\\pricing_model.pkl"
)

print("⚡ Smart EV Charging AI System Started")
print("--------------------------------------")

# ----------------------------------------
# User Inputs
# ----------------------------------------
time_hour = int(input("Enter time (0–23): "))
voltage_V = float(input("Enter voltage (V): "))
current_A = float(input("Enter current (A): "))
power_factor = float(input("Enter power factor (0.7–1.0): "))

# ----------------------------------------
# Calculate Derived Values
# ----------------------------------------

# Power formula
power_W = calculate_power(voltage_V, current_A, power_factor)

# Energy for 1 hour
energy_kWh = calculate_energy(power_W)

# Grid load from plant capacity
grid_load = calculate_grid_load(power_W)

# Demand level from grid load
demand_level = calculate_demand_level(grid_load)

# Peak hour detection
peak_hour = calculate_peak_hour(time_hour)

# Cumulative energy estimate
cumulative_energy_kWh = calculate_cumulative_energy(
    energy_kWh,
    time_hour
)

# ----------------------------------------
# Show Calculated Values
# ----------------------------------------
print("\n📊 Calculated Values:")
print("Power (W):", power_W)
print("Energy (kWh):", energy_kWh)
print("Grid Load:", grid_load)
print("Demand Level:", demand_level)
print("Peak Hour:", peak_hour)
print("Cumulative Energy:", cumulative_energy_kWh)

# ----------------------------------------
# Prepare Input for Model
# ----------------------------------------
input_data = prepare_input(
    time_hour,
    voltage_V,
    current_A,
    power_factor,
    power_W,
    energy_kWh,
    cumulative_energy_kWh,
    demand_level,
    grid_load,
    peak_hour
)

# ----------------------------------------
# Predict Price
# ----------------------------------------
predicted_price = model.predict(input_data)[0]

# ----------------------------------------
# Display Result
# ----------------------------------------
display_price(predicted_price)

# ----------------------------------------
# Recommendation
# ----------------------------------------
if predicted_price < 9:
    print("🟢 Best Time to Charge")
elif predicted_price < 12:
    print("🟡 Moderate Charging Cost")
else:
    print("🔴 Peak Hour - Charging Expensive")

print("\n✅ System Ready for Hardware Integration")