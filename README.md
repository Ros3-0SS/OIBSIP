# OIBSIP

## Oasis Infobyte Internship — Data Analytics

This repository contains my **Oasis Infobyte Internship** projects for the Data Analytics track. The projects demonstrate practical skills in data cleaning, exploratory data analysis, visualisation, customer segmentation, machine learning, model evaluation and business recommendations.

## 📊 Data Analytics Projects

### Level 1

#### Task 1 — EDA on Online Retail Sales
`DataAnalytics-L1-EDARetailSales/`

Exploratory Data Analysis of online retail transactions, including data cleaning, descriptive statistics, revenue trends, Average Order Value (AOV), product analysis, country analysis, correlation analysis, visualisations, findings and business recommendations.

The notebook is validated automatically through **GitHub Actions**. The workflow executes the notebook from top to bottom, verifies the generated dataset and visualisations, and stores the execution results as a workflow artifact without creating automated commits on the `main` branch.

The Online Retail Sales EDA project demonstrates an end-to-end analytics workflow:

Raw data → Data inspection → Data cleaning → Feature engineering → Descriptive statistics → Trend analysis → AOV analysis → Product analysis → Country analysis → Correlation analysis → Visualisation → Findings → Business recommendations

The project also documents important dataset limitations instead of making unsupported assumptions. In particular, the supplied retail dataset does not contain reliable age/gender fields or a dedicated product-category field, so those analyses are not fabricated.

#### Task 2 — Online Retail Customer Segmentation
`DataAnalytics-L1-CustomerSegmentation/`

Customer segmentation using the UCI Online Retail dataset, RFM analysis and K-Means clustering. The project includes data preparation, exploratory analysis, feature engineering, standardisation, the Elbow Method, silhouette scoring, cluster profiling, visualisation and marketing recommendations.

### Level 2

#### Task 3 — Fraud Detection
`DataAnalytics-L2-FraudDetection/`

Machine-learning fraud detection on a heavily imbalanced financial transaction dataset. The project uses exploratory data analysis, stratified train-test splitting, feature scaling, SMOTE oversampling, Logistic Regression and Random Forest models. Models are evaluated using Precision, Recall, F1-score and ROC-AUC, with confusion matrices, ROC curves and Random Forest feature importance included.

**Key result:** Random Forest achieved the strongest overall balance, with **80.0% precision, 85.7% recall, 82.8% F1-score and 97.8% ROC-AUC** on the test set.

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
