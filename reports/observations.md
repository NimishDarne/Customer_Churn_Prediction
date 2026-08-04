# Customer Churn Dataset
Dataset Shape - (7043, 21)

Target Column - 'Churn'

Numeric Columns - 'SeniorCitizen', 'tenure', 'MonthlyCharges', out of which the seniorcitizen is encoded feature

Categorical Columns - 'gender',	'Partner	Dependents', 'PhoneService',	'MultipleLines',	'InternetService',	'OnlineSecurity',	'OnlineBackup',	'DeviceProtection',	'TechSupport',	'StreamingTV',	'StreamingMovies',	'Contract',	'PaperlessBilling',	'PaymentMethod',	'TotalCharges',	'Churn'.

Interesting Things I Found - - TotalCharges has the data type object, but most of its values look like numbers.
- SeniorCitizen is stored as a number (0 and 1), but it actually represents categories (No and Yes).
- Around 26.5% of customers left the company.

Questions I Still Have -  Few doubts about the syntax and the methods that are used. 