# HELPER FUNCTIONS FOR SMART EV CHARGING PROJECT

import pandas as pd


# ----------------------------------------
# Load Dataset
# ----------------------------------------
def load_dataset(file_path=r"E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\ev_dynamic_pricing_60days.csv"):
    
    data = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully")
    return data


# ----------------------------------------
# Split Features and Target
# ----------------------------------------
def split_features_target(data):

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

    return X, y


# ----------------------------------------
# Calculate Power
# Formula: P = V × I × PF
# ----------------------------------------
def calculate_power(voltage_V, current_A, power_factor):

    power_W = round(voltage_V * current_A * power_factor, 2)
    return power_W


# ----------------------------------------
# Calculate Energy
# Formula: Energy = Power / 1000
# Assuming 1 hour charging duration
# ----------------------------------------
def calculate_energy(power_W):

    energy_kWh = round(power_W / 1000, 3)
    return energy_kWh


# ----------------------------------------
# Calculate Grid Load
# Formula: Power / Plant Capacity
# Plant Capacity = 1500 W
# ----------------------------------------
def calculate_grid_load(power_W):

    plant_capacity = 1500
    grid_load = round(power_W / plant_capacity, 2)
    return grid_load


# ----------------------------------------
# Calculate Demand Level
# Based on grid load
# ----------------------------------------
def calculate_demand_level(grid_load):

    if grid_load < 0.10:
        return 2
    elif grid_load < 0.15:
        return 5
    elif grid_load < 0.20:
        return 8
    else:
        return 9


# ----------------------------------------
# Detect Peak Hour
# ----------------------------------------
def calculate_peak_hour(time_hour):

    if 17 <= time_hour <= 21:
        return 1
    else:
        return 0


# ----------------------------------------
# Calculate Cumulative Energy
# ----------------------------------------
def calculate_cumulative_energy(energy_kWh, time_hour):

    cumulative_energy_kWh = round(
        energy_kWh * (time_hour + 1),
        3
    )

    return cumulative_energy_kWh


# ----------------------------------------
# Calculate Price Formula
# ----------------------------------------
def calculate_price_formula(demand_level, grid_load):

    price = round(
        6.5 + (demand_level * 0.5) + (grid_load * 10),
        2
    )

    return price


# ----------------------------------------
# Prepare Input for Prediction
# ----------------------------------------
def prepare_input(
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
):

    input_data = [[
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
    ]]

    return input_data


# ----------------------------------------
# Display Prediction Result
# ----------------------------------------
def display_price(price):

    print("\n💰 Predicted Charging Price: ₹", round(price, 2), "/kWh")

    if price < 9:
        print("🟢 Cheap Charging Period")
    elif price < 12:
        print("🟡 Moderate Charging Cost")
    else:
        print("🔴 Expensive Charging Period")