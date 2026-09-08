# Fraud Detection Analysis Results

## Dataset

The analysis was run on the supplied `creditcard.csv` dataset.

- Original transactions: **284,807**
- Duplicate rows removed: **1,081**
- Final transactions: **283,726**
- Legitimate transactions: **283,253**
- Fraudulent transactions: **473**
- Features used: **30**
- Missing values after cleaning: **0**
- Fraud rate: approximately **0.17%**

The dataset is therefore highly imbalanced, making accuracy alone an unsuitable primary metric.

## Models

Two models were evaluated using a stratified train/test split and SMOTE applied within the training pipeline:

1. Logistic Regression — baseline model
2. Random Forest — tree-based model

## Performance

| Model | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression + SMOTE | 35.22% | **88.78%** | 50.43% | 96.74% |
| Random Forest + SMOTE | **80.00%** | 85.71% | **82.76%** | **97.78%** |

## Preferred Model

**Random Forest** provided the strongest overall balance between identifying fraudulent transactions and limiting false positives.

Random Forest achieved **80.00% precision**, **85.71% recall**, **82.76% F1-score**, and **97.78% ROC-AUC** on the test set.

Logistic Regression achieved slightly higher recall (**88.78%**) but produced substantially lower precision (**35.22%**), meaning it generated more false-positive alerts.

## Conclusion

The analysis demonstrates that fraud detection requires evaluation beyond accuracy because fraudulent transactions represent only a very small fraction of all transactions. SMOTE was used to address the severe class imbalance during model training. Random Forest achieved the best overall F1-score and ROC-AUC, while Logistic Regression provided a useful baseline with slightly higher recall.

For a production fraud system, the decision threshold should be tuned according to the relative cost of missed fraud versus false alarms. A scalable implementation should also use efficient feature generation, batch or streaming inference, monitoring, periodic retraining, and human review for high-risk cases.

**Educational project:** model results are experimental and should not be treated as a production financial-fraud decision system.
