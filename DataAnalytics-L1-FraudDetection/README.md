# 💳 Fraud Detection — Machine Learning

This project implements **Oasis Infobyte Data Analytics — Level 1, Task 3: Fraud Detection**.

## Objective
Build a machine-learning pipeline to detect fraudulent financial transactions in a heavily imbalanced dataset, with emphasis on SMOTE, model comparison and fraud-focused evaluation metrics.

## Dataset
The benchmark Credit Card Fraud Detection dataset contains **284,807 transactions**, including **492 fraudulent transactions (0.1727%)**. The raw CSV is intentionally not committed because it is about 151 MB and exceeds GitHub's normal single-file limit. Place it locally at `data/creditcard.csv` before running the notebook.

## Completed analysis
1. Class imbalance analysis
2. Stratified 80/20 train/test split
3. Standardisation
4. SMOTE oversampling applied only to the training data
5. Logistic Regression
6. Random Forest
7. Precision, Recall, F1-score and ROC-AUC
8. Confusion matrices
9. ROC curve
10. Random Forest feature importance
11. Precision vs Recall discussion
12. Scalability discussion

## Results from the supplied dataset
| Model | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.3522 | 0.8878 | 0.5043 | 0.9674 |
| Random Forest | **0.8000** | 0.8571 | **0.8276** | **0.9778** |

The Random Forest provides the strongest overall balance in this run. Logistic Regression achieves slightly higher recall, which illustrates the precision–recall trade-off in fraud detection.

### Most important Random Forest features
The leading features were **V14, V17, V12, V10, V3, V16, V4, V9, V2 and V7**. These are anonymised PCA-derived variables, so they should not be interpreted as directly meaningful business attributes without additional feature documentation.

## Project structure
```text
OIBSIP/
└── DataAnalytics-L1-FraudDetection/
    ├── README.md
    ├── requirements.txt
    ├── data/
    │   └── creditcard.csv   # local only; not committed
    ├── notebooks/
    │   ├── Fraud_Detection_Machine_Learning.ipynb
    │   └── Fraud_Detection_SMOTE_Logistic_RF.ipynb
    └── results/
        ├── class_distribution.svg
        ├── confusion_matrices.svg
        ├── feature_importance.svg
        ├── model_metrics.csv
        ├── random_forest_feature_importance.csv
        ├── results_summary.json
        └── roc_curve.svg
```

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/Fraud_Detection_SMOTE_Logistic_RF.ipynb
```

Then place `creditcard.csv` inside `data/` and run the notebook from top to bottom.

## Important note
This is an educational internship project. The reported metrics are from one stratified hold-out split and should not be treated as production-ready fraud detection without threshold optimisation, cross-validation, cost-sensitive analysis, monitoring and domain validation.
