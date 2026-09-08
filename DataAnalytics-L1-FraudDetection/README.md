# 💳 Fraud Detection — Machine Learning

This project implements **Oasis Infobyte Data Analytics — Level 1, Task 3: Fraud Detection**.

## Objective
Build a machine-learning pipeline that detects fraudulent financial transactions in a heavily imbalanced dataset. The project focuses on appropriate evaluation metrics, class-imbalance handling, model comparison and practical scalability.

## Dataset
The recommended benchmark is the **Credit Card Fraud Detection** dataset containing 284,807 transactions, including 492 fraudulent transactions.

Because the raw CSV is large, it is **not committed to this repository**. Download the dataset and place it here:

```text
data/creditcard.csv
```

See `data/README.md` for the expected filename and setup instructions.

## What the notebook covers

1. Dataset loading and inspection
2. Class-imbalance analysis and fraud percentage
3. Transaction-amount EDA
4. Approximate time-of-day analysis
5. Stratified train/test split
6. SMOTE oversampling applied only to the training pipeline
7. Logistic Regression
8. Random Forest
9. Precision, Recall, F1-score and ROC-AUC
10. Confusion matrices and ROC curve
11. Random Forest feature importance
12. Precision vs Recall discussion
13. Scalability discussion for 1 million transactions/hour

## Project structure

```text
OIBSIP/
└── DataAnalytics-L1-FraudDetection/
    ├── README.md
    ├── requirements.txt
    ├── data/
    │   └── README.md
    └── notebooks/
        └── Fraud_Detection_Machine_Learning.ipynb
```

## Tools

- Python
- Pandas
- NumPy
- Scikit-learn
- imbalanced-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/Fraud_Detection_Machine_Learning.ipynb
```

Then place `creditcard.csv` inside `data/` and run the notebook from top to bottom.

## Important note

This is an educational internship project. Model performance should not be interpreted as production-ready fraud detection without additional validation, threshold optimisation, monitoring, security controls and domain-specific cost analysis.
