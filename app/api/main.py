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
import os

# Get the absolute path to the root folder
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
feature_path = os.path.join(base_dir, "feature_order.txt")

# Load expected feature order
with open(feature_path, "r", encoding="cp1252") as f:
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

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Getaround Pricing API!"}

# Prediction route
@app.post("/predict")
def predict(data: FriendlyInput):
    user_input = data.dict()
    encoded_input, input_features = encode_input(user_input, reference_df)
    input_vector = pd.Series(encoded_input, index=input_features).reindex(expected_features, fill_value=0).values
    prediction = model.predict([input_vector])
    return {"prediction": prediction.tolist()}


