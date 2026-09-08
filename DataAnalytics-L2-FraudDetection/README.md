# 💳 Fraud Detection — Machine Learning

### OASIS INFOBYTE SIP — Data Analytics Level 2 • Task 3

> **An end-to-end fraud-detection project that combines exploratory data analysis, class-imbalance handling, supervised machine learning, model evaluation, feature analysis and production scalability considerations.**

---

## 📌 Project Overview

Financial fraud detection is a severely imbalanced classification problem because fraudulent transactions are rare compared with legitimate transactions.

This project uses the **Credit Card Fraud Detection dataset** to investigate fraud patterns and build two classification models: **Logistic Regression** and **Random Forest**. The workflow includes transaction-amount analysis, relative time-of-day analysis, stratified sampling, feature scaling, **SMOTE**, model comparison, fraud-focused evaluation metrics, feature importance and scalability planning.

The analysis deliberately avoids relying on accuracy alone because accuracy can be misleading when the positive class is extremely rare.

---

## 🎯 Objectives

- 🔍 Load and understand the transaction dataset
- 📊 Measure the percentage of fraudulent transactions and analyse class imbalance
- 💰 Compare transaction-amount distributions for fraud and legitimate transactions
- 🕐 Analyse fraud activity across the relative 24-hour cycle represented by the `Time` feature
- ⚠️ Explain why standard accuracy is misleading for this problem
- ✂️ Use a stratified train-test split so fraud appears in both sets
- ⚖️ Apply **SMOTE** to the training data only
- 🤖 Train and compare Logistic Regression and Random Forest
- 📈 Evaluate Precision, Recall, F1-score and ROC-AUC
- 🎯 Explain the Recall-versus-Precision trade-off and metric priority
- 🔎 Analyse Random Forest feature importance
- 🚀 Discuss how the solution could scale to **1 million transactions per hour**

---

## 📂 Dataset

The project uses the widely used **Credit Card Fraud Detection** dataset.

- **284,807** total transactions
- **492** fraudulent transactions
- Fraud rate: approximately **0.1727%**

The raw `creditcard.csv` file is approximately **151 MB**, so it is not stored in the normal Git history. Place it locally at:

```text
data/creditcard.csv
```

Git LFS is used in the project setup for large-file version control.

---

## 🔬 Methodology

### 1️⃣ Class imbalance analysis

The notebook calculates the fraud percentage directly from the `Class` target and visualises the legitimate-versus-fraud class distribution.

### 2️⃣ Exploratory Data Analysis

**Transaction amounts:** the notebook compares the distribution of transaction amounts between fraudulent and legitimate transactions. Because transaction amounts are skewed, a `log(1 + Amount)` transformation is used for the distribution visualisation.

**Time of day:** the dataset's `Time` field represents elapsed seconds from the first transaction rather than a real-world timestamp. It is converted into a relative 24-hour cycle to examine changes in fraud rate by hour.

### 3️⃣ Why accuracy is not enough

With fraud representing only about 0.17% of transactions, a classifier predicting every transaction as legitimate would still achieve very high accuracy while detecting no fraud. The project therefore focuses on minority-class metrics.

### 4️⃣ Stratified train-test split

An **80/20 stratified split** preserves the class distribution and ensures fraud cases are present in both training and testing sets.

### 5️⃣ Feature scaling

`StandardScaler` is fitted on the training data and then applied to the test data, preventing information from the test set from influencing preprocessing.

### 6️⃣ SMOTE

**Synthetic Minority Over-sampling Technique (SMOTE)** is applied **only to the training data**. This avoids leakage from synthetic samples into the test set.

### 7️⃣ Model training

Two classification models are evaluated:

- **Logistic Regression** — linear baseline model
- **Random Forest** — nonlinear ensemble tree model

### 8️⃣ Model evaluation

The models are evaluated using:

- 🎯 Precision
- 🚨 Recall
- ⚖️ F1-score
- 📈 ROC-AUC
- 🔲 Confusion matrices
- 📊 ROC curve

---

## 📊 Model Performance

Results from the supplied dataset and evaluated stratified hold-out split:

| Model | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression | 35.22% | **88.78%** | 50.43% | 96.74% |
| Random Forest | **80.00%** | 85.71% | **82.76%** | **97.78%** |

### 🏆 Best overall model: Random Forest

Random Forest produced the strongest overall balance in this experiment, while Logistic Regression achieved the higher recall.

This highlights the central fraud-detection trade-off: **higher Recall reduces missed fraud, while higher Precision reduces false alarms**.

---

## 🎯 Which Metric Matters Most?

**Recall is usually the most important starting metric when the cost of missing fraud is high**, because it measures how much of the actual fraud the system catches.

However, maximising recall alone can create too many false positives. Therefore, **Precision and F1-score should be used as operational guardrails**, with the final classification threshold selected according to the relative business cost of missed fraud versus false alerts.

In this experiment:

