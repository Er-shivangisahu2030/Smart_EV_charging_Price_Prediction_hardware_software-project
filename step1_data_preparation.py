# STEP 1: DATA PREPARATION

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\ev_dynamic_pricing_60days.csv")

print("✅ Dataset Loaded Successfully\n")

# Show first rows
print("🔹 First 5 rows:")
print(data.head(), "\n")

# Dataset info
print("🔹 Dataset Info:")
print(data.info(), "\n")

# Statistical summary
print("🔹 Statistical Summary:")
print(data.describe(), "\n")

# Check missing values
print("🔹 Missing Values:")
print(data.isnull().sum(), "\n")

# Remove duplicates if any
data = data.drop_duplicates()

# Feature columns
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

# Target column
y = data["price_rs_per_kWh"]

print("🔹 Features Sample:")
print(X.head(), "\n")

print("🔹 Target Sample:")
print(y.head(), "\n")

# Correlation with price
print("🔹 Correlation with Price:")
print(data.corr()["price_rs_per_kWh"].sort_values(ascending=False), "\n")

# Plot 1: Dynamic Pricing vs Time
plt.figure(figsize=(10, 5))
plt.plot(data["time_hour"], data["price_rs_per_kWh"], marker='o')
plt.xlabel("Time of Day (Hour)")
plt.ylabel("Price (Rs/kWh)")
plt.title("Dynamic Pricing vs Time")
plt.grid(True)
plt.show()

# Plot 2: Grid Load vs Price
plt.figure(figsize=(10, 5))
plt.scatter(data["grid_load"], data["price_rs_per_kWh"])
plt.xlabel("Grid Load")
plt.ylabel("Price (Rs/kWh)")
plt.title("Grid Load vs Price")
plt.grid(True)
plt.show()

# Plot 3: Demand Level vs Price
plt.figure(figsize=(10, 5))
plt.scatter(data["demand_level"], data["price_rs_per_kWh"])
plt.xlabel("Demand Level")
plt.ylabel("Price (Rs/kWh)")
plt.title("Demand Level vs Price")
plt.grid(True)
plt.show()

print("✅ Data Preparation Completed Successfully")