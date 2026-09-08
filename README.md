# OIBSIP

## Oasis Infobyte Internship — Data Analytics

This repository contains my **Oasis Infobyte Internship** projects for the Data Analytics track. The projects cover exploratory data analysis, customer segmentation, and machine-learning-based fraud detection.

## 📊 Data Analytics Projects

### Level 1

#### Task 1 — EDA on Retail Sales Data
`DataAnalytics-L1-EDARetailSales/`

Exploratory Data Analysis of retail sales data, including data cleaning, descriptive statistics, sales trends, visualisations, findings, and business recommendations.

#### Task 2 — Online Retail Customer Segmentation
`DataAnalytics-L1-CustomerSegmentation/`

Customer segmentation using the UCI Online Retail dataset, RFM analysis and K-Means clustering. The project includes data preparation, exploratory analysis, feature engineering, standardisation, the Elbow Method, silhouette scoring, cluster profiling, visualisation, and marketing recommendations.

### Level 2

#### Task 1 — Fraud Detection with Machine Learning
`DataAnalytics-L2-FraudDetection/`

Machine-learning fraud detection on a heavily imbalanced financial transaction dataset. The project uses exploratory data analysis, stratified train-test splitting, feature scaling, SMOTE oversampling, Logistic Regression and Random Forest models. Models are evaluated using Precision, Recall, F1-score and ROC-AUC, with confusion matrices, ROC curves and Random Forest feature importance included.

**Key result:** Random Forest achieved the strongest overall balance, with **80.0% precision, 85.7% recall, 82.8% F1-score and 97.8% ROC-AUC** on the test set.

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- imbalanced-learn
- Jupyter Notebook
- Git & GitHub
- Git LFS

## 📁 Repository Structure

```text
OIBSIP/
├── README.md
├── DataAnalytics-L1-EDARetailSales/
├── DataAnalytics-L1-CustomerSegmentation/
│   ├── README.md
│   ├── requirements.txt
│   ├── data/
│   └── notebooks/
└── DataAnalytics-L2-FraudDetection/
    ├── README.md
    ├── requirements.txt
    ├── data/
    │   ├── README.md
    │   └── creditcard.csv
    ├── notebooks/
    │   ├── Fraud_Detection_Machine_Learning.ipynb
    │   └── Fraud_Detection_SMOTE_Logistic_RF.ipynb
    └── results/
        ├── Fraud_Detection_Results.md
        ├── class_distribution.svg
        ├── confusion_matrices.svg
        ├── feature_importance.svg
        ├── model_metrics.csv
        ├── random_forest_feature_importance.csv
        ├── results_summary.json
        └── roc_curve.svg
```

> **Note:** The fraud-detection dataset is tracked with **Git LFS** because the CSV is larger than GitHub's standard file-size limit.

## 🎯 Internship Goal

The goal of these projects is to strengthen practical data analytics and machine-learning skills by completing end-to-end projects—from data preparation and exploratory analysis to visualisation, modelling, evaluation, interpretation and business recommendations.

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Aspiring Quantitative Analyst
