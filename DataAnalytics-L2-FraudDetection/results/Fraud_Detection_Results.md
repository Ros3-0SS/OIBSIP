# Fraud Detection Analysis Results

## Dataset

The analysis uses the benchmark Credit Card Fraud Detection dataset.

- Original transactions: **284,807**
- Original fraudulent transactions: **492**
- Duplicate rows removed during cleaning: **1,081**
- Final transactions used for modelling: **283,726**
- Final legitimate transactions: **283,253**
- Final fraudulent transactions: **473**
- Features used: **30**
- Missing values after cleaning: **0**
- Final fraud rate: approximately **0.17%**

The distinction between original and cleaned counts is intentional: the original dataset contains 492 fraud cases, while the modelling dataset contains 473 after duplicate removal.

## Models

Two models were evaluated using an 80/20 stratified train/test split and SMOTE applied only to the training data:

1. **Logistic Regression + SMOTE** — baseline model
2. **Random Forest + SMOTE** — nonlinear ensemble model

## Performance

| Model | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression + SMOTE | 35.22% | **88.78%** | 50.43% | 96.74% |
| Random Forest + SMOTE | **80.00%** | 85.71% | **82.76%** | **97.78%** |

## Preferred Model

**Random Forest** provided the strongest overall balance between identifying fraudulent transactions and limiting false-positive alerts.

Random Forest achieved **80.00% precision**, **85.71% recall**, **82.76% F1-score**, and **97.78% ROC-AUC** on the hold-out test set.

Logistic Regression achieved slightly higher recall (**88.78%**) but substantially lower precision (**35.22%**), demonstrating the Recall-versus-Precision trade-off.

## Key Interpretation

Recall is an important starting metric when missed fraud is costly, but maximising recall alone can create an excessive number of false alerts. Precision and F1-score therefore provide important operational guardrails. In a production system, the classification threshold should be selected using the relative business cost of missed fraud versus false positives.

## Conclusion

The analysis demonstrates why fraud detection requires evaluation beyond accuracy when the positive class is extremely rare. SMOTE was applied only to the training data to improve minority-class representation without contaminating the hold-out test set.

Random Forest achieved the best overall F1-score and ROC-AUC, while Logistic Regression produced slightly higher recall. The strongest Random Forest predictors were anonymised PCA-derived features, so their importance should not be interpreted as direct business-variable importance.

For production use, threshold optimisation, load testing, scalable feature generation, batch or streaming inference, monitoring, periodic retraining and human review would be required.

**Educational project:** these model results are experimental and should not be treated as a production financial-fraud decision system.
