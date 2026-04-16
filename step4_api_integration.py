# API SERVER FOR SMART EV CHARGING (AI + IoT)

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# Create FastAPI app
app = FastAPI()

# Load trained AI model
model_path = os.path.join(os.path.dirname(__file__), "E:\\PROJECT FILE\\PROJECT 16 - Smart_EV_charging\\models\\pricing_model.pkl")
model = joblib.load(model_path)

print("✅ AI Model Loaded Successfully")


# ----------------------------------------
# Request Body Schema
# ----------------------------------------
class InputData(BaseModel):
    time_hour: float
    power_W: float
    energy_kWh: float
    demand_level: float
    grid_load: float


# ----------------------------------------
# Home Route
# ----------------------------------------
@app.get("/")
def home():
    return {"message": "Smart EV Charging AI Server Running ⚡"}


# ----------------------------------------
# Prediction Route
# ----------------------------------------
@app.post("/predict")
def predict(data: InputData):

    try:
        input_data = [[
            data.time_hour,
            data.power_W,
            data.energy_kWh,
            data.demand_level,
            data.grid_load
        ]]

        predicted_price = model.predict(input_data)[0]

        return {
            "predicted_price_rs_per_kWh": round(float(predicted_price), 2),
            "status": "success"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# ----------------------------------------
# Run server (IMPORTANT)
# ----------------------------------------
# Run this from terminal:
# uvicorn main:app --reload