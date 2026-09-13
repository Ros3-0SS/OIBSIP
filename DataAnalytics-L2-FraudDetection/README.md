# 💳 Fraud Detection — SMOTE, Logistic Regression & Random Forest

### OASIS INFOBYTE SIP — Data Analytics Level 2 • Task 3

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Analysis-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Imbalanced--learn](https://img.shields.io/badge/Imbalanced--learn-SMOTE-red)](https://imbalanced-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-11557c)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualisation-76B5C5)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Git LFS](https://img.shields.io/badge/Git%20LFS-Large%20Files-6f42c1?logo=git&logoColor=white)](https://git-lfs.com/)

> **An end-to-end machine-learning project focused on detecting fraudulent credit-card transactions under severe class imbalance, with fraud-focused evaluation, feature importance and production scalability considerations.**

---

## 📌 Project Overview

This project develops and evaluates machine-learning models for **credit-card fraud detection** using a highly imbalanced transaction dataset.

The workflow follows a reproducible **inspect → clean → explore → split → balance → train → evaluate → interpret → scale** approach. The analysis deliberately prioritises fraud-sensitive metrics rather than relying on accuracy alone.

The project compares **Logistic Regression with SMOTE** against a **Random Forest with SMOTE**, evaluates the models using Precision, Recall, F1-score and ROC-AUC, and examines the trade-off between catching fraudulent transactions and limiting false-positive alerts.

---

## 🎯 Objectives

- 🔍 Measure fraud prevalence and class imbalance
- 💳 Compare transaction amounts for fraudulent vs legitimate transactions
- 🕒 Analyse fraud activity across the dataset's relative 24-hour cycle
- ⚠️ Explain why accuracy is misleading for highly imbalanced fraud data
- 🧪 Use a stratified train/test split
- ⚖️ Apply SMOTE to the training data only
- 🤖 Train Logistic Regression and Random Forest models
- 📊 Evaluate Precision, Recall, F1-score and ROC-AUC
- 🔄 Explain the Recall vs Precision trade-off
- 🔎 Analyse Random Forest feature importance
- 🚀 Discuss scalability for 1 million transactions per hour

---

## 📂 Dataset

The benchmark **Credit Card Fraud Detection** dataset originally contains:

| Metric | Value |
|---|---:|
| Total transactions | **284,807** |
| Fraudulent transactions | **492** |
| Original fraud rate | **≈ 0.1727%** |
| Duplicate rows removed | **1,081** |
| Cleaned transactions | **283,726** |
| Cleaned legitimate transactions | **283,253** |
| Cleaned fraudulent transactions | **473** |
| Cleaned fraud rate | **≈ 0.17%** |

The dataset is extremely imbalanced: fraudulent transactions represent only a tiny fraction of all transactions.

The CSV is approximately **151 MB**, so it is tracked using **Git LFS**. The repository contains the LFS pointer for `data/creditcard.csv`; cloning with Git LFS retrieves the actual dataset.

---

## 🧹 Data Preparation

The analysis removes duplicate rows before modelling. After cleaning, the modelling dataset contains **283,726 transactions**, including **473 fraudulent transactions**.

The project preserves the minority-class examples while ensuring that the machine-learning workflow does not leak information from the test set into training.

---

## 🔬 Methodology

### 1. Exploratory Data Analysis

The notebook examines:

- Class distribution and fraud percentage
- Transaction amount distribution for fraud vs legitimate transactions
- Relative time-of-day patterns using the `Time` feature
- The extreme imbalance between legitimate and fraudulent transactions

The `Time` variable records elapsed seconds rather than a real-world timestamp, so the time analysis is interpreted as a **relative 24-hour cycle**, not as a calendar-based time series.

### 2. Stratified Train/Test Split

An **80/20 stratified split** is used so that the fraud class is represented proportionally in both training and test sets.

### 3. Feature Scaling

`StandardScaler` is fitted on the training data only and then applied to the test data. This prevents information from the test set influencing the preprocessing stage.

### 4. SMOTE

**Synthetic Minority Over-sampling Technique (SMOTE)** is applied **only to the training data**. The test set remains untouched so that final evaluation reflects the original class distribution.

### 5. Machine Learning Models

Two supervised models are evaluated:

- **Logistic Regression + SMOTE** — an interpretable linear baseline
- **Random Forest + SMOTE** — a nonlinear ensemble model capable of capturing more complex relationships

### 6. Evaluation

The models are assessed using:

- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrices
- ROC curve

---

## ⚠️ Why Accuracy Is Misleading

Fraud accounts for only about **0.17%** of transactions. A model could predict almost every transaction as legitimate and still achieve extremely high accuracy while failing to identify the transactions that matter most.

For this reason, the project focuses on **Recall, Precision, F1-score and ROC-AUC**. In fraud detection, missing a fraudulent transaction can be more costly than generating an additional false-positive alert, although the appropriate balance depends on the business context.

---

## 📈 Model Performance

Results from the evaluated stratified hold-out split:

| Model | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression + SMOTE | 35.22% | **88.78%** | 50.43% | 96.74% |
| Random Forest + SMOTE | **80.00%** | 85.71% | **82.76%** | **97.78%** |

### 🏆 Best Overall Model — Random Forest

**Random Forest + SMOTE** provides the strongest overall balance in this experiment:

- 🥇 **80.00% Precision**
- 🎯 **85.71% Recall**
- ⭐ **82.76% F1-score**
- 📈 **97.78% ROC-AUC**

Logistic Regression achieves slightly higher recall (**88.78%**), meaning it catches a larger proportion of fraud in this experiment, but its much lower precision means considerably more legitimate transactions are flagged as suspicious.

### 🔄 Recall vs Precision Trade-off

For fraud detection, **Recall is often the most important starting metric when missing fraud is costly**. However, maximising recall without considering precision can produce too many false-positive alerts and overwhelm investigation teams.

The operational threshold should therefore be selected according to the business cost of:

**Missed fraud ↔ False-positive investigation cost**

---

## 🔎 Feature Importance

The leading Random Forest predictors were:

**V14, V17, V12, V10, V3, V16, V4, V9, V2 and V7**.

These `V` variables are anonymised **PCA-derived features**, so their importance represents predictive signal rather than directly interpretable business variables such as merchant type or customer demographics.

---

## 📊 Results & Visualisations

The committed `results/` directory contains the final project outputs:

- `class_distribution.svg` — class imbalance visualisation
- `confusion_matrices.svg` — model confusion matrices
- `feature_importance.svg` — Random Forest feature importance
- `roc_curve.svg` — ROC curve comparison
- `model_metrics.csv` — model evaluation metrics
- `random_forest_feature_importance.csv` — feature importance data
- `results_summary.json` — machine-readable results summary
- `Fraud_Detection_Results.md` — written results summary

The notebook also contains the exploratory analysis and written interpretations of the visualisations.

---

## 🚀 Scalability — 1 Million Transactions per Hour

A production system processing **1,000,000 transactions per hour** must handle approximately **277.8 transactions per second**.

A scalable fraud-detection architecture could use:

1. ⚡ Streaming or micro-batched transaction ingestion
2. 🧮 Efficient/vectorised feature generation
3. 🤖 Parallel model-serving workers
4. ⚖️ Load balancing across scoring services
5. 📈 Horizontal autoscaling with capacity headroom
6. 📡 Monitoring of throughput, p95/p99 latency and data quality
7. 🚨 Fraud-rate and model-drift monitoring
8. 👩🏽‍💻 Human investigation workflows for suspicious transactions
9. 🔁 Periodic model retraining and validation
10. 🎚️ Centralised threshold management

The actual infrastructure requirement should be established through **production-like load testing**, rather than inferred from notebook execution time alone.

---

## 📁 Project Structure

```text
DataAnalytics-L2-FraudDetection/
│
├── 📂 data/
│   ├── README.md
│   └── creditcard.csv                 ← Git LFS tracked
│
├── 📂 notebooks/
│   └── Fraud_Detection_SMOTE_Logistic_RF.ipynb
│
├── 📂 results/
│   ├── Fraud_Detection_Results.md
│   ├── class_distribution.svg
│   ├── confusion_matrices.svg
│   ├── feature_importance.svg
│   ├── model_metrics.csv
│   ├── random_forest_feature_importance.csv
│   ├── results_summary.json
│   └── roc_curve.svg
│
├── 📄 .gitattributes
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🛠️ Tools & Technologies

- **Python** — Programming and analysis
- **Pandas** — Data manipulation
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualisation
- **Seaborn** — Statistical visualisation
- **Scikit-learn** — Machine learning and evaluation
- **imbalanced-learn / SMOTE** — Class-imbalance handling
- **Jupyter Notebook** — Interactive analysis
- **Git & GitHub** — Version control and portfolio management
- **Git LFS** — Large dataset versioning

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ros3-0SS/OIBSIP.git
cd OIBSIP/DataAnalytics-L2-FraudDetection
```

### 2. Install Git LFS

```bash
git lfs install
```

### 3. Download the dataset

```bash
git lfs pull
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Open the notebook

```bash
jupyter notebook
```

Then open:

```text
notebooks/Fraud_Detection_SMOTE_Logistic_RF.ipynb
```

### 6. Run the notebook

Run the notebook **from top to bottom** so that the data preparation, EDA, SMOTE workflow, model training, evaluation and result generation are reproduced in sequence.

---

## 📈 Skills Demonstrated

This project demonstrates an end-to-end **imbalanced classification** workflow:

**Data inspection → Data cleaning → EDA → Class-imbalance analysis → Stratified splitting → Feature scaling → SMOTE → Model training → Model evaluation → Feature importance → Business trade-off analysis → Scalability planning**

---

## 💡 Key Takeaways

- 🚨 Fraud is extremely rare, representing only about **0.17%** of transactions.
- ⚠️ Accuracy alone would give a misleading picture of model performance.
- 🎯 **Logistic Regression + SMOTE** achieved the highest recall at **88.78%**.
- 🏆 **Random Forest + SMOTE** achieved the strongest overall balance, with **80.00% precision, 85.71% recall, 82.76% F1-score and 97.78% ROC-AUC**.
- 🔎 Random Forest feature importance identified **V14, V17, V12 and V10** among the strongest predictors.
- ⚖️ Fraud detection requires balancing missed fraud against false-positive investigation costs.
- 🚀 A production-scale solution must consider throughput, latency, monitoring, drift and model-serving architecture.

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Data Analytics Portfolio • OASIS INFOBYTE SIP

---

> ⚠️ **Educational project:** the reported model results are experimental and should not be treated as a production financial-fraud decision system.

⭐ *Explore the repository to see the complete notebook, machine-learning results and supporting visualisations.*
