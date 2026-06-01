import joblib

from src.scoring import (generate_credit_score,risk_category,recommendation)
from src.feature_engineering import create_features


model = joblib.load("models/xgb_model.pkl")

def predict_customer(data):
    data = create_features(data)
    probability = model.predict_proba(data)[0][1]
    score = generate_credit_score(probability)

    return {
        "default_probability": round(float(probability),4),
        "credit_score": score,
        "risk_level": risk_category(score),
        "recommendation": recommendation(score)
    }