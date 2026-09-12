# OIBSIP — Data Analytics Portfolio

[![OASIS INFOBYTE](https://img.shields.io/badge/OASIS%20INFOBYTE-Data%20Analytics-blue)](https://oasisinfobyte.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![GitHub Actions](https://github.com/Ros3-0SS/OIBSIP/actions/workflows/run-eda-retail-sales.yml/badge.svg)](https://github.com/Ros3-0SS/OIBSIP/actions/workflows/run-eda-retail-sales.yml)

> **OASIS INFOBYTE SIP — Data Analytics Portfolio**  
> A collection of practical analytics and machine-learning projects covering data preparation, exploratory analysis, customer segmentation, fraud detection, model evaluation and business recommendations.

---

## 📌 About This Repository

This repository contains my **OASIS INFOBYTE Data Analytics internship projects**. Each project follows an end-to-end workflow: from preparing and analysing data to communicating findings and translating them into practical business recommendations.

The portfolio currently includes **three projects across Level 1 and Level 2**:

| Level | Task | Project | Focus |
|---|---|---|---|
| Level 1 | Task 1 | [EDA on Online Retail Sales](./DataAnalytics-L1-EDARetailSales/) | Exploratory data analysis, sales trends, AOV, products, markets and correlations |
| Level 1 | Task 2 | [Online Retail Customer Segmentation](./DataAnalytics-L1-CustomerSegmentation/) | RFM analysis, K-Means clustering and customer profiling |
| Level 2 | Task 3 | [Fraud Detection](./DataAnalytics-L2-FraudDetection/) | Imbalanced classification, SMOTE, Logistic Regression and Random Forest |

---

## 📊 Projects

### Level 1 — Task 1: EDA on Online Retail Sales

**Project:** [`DataAnalytics-L1-EDARetailSales/`](./DataAnalytics-L1-EDARetailSales/)

An exploratory analysis of online retail transactions covering data cleaning, descriptive statistics, revenue trends, Average Order Value (AOV), product analysis, country analysis, correlation analysis, visualisations, findings and business recommendations.

**Workflow:**

`Raw data → Data inspection → Data cleaning → Feature creation → Descriptive statistics → Trend analysis → AOV analysis → Product analysis → Market analysis → Correlation analysis → Visualisation → Findings → Recommendations`

The project also documents dataset limitations rather than inventing unavailable information. The supplied dataset does **not** contain reliable age/gender fields or a dedicated product-category field, so those analyses are intentionally not fabricated.

**Automation:** The notebook is automatically executed and validated by GitHub Actions. The workflow checks the notebook from top to bottom, verifies required outputs and stores the execution results as an artifact. It uses read-only repository permissions and does **not** create automated commits on `main`.

### Level 1 — Task 2: Online Retail Customer Segmentation

**Project:** [`DataAnalytics-L1-CustomerSegmentation/`](./DataAnalytics-L1-CustomerSegmentation/)

A customer segmentation project using the UCI Online Retail dataset, **Recency, Frequency and Monetary (RFM)** analysis and **K-Means clustering**.

The project covers data preparation, exploratory analysis, RFM feature engineering, transformation and standardisation, cluster selection using the Elbow Method and Silhouette Score, cluster profiling, visualisation and marketing recommendations.

### Level 2 — Task 3: Fraud Detection

**Project:** [`DataAnalytics-L2-FraudDetection/`](./DataAnalytics-L2-FraudDetection/)

A machine-learning fraud-detection project focused on severe class imbalance. The workflow uses a stratified train-test split, feature scaling, **SMOTE**, Logistic Regression and Random Forest models.

Models are evaluated using **Precision, Recall, F1-score and ROC-AUC**, with confusion matrices, ROC curves and Random Forest feature importance.

**Experiment result:** Random Forest achieved **80.0% precision, 85.7% recall, 82.8% F1-score and 97.8% ROC-AUC** on the evaluated test set.

> **Note:** These model results are experimental and should not be treated as a production financial-fraud decision system.

---

## 🛠️ Tools & Technologies

### Data Analytics

- **Python** — Programming, analysis and automation
- **Pandas** — Data manipulation, cleaning and aggregation
- **NumPy** — Numerical computing
- **Matplotlib** — Data visualisation
- **Seaborn** — Statistical visualisation
- **Jupyter Notebook** — Interactive and reproducible analysis

### Machine Learning

- **Scikit-learn** — Standardisation, K-Means, Logistic Regression, Random Forest and model evaluation
- **imbalanced-learn** — SMOTE oversampling for imbalanced classification

### Data, Version Control & Reproducibility

- **UCI ML Repository / ucimlrepo** — Dataset acquisition for customer segmentation
- **Git** — Version control
- **GitHub** — Repository hosting
- **Git LFS** — Large dataset versioning
- **requirements.txt** — Python dependency management

### Automation

- **GitHub Actions** — Automated execution and validation of the Task 1 EDA notebook
- **nbconvert** — Non-interactive notebook execution
- **actions/upload-artifact** — Stores workflow-generated outputs without automatically committing them to `main`

---

## 📁 Repository Structure

```text
OIBSIP/
│
├── 📄 README.md
├── 📄 .gitattributes
│
├── 📂 .github/
│   └── 📂 workflows/
│       └── 📄 run-eda-retail-sales.yml
│
├── 📂 DataAnalytics-L1-EDARetailSales/
│   ├── 📄 README.md
│   ├── 📄 requirements.txt
│   ├── 📄 .gitignore
│   ├── 📓 EDA_Retail_Sales.ipynb
│   ├── 📂 data/
│   │   ├── 📂 raw/
│   │   │   └── 📄 online_retail.csv
│   │   └── 📂 cleaned/
│   │       └── 📄 online_retail_cleaned.csv
│   └── 📂 outputs/
│       ├── 📄 before_after_cleaning.csv
│       ├── 📄 findings.md
│       ├── 📈 monthly_aov.svg
│       └── 📈 generated visualisations (*.png)
│
├── 📂 DataAnalytics-L1-CustomerSegmentation/
│   ├── 📄 README.md
│   ├── 📄 requirements.txt
│   ├── 📂 data/
│   │   └── 📄 README.md
│   ├── 📂 notebooks/
│   │   └── 📓 Online_Retail_Customer_Segmentation.ipynb
│   └── 📂 outputs/
│       ├── 📈 generated visualisations (*.png)
│       └── 📊 customer_segment_summary.csv
│
└── 📂 DataAnalytics-L2-FraudDetection/
    ├── 📄 README.md
    ├── 📄 .gitattributes
    ├── 📄 requirements.txt
    ├── 📂 data/
    │   ├── 📄 README.md
    │   └── 📄 creditcard.csv
    ├── 📂 notebooks/
    │   └── 📓 Fraud_Detection_SMOTE_Logistic_RF.ipynb
    └── 📂 results/
        ├── 📄 Fraud_Detection_Results.md
        ├── 📊 model_metrics.csv
        ├── 📊 random_forest_feature_importance.csv
        ├── 📄 results_summary.json
        └── 📈 evaluation visualisations (*.svg)
```

> **Git LFS:** Large datasets are tracked with Git LFS where required. After cloning, run `git lfs pull` to retrieve the actual dataset files.

---

## ⚙️ Automated Notebook Validation

The repository includes a GitHub Actions workflow for **Task 1 — EDA on Online Retail Sales**:

```text
.github/workflows/run-eda-retail-sales.yml
```

The workflow:

1. Checks out the repository with Git LFS support.
2. Sets up Python 3.11.
3. Installs the project's required dependencies.
4. Executes `EDA_Retail_Sales.ipynb` from top to bottom.
5. Verifies the cleaned dataset and required visualisations.
6. Confirms that notebook code cells were executed successfully.
7. Uploads the executed notebook, cleaned dataset and generated outputs as a workflow artifact.

The workflow has **read-only repository permissions** and does not automatically write generated files back to the `main` branch.

---

## 🎯 Internship Goal

The goal of this portfolio is to demonstrate practical, reproducible data analytics skills across the full analytics lifecycle:

**Data acquisition → Data cleaning → Exploratory analysis → Feature engineering → Visualisation → Machine learning → Evaluation → Interpretation → Business recommendations**

The projects are designed to show not only technical implementation, but also the ability to identify data limitations, explain analytical decisions and communicate results responsibly.

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ **Explore the individual project READMEs above for methodology, results, how-to-run instructions and detailed project documentation.**
