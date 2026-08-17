# Exploratory Data Analysis Report

## Churn Distribution

- 5174 customers stayed.
- 1869 customers left.
- Churn rate is approximately 26.5%.
- The dataset is moderately imbalanced.

---

## Gender

- Male and Female customers are almost equally distributed.
- No significant gender imbalance is observed.

---

## Contract

- Month-to-month contracts are the most common.
- One-year contracts are the least common.
- Long-term contracts may reduce customer churn. This is a hypothesis that will be tested later.

---

## Internet Service

- Fiber optic is the most commonly used internet service.
- DSL is the second most common.
- Some customers do not use internet service.

---

## Initial Business Insights

- Most customers remain with the company.
- Contract type appears to be an important feature.
- Customer retention strategies may be especially useful for month-to-month customers.

Numerical Feature Insights

- Customers who churned have a higher median MonthlyCharges than customers who stayed.
- Customers who churned generally have much lower tenure than customers who stayed.
- Shorter tenure appears to be strongly associated with churn.
- Higher MonthlyCharges appear to be associated with higher churn.

Payment Method Insights

- Electronic check has the highest churn rate among the payment methods.
- Mailed check, bank transfer and credit card have substantially lower churn rates.
- Payment method appears to be a potentially useful feature for prediction.

Overall EDA Insights

The strongest patterns observed so far are:
1. Contract type
2. Tenure
3. MonthlyCharges
4. TechSupport
5. PaymentMethod
6. InternetService

These relationships are hypotheses based on exploratory analysis and do not prove causation.