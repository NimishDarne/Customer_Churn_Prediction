# Customer Churn Prediction

A machine learning project that predicts whether a telecom customer is likely to leave a service provider using customer demographics, subscription details, contract information, and billing data.

The project includes exploratory data analysis, preprocessing, model comparison, hyperparameter tuning, threshold selection, and an interactive Streamlit application.

## Problem Statement

Customer churn can affect a telecom company's revenue and customer retention. Identifying customers who may leave can help businesses prioritize retention efforts.

This project uses historical customer data to estimate churn probability and classify customers as likely to churn or likely to stay.

## Features

- Exploratory data analysis and visualization
- Data cleaning and preprocessing
- Categorical encoding and numerical scaling
- Logistic Regression and Random Forest experiments
- Stratified cross-validation and hyperparameter tuning
- Prediction threshold analysis
- Saved scikit-learn pipeline
- Interactive Streamlit application with input validation and risk categories

## Dataset

The project uses the Telco Customer Churn dataset, containing 7,043 customer records and 21 original columns.

The target variable is `Churn`:
- `Yes`: customer churned
- `No`: customer stayed

The `customerID` column is excluded from the model features. The final feature set contains 19 columns.

Dataset source: [IBM Sample Data Sets — Telco Customer Churn](https://www.ibm.com/docs/en/cognos-analytics/11.1.0?topic=samples-telco-customer-churn)

Please ensure you have the right to redistribute the dataset before including it in this repository.

## Methodology

1. Inspected the dataset and analyzed churn distribution.
2. Investigated data quality issues, including invalid `TotalCharges` values.
3. Separated the target variable from the input features.
4. Used a scikit-learn `ColumnTransformer` to one-hot encode categorical features and scale numerical features.
5. Compared Logistic Regression and Random Forest using stratified five-fold cross-validation.
6. Tuned hyperparameters with `RandomizedSearchCV`.
7. Compared classification thresholds using out-of-fold predictions on the training data.
8. Evaluated the selected Logistic Regression pipeline on a held-out test set.

The final selected pipeline uses balanced Logistic Regression with `C=0.5`. The application uses a classification threshold of `0.6`.

## Model Evaluation

Final held-out test results at threshold `0.6`:

| Metric | Score |
|---|---:|
| Accuracy | 76.30% |
| Precision | 54.10% |
| Recall | 70.59% |
| F1-score | 61.25% |
| ROC-AUC | 84.16% |

### Confusion Matrix

| | Predicted stay | Predicted churn |
|---|---:|---:|
| Actual stay | 811 | 224 |
| Actual churn | 110 | 264 |

The model identified 264 of 374 actual churners in the test set. It also flagged 224 customers who ultimately stayed, so the predictions should be used to support—not replace—business judgment.

## Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Customer_Churn_Prediction
```

Replace the placeholder with your actual repository URL.

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Launch the application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`.

## Project Structure

```text
Customer_Churn_Prediction/
├── app.py
├── requirements.txt
├── models/
│   └── churn_pipeline.joblib
├── data/
├── notebooks/
└── README.md
```

Your existing notebooks and folders may contain additional files.

## Limitations

- Performance depends on the quality and representativeness of the dataset.
- The threshold of `0.6` was selected by comparing F1-scores across a limited set of thresholds; it has not been validated against real business costs.
- Risk categories displayed in the app are illustrative, not validated business risk bands.
- The model estimates patterns from historical data and does not establish why an individual customer might leave.
- Performance may change when applied to new customers or different telecom providers.

## Future Improvements

- Evaluate additional models and calibration methods.
- Test threshold choices using business costs and retention campaign capacity.
- Add automated tests and stronger input validation.
- Deploy the application and monitor performance over time.

## Technologies

Python, pandas, scikit-learn, joblib, Streamlit, Matplotlib, and Seaborn.
