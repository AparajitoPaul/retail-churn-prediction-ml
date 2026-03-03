# Retail Customer Churn Prediction  
Time-Aware Machine Learning with Revenue Optimization

---

## Project Overview

This project develops a production-style, time-aware churn prediction system using over 1 million retail transactions across approximately 6,000 customers.

Unlike typical churn projects, this implementation:

- Uses forward-looking time-based labeling to prevent target leakage  
- Engineers advanced behavioral features  
- Compares multiple machine learning models  
- Applies model explainability techniques  
- Translates churn probability into revenue-at-risk  
- Simulates retention campaign return on investment  

The objective is not just prediction accuracy, but financially optimized customer targeting.

---

## Business Objective

As of a defined cutoff date:

- Identify customers likely to churn within the next 90 days  
- Prioritize retention efforts to maximize revenue impact  

The project integrates predictive modeling with strategic financial decision-making.

---

## Time-Based Churn Definition

- Cutoff Date: 2011-09-01  
- Prediction Window: 90 days  

A customer is labeled as churned if they make no purchase within 90 days after the cutoff date.

Historical data is used for feature engineering, while future data defines churn labels. This separation ensures leakage-free validation and realistic performance estimates.

---

## Methodology

### 1. Raw Data Audit
- Validated schema and time coverage  
- Checked missing values and duplicates  
- Confirmed suitability for churn modeling  

### 2. Data Cleaning
- Removed cancelled invoices  
- Removed negative quantity and price transactions  
- Dropped records with missing Customer IDs  
- Created revenue feature (Quantity × UnitPrice)  

### 3. Time-Based Labeling
- Separated historical window for features  
- Used forward window for churn definition  

### 4. Advanced Feature Engineering

Customer-level behavioral features include:

- Recency, Frequency, Monetary (RFM)  
- Interpurchase gap mean and volatility  
- Basket size mean and variability  
- Revenue trend (linear regression slope)  
- Product diversity ratio  
- Seasonality ratio  

These features capture engagement decay, stability, and spending behavior.

### 5. Model Training

Compared the following models:

- Logistic Regression  
- Random Forest  
- XGBoost  

### 6. Model Evaluation

Evaluation metrics:

- ROC-AUC (~0.79)  
- F1 Score (~0.76)  
- Precision@Top15% (~0.90)  
- Recall@Top15% (~0.23)  

Logistic Regression performed best under leakage-free validation.

### 7. Revenue-at-Risk Optimization

Initial strategy (probability-only targeting):
- Captured approximately 2% of revenue  
- Produced negative ROI  

Improved strategy:

RiskScore = ChurnProbability × MonetaryValue

Results:
- Captured approximately 41% of revenue-at-risk  
- Achieved approximately 7.6x simulated ROI  

This demonstrates the importance of aligning predictive analytics with financial prioritization.

---

## Key Findings

- Recency is the strongest churn driver  
- Behavioral instability predicts churn more strongly than raw frequency  
- Higher monetary value reduces churn probability  
- Probability-only targeting is financially misleading  
- Revenue-weighted targeting significantly improves profitability  
- Time-based validation prevents artificially inflated performance  

---

## Project Structure

Retail_Churn_Prediction/
│
├── data/
│   ├── raw/
│   │   └── README.md
│   ├── processed/
│   │   └── README.md
│
├── models/
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_churn_definition.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_model_evaluation.ipynb
│   ├── 07_model_explainability.ipynb
│   ├── 08_business_simulation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── churn.py
│   ├── features.py
│   ├── modeling.py
│   ├── evaluation.py
│
├── requirements.txt
└── README.md

The structure follows modular machine learning engineering practices, separating raw data, processed data, feature engineering, modeling, and evaluation.

---

## Data Access

Due to GitHub file size limitations, raw and processed datasets are hosted externally.

See:
- data/raw/README.md  
- data/processed/README.md  

for download instructions and expected folder structure.

---

## Environment Setup

Clone the repository:

git clone <repository-link>
cd Retail_Churn_Prediction

Install dependencies:

pip install -r requirements.txt

Download datasets from the Google Drive link and place them inside:

data/raw/  
data/processed/

Then run notebooks sequentially.

---

## Skills Demonstrated

- Time-Series Aware Churn Modeling  
- Advanced Behavioral Feature Engineering  
- Classification and Ranking Metrics  
- Model Explainability  
- Revenue Impact Simulation  
- ROI Optimization Strategy  
- Modular ML Project Architecture  

---

## Author

Aparajito Paul  
MBA (Marketing) | Data Science (IIT Madras)  
Transitioning into Data Analytics and Machine Learning
