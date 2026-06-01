# 🏦 AI-Powered Loan Default Risk Prediction & Credit Scoring System

## 📌 Project Overview

An end-to-end Machine Learning system that predicts loan default risk, generates borrower credit scores, categorizes risk levels, and provides automated loan approval recommendations.

Built using the Lending Club dataset containing 390K+ loan records, this project demonstrates a complete production-grade ML workflow including data preprocessing, feature engineering, model training, explainability, API deployment, and Dockerization.

> ⚠️ Dataset not included in this repository due to GitHub file size limitations. Please download the Lending Club dataset manually and place `loan.csv` inside `data/raw/`.
---


## 🚀 Key Features

* Loan Default Prediction
* Credit Risk Analysis
* Credit Score Generation (300–900)
* Risk Categorization
* Loan Approval Recommendation Engine
* Explainable AI using SHAP
* SMOTE for Class Imbalance Handling
* FastAPI REST API
* Docker Deployment
* Production ML Pipeline

---

## 🏗️ Project Architecture

User Input
↓
Feature Engineering
↓
Preprocessing Pipeline
↓
XGBoost Model
↓
Default Probability
↓
Credit Score
↓
Risk Classification
↓
Approval Recommendation
↓
FastAPI Response

---

## 📊 Dataset

### Lending Club Loan Dataset

Features include:

* Loan Amount
* Interest Rate
* Annual Income
* Debt-to-Income Ratio
* Employment Length
* Home Ownership
* FICO Score
* Credit Utilization
* Loan Purpose
* Verification Status

Target Variable:

* Fully Paid → 0
* Charged Off → 1

---

## 🛠️ Tech Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost
* Imbalanced-Learn (SMOTE)

### Explainability

* SHAP

### Deployment

* FastAPI
* Uvicorn

### Containerization

* Docker

---

## 📂 Project Structure

```text
loan-default-prediction/
│
├── api/
│   ├── __init__.py
│   ├── app.py
│   └── schemas.py
│
├── src/
│   ├── __init__.py
│   ├── predict.py
│   ├── scoring.py
│   └── feature_engineering.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── xgb_model.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_explainability.ipynb
│
├── reports/
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/loan-default-risk-prediction-system.git

cd loan-default-risk-prediction-system
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Dataset

This project uses the publicly available Lending Club Loan Dataset.

### Download Dataset

Download the dataset from:

https://www.kaggle.com/datasets/wordsforthewise/lending-club

After downloading, extract the archive.

You will find files similar to:

```text
accepted_2007_to_2018Q4.csv.gz
rejected_2007_to_2018Q4.csv.gz
```

Extract the files and locate:

```text
accepted_2007_to_2018Q4.csv
```

This project only uses the accepted loans dataset.

### Project Dataset Setup

Rename:

```text
accepted_2007_to_2018Q4.csv
```

to:

```text
loan.csv
```

Then move it to:

```text
loan-default-prediction/
└── data/
    └── raw/
        └── loan.csv
```

Final structure:

```text
data/
└── raw/
    └── loan.csv
```

### Important Note

The original Lending Club dataset is very large (multiple GBs) and is intentionally excluded from this repository using `.gitignore`.

To run this project, users must download the dataset manually and place it in the `data/raw/` directory.

### Loading Sample

For systems with limited RAM, load only a subset of the dataset:

```python
df = pd.read_csv(
    "data/raw/loan.csv",
    low_memory=False,
    nrows=500000
)
```

This project was developed using the first 500,000 records from the Lending Club dataset.

---

## 📈 Model Development Workflow

### Data Cleaning

* Missing Value Handling
* Leakage Removal
* Target Engineering

### Feature Engineering

* Loan-to-Income Ratio
* Average FICO Score
* Monthly Income
* Installment Income Ratio
* Credit Utilization

### Handling Class Imbalance

* SMOTE Oversampling

### Models Trained

* Logistic Regression
* Random Forest
* XGBoost

---

## 📊 Model Performance

| Model               | ROC-AUC |
| ------------------- | ------- |
| Logistic Regression | 0.727   |
| Random Forest       | 0.717   |
| XGBoost             | 0.727   |

### Selected Production Model

✅ XGBoost Classifier

Reason:

* Better probability estimates
* Strong performance on tabular data
* Supports explainability via SHAP
* Industry-standard for credit risk modeling

---

## 🧠 Explainable AI

SHAP was used to explain model predictions.

Important features identified:

* Interest Rate
* Debt-to-Income Ratio
* FICO Score
* Loan Amount
* Credit Utilization

This improves transparency and trust in loan approval decisions.

---

## 💳 Credit Score Engine

Default probability is converted into a credit score.

Formula:

```python
score = 900 - (default_probability * 600)
```

Score Range:

| Score     | Risk        |
| --------- | ----------- |
| 800+      | Low Risk    |
| 650–799   | Medium Risk |
| Below 650 | High Risk   |

---

## 🤖 Loan Recommendation Logic

| Credit Score | Recommendation |
| ------------ | -------------- |
| 800+         | Approve        |
| 650–799      | Review         |
| Below 650    | Reject         |

---

## 🚀 FastAPI Deployment

Run API

```bash
uvicorn api.app:app --reload
```

Open Swagger UI

```text
http://localhost:8000/docs
```

---

## Sample Request

```json
{
  "loan_amnt": 10000,
  "term": "36 months",
  "int_rate": 10.5,
  "installment": 325,
  "annual_inc": 70000,
  "dti": 15.2,
  "emp_length": "10+ years",
  "home_ownership": "MORTGAGE",
  "purpose": "debt_consolidation",
  "fico_range_low": 700,
  "fico_range_high": 704,
  "open_acc": 12,
  "pub_rec": 0,
  "revol_bal": 15000,
  "revol_util": 40.2,
  "mort_acc": 2,
  "grade": "B",
  "sub_grade": "B2",
  "verification_status": "Verified",
  "inq_last_6mths": 1,
  "delinq_2yrs": 0
}
```

---

## Sample Response

```json
{
  "default_probability": 0.17,
  "credit_score": 798,
  "risk_level": "Medium Risk",
  "recommendation": "Review"
}
```

---

## 🐳 Docker Support

Build Image

```bash
docker build -t loan-risk-api .
```

Run Container

```bash
docker run -p 8000:8000 loan-risk-api
```

---

## 📌 Resume Highlights

* Developed an end-to-end Loan Default Risk Prediction System using XGBoost and SHAP.
* Engineered business-focused credit risk features on 390K+ loan records.
* Implemented SMOTE-based imbalance handling and model explainability.
* Built a credit scoring and risk categorization engine.
* Deployed the model through FastAPI and Docker for real-time predictions.

---

## 🔮 Future Enhancements

* Streamlit Dashboard
* Model Monitoring
* MLflow Tracking
* CI/CD Pipeline
* Cloud Deployment (AWS/GCP/Azure)
* Real-time Risk Monitoring

---

## ⭐ If you found this project useful, consider starring the repository.
