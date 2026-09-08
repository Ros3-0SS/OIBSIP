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
2. HistGradientBoosting — tree-based model

> Note: the original notebook skeleton specified Random Forest as the second model. The successful completed run used HistGradientBoosting because the full Random Forest + SMOTE configuration was too computationally heavy in the execution environment. The results below reflect the model that was actually run.

## Performance

| Model | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression + SMOTE | 44.77% | **81.05%** | 57.68% | 96.24% |
| HistGradientBoosting + SMOTE | **79.79%** | 78.95% | **79.37%** | **96.66%** |

## Preferred Model

**HistGradientBoosting** provided the strongest overall balance between identifying fraudulent transactions and limiting false positives.

Its test-set confusion matrix was:

- True negatives: **56,632**
- False positives: **19**
- True positives: **75**
- False negatives: **20**

Logistic Regression achieved slightly higher recall (**81.05%**) but produced substantially more false positives, resulting in lower precision (**44.77%**).

## Conclusion

The analysis demonstrates that fraud detection requires evaluation beyond accuracy because fraudulent transactions represent only a very small fraction of all transactions. SMOTE was used to address the severe class imbalance during model training. HistGradientBoosting achieved the best overall F1 and ROC-AUC in the completed run, while Logistic Regression provided a useful baseline with slightly higher recall.

For a production fraud system, the decision threshold should be tuned according to the relative cost of missed fraud versus false alarms. A scalable implementation should also use efficient feature generation, batch or streaming inference, monitoring, periodic retraining, and human review for high-risk cases.

**Educational project:** model results are experimental and should not be treated as a production financial-fraud decision system.
