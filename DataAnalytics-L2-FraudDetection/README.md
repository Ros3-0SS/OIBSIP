# 💳 Fraud Detection — SMOTE, Logistic Regression & Random Forest

### OASIS INFOBYTE SIP — Data Analytics Level 2 • Task 3

An end-to-end fraud-detection project covering exploratory data analysis, severe class-imbalance handling, supervised machine learning, fraud-focused evaluation, feature importance and production scalability considerations.

## 🎯 Objectives

- Measure fraud prevalence and class imbalance
- Compare transaction amounts for fraudulent vs legitimate transactions
- Analyse fraud activity across the dataset's relative 24-hour cycle
- Explain why accuracy is misleading for highly imbalanced fraud data
- Use a stratified train/test split so fraud is represented in both sets
- Apply SMOTE to the training data only
- Train Logistic Regression and Random Forest models
- Evaluate Precision, Recall, F1-score and ROC-AUC
- Explain the Recall vs Precision trade-off and metric priority
- Analyse Random Forest feature importance
- Discuss scalability for 1 million transactions per hour

## 📊 Dataset

The benchmark Credit Card Fraud Detection dataset originally contains **284,807 transactions**, including **492 fraudulent transactions** (approximately **0.1727%**).

During the analysis, **1,081 duplicate rows were removed**, leaving **283,726 transactions**: **283,253 legitimate** and **473 fraudulent**. The cleaned fraud rate remains approximately **0.17%**.

The dataset is tracked with **Git LFS** because the CSV is approximately **151 MB**. The repository contains the LFS pointer at `data/creditcard.csv`; cloning with Git LFS retrieves the actual dataset.

## 🔬 Methodology

### Exploratory Data Analysis

- Class distribution and fraud percentage
- Transaction amount comparison using `log(1 + Amount)` because amounts are skewed
- Relative time-of-day analysis using the `Time` feature, which records elapsed seconds rather than a real-world timestamp

### Imbalanced classification workflow

1. 80/20 **stratified** train/test split
2. `StandardScaler` fitted on training data only
3. **SMOTE** applied to training data only to avoid test-set leakage
4. Logistic Regression as the baseline model
5. Random Forest as the nonlinear ensemble model
6. Evaluation with Precision, Recall, F1-score, ROC-AUC, confusion matrices and ROC curve

### Why accuracy is not enough

Fraud represents only about 0.17% of the transactions. A model that predicts almost everything as legitimate could achieve very high accuracy while detecting little or no fraud. The project therefore focuses on minority-class performance rather than accuracy alone.

## 📈 Model Performance

Results from the evaluated stratified hold-out split:

| Model | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression + SMOTE | 35.22% | **88.78%** | 50.43% | 96.74% |
| Random Forest + SMOTE | **80.00%** | 85.71% | **82.76%** | **97.78%** |

### 🏆 Best overall model: Random Forest

Random Forest provides the strongest overall balance in this experiment, with substantially higher precision and the best F1-score and ROC-AUC. Logistic Regression has slightly higher recall, so it catches a larger share of fraud at the cost of many more false-positive alerts.

For fraud detection, **Recall is usually the most important starting metric when missing fraud is costly**, while Precision and F1-score act as operational guardrails. The final threshold should be selected according to the business cost of missed fraud versus false alerts.

## 🔎 Feature Importance

The leading Random Forest predictors were **V14, V17, V12, V10, V3, V16, V4, V9, V2 and V7**. These `V` variables are anonymised PCA-derived features, so their importance represents predictive signal rather than directly interpretable business variables.

## 🚀 Scalability: 1 Million Transactions per Hour

1,000,000 transactions/hour is approximately **277.8 transactions/second**. A production solution should use a stateless, horizontally scalable scoring architecture with:

- Streaming or micro-batched ingestion
- Efficient/vectorised feature generation
- Parallel model-serving workers behind a load balancer
- Autoscaling and capacity headroom
- Monitoring of throughput, p95/p99 latency, data quality, fraud rate and model drift
- Threshold management and human investigation workflows
- Periodic retraining and validation

The exact infrastructure requirement should be established through production-like load testing rather than assumed from notebook execution alone.

## 📁 Project Structure

```text
DataAnalytics-L2-FraudDetection/
├── README.md
├── .gitattributes
├── requirements.txt
├── data/
│   ├── README.md
│   └── creditcard.csv              # Git LFS
├── notebooks/
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

The committed `results/` directory contains the final submission visuals and model outputs. The notebook can regenerate the exploratory plots locally from the LFS dataset.

## ▶️ How to Run

```bash
git clone https://github.com/Ros3-0SS/OIBSIP.git
cd OIBSIP/DataAnalytics-L2-FraudDetection
pip install -r requirements.txt
```

Make sure Git LFS is installed, then pull the dataset if necessary:

```bash
git lfs pull
```

Open:

```text
notebooks/Fraud_Detection_SMOTE_Logistic_RF.ipynb
```

Run the notebook from top to bottom.

## 📋 OASIS INFOBYTE Task 3 Alignment

- ✅ Dataset loading and fraud-percentage analysis
- ✅ Fraud vs legitimate transaction-amount analysis
- ✅ Time-of-day analysis
- ✅ Explanation of misleading accuracy
- ✅ SMOTE class-imbalance handling
- ✅ Stratified train/test split
- ✅ Logistic Regression + Random Forest
- ✅ Precision, Recall, F1-score and ROC-AUC
- ✅ Recall vs Precision trade-off and metric priority
- ✅ Random Forest feature importance
- ✅ Scalability discussion for 1 million transactions/hour

## 🛠️ Technologies

Python • Pandas • NumPy • Matplotlib • Seaborn • Scikit-learn • imbalanced-learn/SMOTE • Jupyter • Git • GitHub • Git LFS

## 👩🏽‍💻 Author

**Ntsako Sibanda**

> **Educational project:** the reported model results are experimental and should not be treated as a production financial-fraud decision system.
