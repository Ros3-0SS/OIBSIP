# 💳 Fraud Detection — SMOTE, Logistic Regression & Random Forest

### OASIS INFOBYTE SIP — Data Analytics Level 2 • Task 3

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Analysis-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-11557c)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualisation-76B5C5)](https://seaborn.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

> **An end-to-end fraud detection project focused on class imbalance, SMOTE, machine learning classification and fraud-focused model evaluation.**

---

## 📌 Project Overview

This project develops a machine learning workflow for detecting fraudulent credit-card transactions.

The analysis follows a reproducible **inspect → clean → explore → balance → model → evaluate** workflow. Because fraudulent transactions represent only a very small proportion of the dataset, the project focuses on appropriate evaluation metrics rather than relying on accuracy alone.

---

## 🎯 Objectives

- 🔍 Inspect and understand the dataset and its class distribution
- ⚠️ Measure the extent of fraud and class imbalance
- 💰 Compare transaction amounts for fraudulent and legitimate transactions
- 🕐 Analyse fraud activity across the dataset's relative 24-hour cycle
- 📊 Explain why accuracy can be misleading for imbalanced fraud detection
- 🧪 Apply **SMOTE** to address class imbalance
- 🔀 Use a **stratified train/test split**
- 🤖 Train **Logistic Regression** and **Random Forest** models
- 📈 Evaluate models using Precision, Recall, F1-score and ROC-AUC
- 🧩 Analyse confusion matrices and ROC curves
- 🔎 Examine Random Forest feature importance
- ⚖️ Discuss the Recall vs Precision trade-off
- 🚀 Consider how the solution could scale to high transaction volumes

---

## 📂 Dataset

The benchmark **Credit Card Fraud Detection** dataset contains transaction information with anonymised PCA-derived features (`V1`–`V28`), `Time`, `Amount` and the target variable `Class`.

The original dataset contains **284,807 transactions**, including **492 fraudulent transactions**. This means fraud represents only a tiny fraction of all transactions, creating a severe class-imbalance problem.

The dataset is tracked with **Git LFS** because the CSV is large. After cloning the repository, Git LFS should be used to retrieve the actual dataset.

---

## 🧹 Data Preparation

The notebook performs the following preparation steps:

1. Load the credit-card transaction dataset.
2. Inspect data types, missing values and duplicate records.
3. Examine the distribution of legitimate and fraudulent transactions.
4. Analyse transaction amounts and the relative time-of-day pattern.
5. Separate features from the target variable.
6. Perform an **80/20 stratified train/test split**.
7. Standardise numerical features using training data.
8. Apply **SMOTE only to the training set** to prevent test-set leakage.

Applying SMOTE only after the train/test split is important because synthetic observations must not influence the independent test set used for final evaluation.

---

## 📊 Exploratory Data Analysis

### ⚠️ Class Imbalance

The dataset is extremely imbalanced: legitimate transactions vastly outnumber fraudulent transactions. This makes fraud detection a minority-class problem where a model can appear highly accurate while performing poorly at identifying fraud.

### 💰 Transaction Amounts

Transaction amounts are examined for fraudulent and legitimate transactions. Because transaction amounts are highly skewed, a logarithmic transformation can be used for clearer visual comparison.

### 🕐 Time-of-Day Analysis

The `Time` variable records elapsed seconds rather than a real-world timestamp. The project therefore uses a relative 24-hour cycle to examine how fraud activity varies throughout the recorded period.

---

## 🤖 Machine Learning Workflow

### Logistic Regression

Logistic Regression provides a simple, interpretable baseline for binary fraud classification after addressing the severe class imbalance.

### Random Forest

Random Forest provides a nonlinear ensemble approach capable of capturing more complex relationships between the anonymised transaction features.

Both models are trained after applying SMOTE to the training data only.

---

## 📈 Model Evaluation

Accuracy is deliberately not treated as the primary metric because the overwhelming majority of transactions are legitimate.

The project evaluates:

- **Precision** — Of the transactions predicted as fraud, how many were actually fraudulent?
- **Recall** — Of the actual fraudulent transactions, how many were detected?
- **F1-score** — The harmonic mean of Precision and Recall.
- **ROC-AUC** — Measures the model's ability to distinguish between fraudulent and legitimate transactions across classification thresholds.

Confusion matrices and ROC curves are also used to make model performance easier to interpret.

### ⚖️ Recall vs Precision

Fraud detection involves a practical trade-off. Increasing Recall can help identify more fraudulent transactions, but it may also increase false-positive alerts. Higher Precision reduces unnecessary alerts but can come with missed fraud.

The appropriate balance depends on the cost of missed fraud versus the operational cost of investigating false alerts.

---

## 🔎 Feature Importance

Random Forest feature importance is used to identify which anonymised variables contribute most strongly to the model's predictions.

The `V1`–`V28` variables are PCA-derived and anonymised, so their importance represents predictive signal rather than directly interpretable business characteristics.

---

## 🚀 Scalability Considerations

A production fraud-detection system processing very high transaction volumes would require more than a notebook-based model.

A scalable architecture could include:

- Streaming or micro-batched transaction ingestion
- Efficient feature generation
- Parallel model-serving workers
- Load balancing and horizontal scaling
- Monitoring of latency, throughput and fraud rates
- Model-drift and data-quality monitoring
- Threshold management
- Human investigation workflows
- Periodic model retraining and validation

For a target such as **1 million transactions per hour**, production capacity should be established through realistic load testing rather than assumed from notebook execution.

---

## 📁 Project Structure

```text
DataAnalytics-L2-FraudDetection/
│
├── 📄 README.md
├── 📄 .gitattributes
├── 📄 requirements.txt
│
├── 📂 data/
│   ├── 📄 README.md
│   └── creditcard.csv                 ← Dataset • Git LFS tracked
│
├── 📂 notebooks/
│   └── 📓 Fraud_Detection_SMOTE_Logistic_RF.ipynb
│
└── 📂 results/
    ├── Fraud_Detection_Results.md
    ├── class_distribution.svg
    ├── confusion_matrices.svg
    ├── feature_importance.svg
    ├── model_metrics.csv
    ├── random_forest_feature_importance.csv
    ├── results_summary.json
    └── roc_curve.svg
```

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

### 3. Retrieve the dataset

```bash
git lfs pull
```

### 4. Install the Python dependencies

```bash
pip install -r requirements.txt
```

### 5. Open Jupyter Notebook

```bash
jupyter notebook
```

### 6. Run the notebook

Open:

```text
notebooks/Fraud_Detection_SMOTE_Logistic_RF.ipynb
```

Run the cells from top to bottom to reproduce the analysis, model training and visualisations.

---

## 🛠️ Tools & Technologies

- **Python** — Programming and machine learning workflow
- **Pandas** — Data manipulation
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualisation
- **Seaborn** — Statistical visualisation
- **Scikit-learn** — Machine learning and model evaluation
- **imbalanced-learn / SMOTE** — Class-imbalance handling
- **Jupyter Notebook** — Interactive analysis
- **Git & GitHub** — Version control
- **Git LFS** — Large dataset versioning

---

## 📈 Skills Demonstrated

This project demonstrates an end-to-end machine learning workflow:

**Data inspection → Data cleaning → Exploratory analysis → Class-imbalance analysis → Stratified splitting → Feature scaling → SMOTE → Model training → Model evaluation → Feature importance → Interpretation → Scalability considerations**

---

## 📋 Task Alignment

The project addresses the applicable requirements of the **OASIS INFOBYTE Data Analytics Level 2 — Task 3: Fraud Detection**, including:

- class-imbalance and fraud-percentage analysis
- fraudulent vs legitimate transaction-amount analysis
- relative time-of-day analysis
- explanation of why accuracy is misleading for imbalanced fraud data
- SMOTE for handling class imbalance
- stratified train/test splitting
- Logistic Regression
- Random Forest
- Precision, Recall and F1-score
- ROC-AUC and ROC curve analysis
- confusion matrices
- Random Forest feature importance
- Recall vs Precision discussion
- scalability considerations for high transaction volumes

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ *Explore the repository to see the complete notebook, analysis results and supporting visualisations.*
