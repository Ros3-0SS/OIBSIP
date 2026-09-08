# 💳 Fraud Detection — Machine Learning

### OASIS INFOBYTE SIP — Data Analytics Level 2 • Task 1

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![imbalanced--learn](https://img.shields.io/badge/imbalanced--learn-SMOTE-red)](https://imbalanced-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

> **An end-to-end machine-learning project focused on detecting fraudulent financial transactions in a severely imbalanced dataset, comparing classification models and evaluating their ability to identify fraud.**

---

## 📌 Project Overview

Financial fraud detection is a challenging classification problem because fraudulent transactions are extremely rare compared with legitimate transactions.

In this project, I build and evaluate a fraud-detection workflow using the **Credit Card Fraud Detection dataset**. The analysis combines exploratory data analysis, stratified sampling, feature scaling, **SMOTE oversampling**, Logistic Regression and Random Forest classification.

The project places particular emphasis on **Precision, Recall, F1-score and ROC-AUC** rather than relying only on accuracy, since accuracy can be misleading when the target classes are highly imbalanced.

---

## 🎯 Objectives

- 🔍 Understand the structure and class distribution of the transaction data
- 📊 Investigate the severe imbalance between legitimate and fraudulent transactions
- ✂️ Create a stratified train-test split
- ⚙️ Standardise numerical features where appropriate
- ⚖️ Apply **SMOTE** to the training data to address class imbalance
- 🤖 Train and compare Logistic Regression and Random Forest models
- 📈 Evaluate models using fraud-focused performance metrics
- 🧮 Analyse confusion matrices and ROC curves
- 🔎 Identify influential features using Random Forest feature importance
- 💡 Discuss the precision–recall trade-off and practical fraud-detection considerations

---

## 📂 Dataset

The project uses the widely used **Credit Card Fraud Detection** dataset.

The dataset contains **284,807 financial transactions**, of which only **492 are fraudulent**, meaning fraudulent transactions represent approximately **0.1727%** of all transactions.

This extreme imbalance makes fraud detection a useful real-world example of why model evaluation must consider minority-class performance.

### Dataset limitation

The raw `creditcard.csv` file is approximately **151 MB**, so it is not stored directly in the repository's normal Git history. The dataset should be placed locally at:

```text
data/creditcard.csv
```

Git LFS is used in the project setup for large-file version control.

---

## 🔬 Methodology

### 1️⃣ Exploratory Data Analysis

The dataset is inspected to understand its structure, variables and class distribution, with particular attention to the extremely small proportion of fraudulent transactions.

### 2️⃣ Stratified train-test split

The data is divided into training and testing sets using a **stratified 80/20 split**, preserving the class proportions in both subsets.

### 3️⃣ Feature scaling

Numerical features are standardised where required to support the machine-learning workflow.

### 4️⃣ SMOTE oversampling

**Synthetic Minority Over-sampling Technique (SMOTE)** is applied **only to the training data**. This is important because applying oversampling before the train-test split could cause information leakage and produce misleading evaluation results.

### 5️⃣ Model training

Two classification approaches are evaluated:

- **Logistic Regression** — a linear baseline classification model
- **Random Forest** — an ensemble tree-based classification model capable of capturing nonlinear relationships

### 6️⃣ Model evaluation

The models are compared using:

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

The **Random Forest** model achieved the strongest overall balance between identifying fraudulent transactions and limiting false fraud alerts, with:

- **80.00% Precision**
- **85.71% Recall**
- **82.76% F1-score**
- **97.78% ROC-AUC**

Logistic Regression achieved slightly higher recall (**88.78%**), meaning it identified a larger proportion of the fraudulent transactions in this particular split. However, its lower precision resulted in substantially more false positives.

This demonstrates an important **precision–recall trade-off** in fraud detection: missing fraud and incorrectly flagging legitimate transactions both have costs.

---

## 🔎 Feature Importance

The leading Random Forest features were:

**V14, V17, V12, V10, V3, V16, V4, V9, V2 and V7**.

The transaction variables beginning with `V` are anonymised **PCA-derived features**. Therefore, their importance should be interpreted as predictive signals rather than direct business attributes such as merchant type, customer age or transaction location.

---

## 📈 Visualisations & Results

The project includes supporting outputs for model interpretation and evaluation:

- 📊 Class distribution
- 🔲 Confusion matrices
- 📈 ROC curve
- 🌲 Random Forest feature importance
- 📋 Model performance metrics
- 📄 Results summary

These outputs are stored in the project's `results/` directory.

---

## 💡 Key Insights

1. **Fraud is extremely rare** — only 492 of 284,807 transactions are fraudulent.
2. **Accuracy alone is not sufficient** for evaluating this problem because a model can appear highly accurate while performing poorly on fraud cases.
3. **SMOTE improves the learning environment for the minority class** by generating synthetic training examples rather than simply duplicating existing fraud observations.
4. **Random Forest produced the strongest overall performance** in this experiment.
5. **Logistic Regression produced higher recall**, demonstrating that model selection depends on the relative cost of missed fraud versus false alerts.
6. The most influential Random Forest predictors are anonymised PCA-derived variables, limiting direct business interpretation.

---

## 🚀 Practical Considerations

A production fraud-detection system would require additional work beyond this internship project, including:

- Threshold optimisation based on business costs
- Cross-validation
- Cost-sensitive learning
- Precision–recall curve analysis
- Model monitoring and drift detection
- Investigation workflows for flagged transactions
- Regular model retraining
- Domain and regulatory validation

The reported metrics therefore represent the performance of this particular experimental workflow rather than a production-ready fraud-detection system.

---

## 🛠️ Tools & Technologies

- **Python** — Programming and analysis
- **Pandas** — Data manipulation
- **NumPy** — Numerical computing
- **Matplotlib** — Data visualisation
- **Seaborn** — Statistical visualisation
- **Scikit-learn** — Machine learning, preprocessing and evaluation
- **imbalanced-learn** — SMOTE oversampling
- **Jupyter Notebook** — Interactive analysis
- **Git & GitHub** — Version control and project hosting
- **Git LFS** — Large dataset version control

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
│   ├── 📓 Fraud_Detection_Machine_Learning.ipynb
│   └── 📓 Fraud_Detection_SMOTE_Logistic_RF.ipynb
│
└── 📂 results/
    ├── 📄 Fraud_Detection_Results.md
    ├── 📊 class_distribution.svg
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

### 2. Open the fraud-detection project

```bash
cd OIBSIP/DataAnalytics-L2-FraudDetection
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place the dataset here:

```text
data/creditcard.csv
```

### 5. Open the notebook

For the final SMOTE/model-comparison workflow, open:

```text
notebooks/Fraud_Detection_SMOTE_Logistic_RF.ipynb
```

### 6. Run the notebook

Run the notebook cells from top to bottom to reproduce the analysis, model training, evaluation metrics and visualisations.

---

## 📈 Portfolio Skills Demonstrated

This project demonstrates an end-to-end machine-learning workflow:

**Data inspection → Class imbalance analysis → Stratified splitting → Feature scaling → SMOTE → Model training → Model comparison → Performance evaluation → Feature importance → Interpretation → Practical recommendations**

---

## 📋 Task Alignment

This project addresses the **OASIS INFOBYTE Data Analytics Level 2 fraud-detection task** by applying machine-learning techniques to a financial transaction dataset and evaluating models using appropriate classification metrics for an imbalanced problem.

The project also documents methodological limitations and explains why fraud-focused metrics such as **Precision, Recall and F1-score** are more informative than accuracy alone for this use case.

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ *Explore the repository to see the complete notebook, model outputs and supporting analysis.*
