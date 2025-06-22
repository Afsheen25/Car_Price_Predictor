# 🚗 Car Price Prediction - End-to-End ML Project

This project is inspired by Chapter 2 of *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*. It demonstrates a complete machine learning pipeline applied to a real-world dataset.

## 📊 Problem

Predict the MSRP (price) of cars based on features like:
- Engine specs
- Brand
- MPG
- Year, etc.

## 🔧 ML Workflow

- ✅ Data Cleaning & Preprocessing
- ✅ Feature Engineering (`power_per_cylinder`, `mpg_ratio`)
- ✅ One-hot Encoding & Scaling Pipelines
- ✅ Model Training (Linear Regression, Random Forest, XGBoost)
- ✅ Hyperparameter Tuning using `RandomizedSearchCV`
- ✅ Evaluation using RMSE

## 🧠 Best Model

- **XGBoost Regressor**
- **Final RMSE on test set:** ~13,728

## 📁 Project Structure

```bash
CarPricePrediction/
├── car_price_predictor.pkl        # Final trained model
├── car_data.csv                   # Dataset
├── car_price_prediction.ipynb     # Notebook with all steps
├── app.py                         # (Optional) Streamlit app (not used)
└── README.md

📌 Notes
Used Scikit-Learn pipelines for clean preprocessing

Missing values handled by dropping few rows

Feature scaling & categorical encoding done properly

Model ready to be deployed!

Made with 💻 by Af