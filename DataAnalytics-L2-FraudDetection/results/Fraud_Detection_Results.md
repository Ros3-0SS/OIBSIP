# Fraud Detection Analysis Results

## Oasis Infobyte Level 2 — Task 3

This project follows the Fraud Detection checklist in the Oasis Infobyte SIP task list.

### Dataset
- Original transactions: **284,807**
- Original fraud cases: **492**
- Duplicate rows removed: **1,081**
- Cleaned modelling rows: **283,726**
- Legitimate transactions after cleaning: **283,253**
- Fraudulent transactions after cleaning: **473**
- Final fraud rate: **0.1667%**
- Missing values after cleaning: **0**

### Modelling
An 80/20 **stratified** train/test split was used. SMOTE was applied **only to the training set**. The two required models are Logistic Regression and Random Forest.

### Current recorded test performance

| Model | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression | 40.00% | 80.00% | 53.33% | 96.64% |
| Random Forest | **92.31%** | 75.79% | **83.24%** | **96.72%** |

Random Forest provides the strongest overall balance in this recorded run. Logistic Regression has higher recall, so it catches more fraud at the cost of substantially more false-positive alerts.

### Required analysis covered
- Class imbalance and fraud percentage
- Fraud vs legitimate transaction amount analysis
- Time-of-day analysis
- Explanation of why standard accuracy is misleading
- SMOTE oversampling
- Stratified train/test split
- Logistic Regression and Random Forest
- Precision, Recall, F1-score and ROC-AUC
- Confusion matrices
- AUC-ROC curve
- Random Forest feature importance
- Recall-versus-Precision trade-off
- Scalability discussion for 1 million transactions per hour

### Important interpretation
The strongest Random Forest predictors are anonymised PCA-derived features. Their importance is predictive rather than causal or directly interpretable as business variables.

**Educational project:** these results are experimental and should not be treated as a production financial-fraud decision system.
