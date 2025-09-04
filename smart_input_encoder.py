import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
import joblib
import os

def encode_input(user_input: dict, reference_df: pd.DataFrame):
    reference_df = reference_df.drop(columns=["Unnamed: 0", "rental_price_per_day"])
    input_df = pd.DataFrame([user_input])
    input_encoded = pd.get_dummies(input_df)
    reference_encoded = pd.get_dummies(reference_df)
    input_encoded = input_encoded.reindex(columns=reference_encoded.columns, fill_value=0)
    return input_encoded.values.tolist()[0], reference_encoded.columns.tolist()

if __name__ == "__main__":
    # Load data
    df = pd.read_csv("data/get_around_pricing_project.csv")

    # Prepare training data
    X = df.drop(columns=["Unnamed: 0", "rental_price_per_day"])
    X = pd.get_dummies(X)
    expected_features = X.columns.tolist()

    # Save feature order
    with open("feature_order.txt", "w") as f:
        for feature in expected_features:
            f.write(f"{feature}\n")

    # Continue with training
    y = df["rental_price_per_day"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train optimized model
    best_model = XGBRegressor(
        learning_rate=0.1,
        max_depth=5,
        n_estimators=300,
        subsample=1.0,
        random_state=42
    )
    best_model.fit(X_train, y_train)

    # Evaluate
    y_pred = best_model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Optimized RMSE: {rmse:.2f}")
    print(f"Optimized MAE: {mae:.2f}")
    print(f"Optimized R² Score: {r2:.2f}")

    # Save model locally
    joblib.dump(best_model, "optimized_model.pkl")

    # Log to MLflow
    mlflow.set_experiment("getaround_pricing")
    with mlflow.start_run(run_name="xgboost_optimized"):
        mlflow.log_params({
            "learning_rate": 0.1,
            "max_depth": 5,
            "n_estimators": 300,
            "subsample": 1.0,
            "random_state": 42
        })
        mlflow.log_metrics({
            "optimized_rmse": rmse,
            "optimized_mae": mae,
            "optimized_r2": r2
        })
        mlflow.sklearn.log_model(best_model, "optimized_model")

        # Sample input
        user_input = {
            "mileage": 12000,
            "engine_power": 110,
            "private_parking_available": True,
            "has_gps": True,
            "has_air_conditioning": True,
            "automatic_car": True,
            "has_getaround_connect": True,
            "has_speed_regulator": True,
            "winter_tires": True,
            "model_key": "Toyota",
            "fuel": "petrol",
            "paint_color": "black",
            "car_type": "suv"
        }

        encoded_input, feature_order = encode_input(user_input, df)
        print("Encoded input:", encoded_input)
        print("Feature order:", feature_order)

        # Save and log feature order
        with open("feature_order.txt", "w") as f:
            for feature in feature_order:
                f.write(f"{feature}\n")
        mlflow.log_artifact("feature_order.txt")

    # Optional: Start MLflow UI (Windows only)
    os.system("start mlflow ui")