- Logistic Regression: **88.78% Recall**, 35.22% Precision
- Random Forest: **85.71% Recall**, **80.00% Precision**

---

## 🔎 Feature Importance

The leading Random Forest predictors were:

**V14, V17, V12, V10, V3, V16, V4, V9, V2 and V7**.

The `V` variables are anonymised **PCA-derived features**, so their importance represents predictive signal rather than directly interpretable business variables such as merchant category or customer demographics.

---

## 🚀 Scalability: 1 Million Transactions per Hour

**1,000,000 transactions/hour ≈ 277.8 transactions/second.**

A production implementation should use a horizontally scalable, stateless scoring architecture. Suitable considerations include:

- Streaming or micro-batched transaction ingestion
- Efficient/vectorised feature generation
- Parallel model-serving workers behind a load balancer
- Autoscaling and capacity headroom for traffic spikes
- Monitoring of throughput, p95/p99 latency, data quality, fraud rate and model drift
- Threshold management and human investigation workflows
- Periodic retraining and validation

If one scoring worker reliably processes `N` transactions per second, the theoretical minimum worker count is `ceil(277.8 / N)` before adding operational headroom. Exact infrastructure requirements must be established through production-like load testing.

---

## 📈 Visualisations & Results

The project includes outputs for:

- 📊 Class distribution
- 💰 Transaction amount distribution
- 🕐 Fraud rate by relative hour
- 🔲 Confusion matrices
- 📈 ROC curve
- 🌲 Random Forest feature importance
- 📋 Model performance metrics
- 📄 Results summary

These outputs are stored in the project's `results/` directory.

---

## 💡 Key Insights

1. **Fraud is extremely rare** — only 492 of 284,807 transactions are fraudulent.
2. **Accuracy alone is insufficient** for this use case because the majority class dominates the dataset.
3. **Transaction amount and relative time-of-day provide useful EDA perspectives** before modelling.
4. **SMOTE improves minority-class representation during training** without contaminating the hold-out test set.
5. **Random Forest produced the strongest overall balance** in the evaluated experiment.
6. **Logistic Regression produced higher recall**, showing that model choice depends on the cost of missed fraud versus false alerts.
7. **Recall is generally prioritised when missed fraud is more costly**, but precision and F1 remain important for controlling investigation workload.
8. The strongest Random Forest predictors are anonymised PCA-derived features, limiting direct business interpretation.

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **imbalanced-learn / SMOTE**
- **Jupyter Notebook**
- **Git & GitHub**
- **Git LFS**

---

## 📁 Project Structure

```text
DataAnalytics-L2-FraudDetection/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📂 data/
│   ├── 📄 README.md
│   └── 💾 creditcard.csv              # local / Git LFS
│
├── 📂 notebooks/
│   └── 📓 Fraud_Detection_SMOTE_Logistic_RF.ipynb
│
└── 📂 results/
    ├── 📄 Fraud_Detection_Results.md
    ├── 📊 class_distribution.svg
    ├── 💰 amount_distribution.png
    ├── 🕐 fraud_rate_by_hour.png
    ├── 🔲 confusion_matrices.svg
    ├── 🌲 feature_importance.svg
    ├── 📋 model_metrics.csv
    ├── 📋 random_forest_feature_importance.csv
    ├── 📄 results_summary.json
    └── 📈 roc_curve.svg
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ros3-0SS/OIBSIP.git
```

### 2. Open the project

```bash
cd OIBSIP/DataAnalytics-L2-FraudDetection
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place the dataset at:

```text
data/creditcard.csv
```

### 5. Open the notebook

```text
notebooks/Fraud_Detection_SMOTE_Logistic_RF.ipynb
```

### 6. Run all cells from top to bottom

The notebook reproduces the EDA, class-imbalance analysis, SMOTE workflow, model training, evaluation, feature importance and scalability discussion.

---

## 📋 OASIS INFOBYTE Task Alignment

This project now covers the complete requested Level 2, Task 3 workflow:

- ✅ Dataset loading and fraud-percentage analysis
- ✅ Transaction-amount distribution: fraud vs legitimate
- ✅ Time-of-day analysis
- ✅ Explanation of misleading accuracy
- ✅ Class-imbalance handling with SMOTE
- ✅ Stratified train/test split
- ✅ Logistic Regression + Random Forest
- ✅ Precision, Recall, F1 and ROC-AUC
- ✅ Recall vs Precision trade-off and metric priority
- ✅ Random Forest feature importance
- ✅ Scalability discussion for 1 million transactions/hour

---

## 📈 Portfolio Skills Demonstrated

**Data loading → EDA → Class imbalance analysis → Stratified splitting → Feature scaling → SMOTE → Model training → Model comparison → Fraud-focused evaluation → Feature importance → Business interpretation → Scalability planning**

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**

---

⭐ *Explore the repository to see the complete fraud-detection notebook, results and supporting analysis.*
