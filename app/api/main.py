from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from smart_input_encoder import encode_input

# Load model
model = joblib.load("models/optimized_model.pkl")

# Load expected feature order  
with open("feature_order.txt", "r", encoding="cp1252") as f:
    expected_features = [line.strip() for line in f.readlines()]

# Load reference data
reference_df = pd.read_csv("data/get_around_pricing_project.csv")

# Define input schema
class FriendlyInput(BaseModel):
    mileage: int
    engine_power: int
    private_parking_available: bool
    has_gps: bool
    has_air_conditioning: bool
    automatic_car: bool
    has_getaround_connect: bool
    has_speed_regulator: bool
    winter_tires: bool
    model_key: str
    fuel: str
    paint_color: str
    car_type: str

# Create app
app = FastAPI()  # Enable default /docs
# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Getaround Pricing API!"}
# Mount the static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Redirect /docs to the custom HTML
@app.get("/docs", include_in_schema=False)
def custom_docs():
    return RedirectResponse(url="/static/docs.html")

# Keep Swagger UI at /swagger
@app.get("/swagger", include_in_schema=False)
def swagger_ui():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Swagger UI")

# Prediction route

@app.post("/predict")
def predict(input_data: FriendlyInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data.dict()])

    # Encode input
    encoded_input = encode_input(input_df, reference_df)

    # Reorder features
    encoded_input = encoded_input[expected_features]

    # Make prediction
    prediction = model.predict(encoded_input)[0]

    return {"predicted_price": round(prediction, 2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)