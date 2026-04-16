# STREAMLIT DASHBOARD
# Fancy Dynamic Pricing-Based Smart EV Charging using AI + IoT

import streamlit as st
import joblib
import pandas as pd
import datetime

# --------------------------------------------
# Page Configuration
# --------------------------------------------
st.set_page_config(
    page_title="Smart EV Charging Dashboard",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------
# Custom CSS
# --------------------------------------------
st.markdown("""
<style>
.big-price {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    padding: 20px;
    border-radius: 20px;
    background-color: #111827;
    color: #00FF99;
    box-shadow: 0px 0px 20px rgba(0,255,153,0.3);
}

.status-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}

.cheap {
    background-color: #d1fae5;
    color: #065f46;
}

.medium {
    background-color: #fef3c7;
    color: #92400e;
}

.expensive {
    background-color: #fee2e2;
    color: #991b1b;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------
# Title
# --------------------------------------------
st.title("⚡ AI-Based Smart EV Charging Dashboard")
st.markdown("### Real-Time Dynamic Pricing using AI + IoT")

# --------------------------------------------
# Load Model
# --------------------------------------------
model = joblib.load(
    r"E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\models\\pricing_model.pkl"
)

# --------------------------------------------
# Sidebar Inputs
# --------------------------------------------
st.sidebar.header("🔧 Input Parameters")

time_hour = st.sidebar.slider("Time of Day (Hour)", 0, 23, 18)
voltage_V = st.sidebar.slider("Voltage (V)", 220, 240, 230)
current_A = st.sidebar.slider("Current (A)", 0.10, 2.00, 1.00)
power_factor = st.sidebar.slider("Power Factor", 0.70, 1.00, 0.90)

# --------------------------------------------
# Derived Values
# --------------------------------------------
power_W = round(voltage_V * current_A * power_factor, 2)
energy_kWh = round(power_W / 1000, 3)

plant_capacity = 1500
grid_load = round(power_W / plant_capacity, 2)

peak_hour = 1 if 17 <= time_hour <= 21 else 0

if grid_load < 0.10:
    demand_level = 2
elif grid_load < 0.15:
    demand_level = 5
elif grid_load < 0.20:
    demand_level = 8
else:
    demand_level = 9

cumulative_energy_kWh = round(energy_kWh * (time_hour + 1), 3)

# --------------------------------------------
# Prediction
# --------------------------------------------
input_data = pd.DataFrame([{
    "time_hour": time_hour,
    "voltage_V": voltage_V,
    "current_A": current_A,
    "power_factor": power_factor,
    "power_W": power_W,
    "energy_kWh": energy_kWh,
    "cumulative_energy_kWh": cumulative_energy_kWh,
    "demand_level": demand_level,
    "grid_load": grid_load,
    "peak_hour": peak_hour
}])

predicted_price = model.predict(input_data)[0]

# --------------------------------------------
# Main Top Metrics
# --------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("⏰ Time", f"{time_hour}:00")
col2.metric("⚡ Power", f"{power_W} W")
col3.metric("🔋 Energy", f"{energy_kWh} kWh")
col4.metric("📊 Demand", demand_level)

# --------------------------------------------
# Big Price Card
# --------------------------------------------
st.markdown("---")
st.subheader("💰 Current Charging Price")

st.markdown(
    f"""
    <div class="big-price">
        ₹ {predicted_price:.2f} / kWh
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------
# Charging Recommendation
# --------------------------------------------
st.markdown("---")
st.subheader("🚦 Charging Recommendation")

if predicted_price < 9:
    st.markdown(
        '<div class="status-box cheap">🟢 Cheap Charging Period<br>Best Time to Charge</div>',
        unsafe_allow_html=True
    )
elif predicted_price < 12:
    st.markdown(
        '<div class="status-box medium">🟡 Moderate Charging Cost<br>Normal Charging Window</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<div class="status-box expensive">🔴 Expensive Charging Period<br>Avoid Peak Hours</div>',
        unsafe_allow_html=True
    )

# --------------------------------------------
# Progress Bars
# --------------------------------------------
st.markdown("---")
st.subheader("📈 Live System Indicators")

st.write("Grid Load")
st.progress(min(int(grid_load * 100), 100))

st.write("Demand Level")
st.progress(demand_level * 10)

st.write("Power Utilization")
st.progress(min(int((power_W / plant_capacity) * 100), 100))

# --------------------------------------------
# Detailed Metrics
# --------------------------------------------
st.markdown("---")
st.subheader("📊 Detailed System Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Voltage", f"{voltage_V} V")
c2.metric("Current", f"{current_A} A")
c3.metric("Power Factor", power_factor)
c4.metric("Peak Hour", "Yes" if peak_hour == 1 else "No")

# --------------------------------------------
# Formula Information
# --------------------------------------------
st.markdown("---")
st.subheader("🧮 Live Formula Calculations")

st.info(f"Power = {voltage_V} × {current_A} × {power_factor} = {power_W} W")
st.info(f"Grid Load = {power_W} / {plant_capacity} = {grid_load}")
st.info(f"Energy = {power_W} / 1000 = {energy_kWh} kWh")

# --------------------------------------------
# Trend Chart
# --------------------------------------------
st.markdown("---")
st.subheader("📉 Simulated Daily Price Trend")

hours = list(range(24))
prices = []

for h in hours:
    if h <= 5:
        prices.append(7.5)
    elif h <= 10:
        prices.append(9.0)
    elif h <= 16:
        prices.append(11.0)
    elif h <= 21:
        prices.append(13.5)
    else:
        prices.append(9.5)

trend_data = pd.DataFrame({
    "Hour": hours,
    "Predicted Price": prices
})

st.line_chart(trend_data.set_index("Hour"))

# --------------------------------------------
# Footer
# --------------------------------------------
st.markdown("---")
st.caption("⚡ Dynamic Pricing-Based Smart EV Charging using AI + IoT")