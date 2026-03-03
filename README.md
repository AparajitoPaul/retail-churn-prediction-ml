\#  Retail Customer Churn Prediction  

\### Time-Based ML Modeling with Revenue Optimization



---



\##  Project Summary



Built a \*\*time-aware customer churn prediction system\*\* using 1M+ retail transactions across ~6,000 customers.



This project goes beyond model accuracy and connects churn predictions directly to \*\*revenue impact and retention ROI\*\*.



Key highlights:



\- Forward-looking churn labeling (leakage-free)

\- Advanced behavioral feature engineering

\- Model comparison (Logistic, RF, XGBoost)

\- SHAP-based explainability

\- Revenue-at-risk simulation

\- ROI-optimized targeting strategy



---



\##  Business Problem



As of a given cutoff date:



> Which customers are likely to churn in the next 90 days?



More importantly:



> How can churn predictions be translated into profitable retention strategy?



---



\##  Time-Based Churn Definition



\- \*\*Cutoff Date:\*\* 2011-09-01  

\- \*\*Prediction Window:\*\* 90 days  



A customer is labeled as churned if they make \*\*no purchase within 90 days after the cutoff date\*\*.



This approach mirrors real-world deployment and prevents target leakage.



---



\##  Modeling Procedure



\### 1. Raw Data Audit

\- Validated schema

\- Verified time coverage

\- Inspected missing values \& duplicates



\### 2️. Data Cleaning

\- Removed cancelled invoices

\- Removed negative quantity/price transactions

\- Dropped anonymous purchases

\- Created `Revenue = Quantity × UnitPrice`



\### 3️. Time-Based Churn Labeling

\- Historical window → Feature engineering

\- Future window → Churn definition



\### 4️. Feature Engineering



\#### RFM Features

\- Recency

\- Frequency

\- Monetary Value



\#### Behavioral Features

\- Interpurchase Gap Mean \& Std (volatility)

\- Basket Value Mean \& Std

\- Revenue Trend (linear regression slope)

\- Product Diversity Ratio

\- Seasonality Ratio



\### 5️. Model Training

Compared:

\- Logistic Regression

\- Random Forest

\- XGBoost



\### 6️. Model Evaluation

Metrics used:

\- ROC-AUC

\- F1 Score

\- Precision@Top15%

\- Recall@Top15%



\### 7️. Explainability

\- SHAP global importance

\- SHAP directionality analysis

\- Behavioral driver interpretation



\### 8️. Revenue-at-Risk Simulation

Converted churn probabilities into financial impact and optimized retention strategy.



---



\##  Model Performance



| Model | ROC-AUC | F1 Score | Precision@Top15% |

|-------|---------|----------|------------------|

| Logistic Regression | ~0.79 | ~0.76 | ~0.90 |

| Random Forest | ~0.77 | ~0.76 | ~0.87 |

| XGBoost | ~0.77 | ~0.76 | ~0.88 |



Logistic Regression slightly outperformed tree-based models under leakage-free validation.



---



\##  Key Findings



\###  1. Recency is the strongest churn driver

Customers with longer inactivity periods have significantly higher churn probability.



\###  2. Behavioral instability predicts churn

High volatility in purchase intervals increases churn risk.



\###  3. High-value customers are more stable

Higher monetary value reduces churn probability.



\###  4. Probability-only targeting can destroy ROI

Targeting top churn-probability customers captured only ~2% of total revenue and resulted in negative ROI.



\###  5. Revenue-weighted targeting improves ROI dramatically



Using:

RiskScore = ChurnProbability × MonetaryValue





\- Captured 41% of revenue-at-risk

\- Achieved 7.6x simulated ROI

\- Demonstrated strategic value of revenue-aligned targeting



---



\## 🏗 Project Structure
Retail\_Churn\_Prediction/

│

├── data/

│ ├── raw/

│ ├── processed/

│

├── notebooks/

│ ├── 01\_data\_loading.ipynb

│ ├── 02\_data\_cleaning.ipynb

│ ├── 03\_churn\_definition.ipynb

│ ├── 04\_feature\_engineering.ipynb

│ ├── 05\_model\_training.ipynb

│ ├── 06\_model\_evaluation.ipynb

│ ├── 07\_model\_explainability.ipynb

│ ├── 08\_business\_simulation.ipynb

│

├── src/

│ ├── preprocessing.py

│ ├── churn.py

│ ├── features.py

│ ├── modeling.py

│ ├── evaluation.py





This structure follows modular ML engineering best practices:

\- Separation of raw and processed data

\- Reusable feature engineering modules

\- Leakage-free modeling workflow

\- Reproducible training pipeline



---



\## 🧩 Skills Demonstrated



\- Time-Series Aware Churn Modeling

\- Advanced Behavioral Feature Engineering

\- Classification \& Ranking Metrics

\- SHAP Explainability

\- Revenue Impact Simulation

\- ROI Optimization Strategy

\- Modular ML Architecture



---



\##  Why This Project Stands Out



Most churn projects:

\- Use static labels

\- Ignore leakage

\- Stop at accuracy metrics



This project:

\- Implements forward-looking validation

\- Detects and corrects leakage

\- Connects ML outputs to financial outcomes

\- Optimizes targeting strategy for profitability



It demonstrates both \*\*technical depth and strategic thinking\*\*.



---



\##  Author



\*\*Aparajito Paul\*\*  

MBA (Marketing) | Data Science (IIT Madras)  

Transitioning into Data Analytics \& Machine Learning


