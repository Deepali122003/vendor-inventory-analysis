# 📦 Inventory Analysis Project

## Overview

The **Inventory Analysis Project** is a machine learning-based analytics system designed to extract insights from inventory, purchase, and vendor invoice data. It uses a SQLite database as the data source and provides predictive models for freight cost estimation and invoice risk detection.


## 🌐 Live Demo

🚀 **Streamlit Application:**  
https://vendor-inventory-analysis.streamlit.app/

---

## Features

- 📊 Inventory and purchase data analysis
- 🚚 Freight cost prediction using regression models
- 🚩 Invoice risk flagging using classification models
- 🗄️ SQLite database integration
- 🤖 Machine learning model training and evaluation
- 💾 Model serialization with Joblib
- 🔮 Inference scripts for making predictions

---

## Project Structure

```text
Inventory-analysis-project/
│
├── data/
│   └── inventory.db
│
├── freight_cost_prediction/
│   ├── train.py
│   ├── data_preprocessing.py
│   ├── modeling_evaluation.py
│   └── models/
│       └── predict_freight_model.pkl
│
├── invoice_flagging/
│   ├── train.py
│   ├── data_preprocessing.py
│   ├── modeling_evaluation.py
│   └── models/
│       ├── predict_flag_invoice.pkl
│       └── scaler.pkl
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── notebooks/
├── requirements.txt
└── README.md
```

---

## Dataset

The project uses a SQLite database:

```text
data/inventory.db
```

### Tables Used

- `vendor_invoice`
- `purchases`

---

# 🚚 Freight Cost Prediction

Predicts freight cost from invoice and purchase information.

### Models Implemented

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Train Model

```bash
python freight_cost_prediction/train.py
```

### Saved Model

```text
freight_cost_prediction/models/predict_freight_model.pkl
```

---

# 🚩 Invoice Risk Flagging

Identifies potentially risky invoices based on invoice and purchase attributes.

### Models Implemented

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Evaluation Metrics

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1 Score

### Features Used

- invoice_quantity
- invoice_dollars
- Freight
- total_item_quantity
- total_item_dollars

### Train Model

```bash
python invoice_flagging/train.py
```

### Saved Files

```text
invoice_flagging/models/predict_flag_invoice.pkl
invoice_flagging/models/scaler.pkl
```

---

# 🔮 Inference

## Freight Cost Prediction

Run:

```bash
python inference/predict_freight.py
```

Example Input:

```python
sample_data = {
    "Dollars": [18000, 9000, 3000]
}
```

---

## Invoice Risk Prediction

Run:

```bash
python inference/predict_invoice_flag.py
```

Example Input:

```python
sample_data = {
    "invoice_quantity": [100, 50, 25],
    "invoice_dollars": [18000, 9000, 3000],
    "Freight": [500, 250, 100],
    "total_item_quantity": [98, 48, 25],
    "total_item_dollars": [17995, 8990, 3005]
}
```

Output:

- **0** → Normal Invoice
- **1** → Potentially Risky Invoice

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- SQLite3
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib

---

# ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd Inventory-analysis-project
```

Create a virtual environment:

```bash
conda create -n inventory_env python=3.11
conda activate inventory_env
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔄 Machine Learning Workflow

1. Load inventory and invoice data from SQLite.
2. Perform feature engineering and preprocessing.
3. Split data into training and testing sets.
4. Train multiple machine learning models.
5. Evaluate model performance.
6. Select the best-performing model.
7. Save the trained model using Joblib.
8. Use inference scripts for prediction.

---

# 🚀 Future Enhancements

- Streamlit dashboard for visualization
- FastAPI deployment
- Real-time invoice monitoring
- Advanced anomaly detection
- Model explainability with SHAP
- Docker containerization
- Cloud deployment

---

## 👨‍💻 Author

**Deepali Talreja**

---

## 📄 License

This project is intended for educational and analytical purposes.
