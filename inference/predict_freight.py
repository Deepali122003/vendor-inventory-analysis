import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "freight_cost_prediction" / "models" / "predict_freight_model.pkl"

def load_model(model_path=MODEL_PATH):
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

def predict_freight_cost(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df["Predicted_Freight"] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":
    sample_data = {
        "Quantity":[100,50,25],
        "Dollars": [18000, 9000, 3000]
    }

    prediction = predict_freight_cost(sample_data)
    print(prediction)