import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"

def load_model(model_path: str = MODEL_PATH):
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

def predict_invoice_flag(input_data):
    model = load_model()

    input_df = pd.DataFrame(input_data)
    input_df["Predicted_Flag"] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":
    sample_data = {
    "invoice_quantity": [100, 50, 25],
    "invoice_dollars": [18000, 9000, 3000],
    "Freight": [500, 250, 100],
    "total_item_quantity": [98, 48, 25],
    "total_item_dollars": [17995, 8990, 3005]
}

    prediction = predict_invoice_flag(sample_data)
    print(prediction)