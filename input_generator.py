import pandas as pd

def generate_sample_input():
    # Load and preprocess the data
    df = pd.read_csv("data/get_around_pricing_project.csv")
    df.drop(columns=["Unnamed: 0", "rental_price_per_day"], inplace=True)
    df_encoded = pd.get_dummies(df, drop_first=True)

    # Get feature names
    feature_names = df_encoded.columns.tolist()

    # Create a sample input with reasonable defaults
    sample = [12000, 110]  # mileage, engine_power
    sample += [0] * (len(feature_names) - 2)  # fill rest with zeros

    return sample, feature_names

if __name__ == "__main__":
    sample_input, feature_names = generate_sample_input()
    print("Sample input:", sample_input)
    print("Feature order:", feature_names)
