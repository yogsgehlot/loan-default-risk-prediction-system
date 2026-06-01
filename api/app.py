from fastapi import FastAPI

import pandas as pd

from api.schemas import LoanRequest
from src.predict import predict_customer

app = FastAPI(title="Loan Default Prediction API",version="1.0.0")

@app.get("/")
def home():
    return {"message": "Loan Default Prediction API"}

@app.post("/predict")
def predict(payload: LoanRequest):
    data = pd.DataFrame([payload.dict()])
    result = predict_customer(data)
    return result