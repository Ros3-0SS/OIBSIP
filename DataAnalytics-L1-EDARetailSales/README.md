# 📊 EDA on Online Retail Sales

### OASIS INFOBYTE SIP — Data Analytics Level 1 • Task 1

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-11557c)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

> **An exploratory data analysis project examining retail transactions, revenue trends, products, markets and customer-related data to uncover actionable business insights.**

---

## 📌 Project Overview

This project performs an **Exploratory Data Analysis (EDA)** of the Online Retail transaction dataset.

The analysis focuses on understanding sales performance over time, identifying high-performing products and markets, examining relationships between numerical variables, and translating the findings into practical business recommendations.

The project also documents important data limitations rather than making unsupported assumptions. For example, the dataset does not contain customer age or gender, so demographic conclusions are not fabricated.

---

## 🎯 Objectives

- 🔍 Inspect and understand the structure and quality of the dataset
- 🧹 Clean and prepare transaction-level data for analysis
- 📈 Analyse monthly and quarterly revenue trends
- 🛍️ Identify high-volume products
- 🌍 Analyse revenue and order concentration across countries
- 📊 Examine relationships between quantity, unit price and revenue
- 💡 Identify useful business insights
- ✅ Provide actionable recommendations based on the analysis

---

## 📂 Dataset

The raw **Online Retail** dataset used for this project was obtained from Kaggle:

**Source:** [Kaggle — Online Retail Transaction Data](https://www.kaggle.com/datasets/thedevastator/online-retail-transaction-data)

The raw CSV is **not duplicated in this repository** in order to keep the repository lightweight. The original dataset can be obtained from the source above.

### Dataset summary

| Metric | Result |
|---|---:|
| Original transaction lines | 541,909 |
| Clean sales transaction lines | 530,104 |
| Unique invoices | 19,960 |
| Unique products | 3,922 |
| Countries | 38 |
| Peak revenue month | 2011-11 |
| Peak revenue quarter | 2011Q4 |

---

## 🧹 Data Cleaning

The following preparation steps were performed:

1. Converted `InvoiceDate` to datetime.
2. Standardised relevant text fields by trimming whitespace.
3. Removed exact duplicate records where applicable.
4. Created a `Revenue` variable:

```text
Revenue = Quantity × UnitPrice
```

5. Identified cancelled invoices using the `C` invoice prefix.
6. Excluded cancellations/returns, non-positive quantities/prices and invalid dates from sales-performance analysis.
7. Retained transactions with missing `CustomerID` because a customer identifier is not required for transaction-level revenue analysis.

---

## 🔬 Analysis Performed

### 📈 Sales Trends

Monthly and quarterly revenue trends were analysed to identify periods of stronger and weaker sales performance.

### 🛍️ Product Analysis

Products were ranked by units sold to identify the highest-volume products.

### 🌍 Market Analysis

Country-level revenue and order counts were analysed to understand market concentration.

### 🔗 Correlation Analysis

A correlation heatmap was used to examine relationships between key numerical variables such as `Quantity`, `UnitPrice`, and `Revenue`.

### 👥 Customer Data

Where `CustomerID` is available, customer-level information is explored. However, the dataset does **not** contain age or gender fields, so those analyses are intentionally excluded.

---

## 📊 Visualisations

The project includes:

- Monthly revenue trend
- Quarterly revenue trend
- Top 10 products by units sold
- Top 10 countries by revenue
- Top 10 countries by number of orders
- Correlation heatmap
- Additional revenue/customer analysis

The visualisations are generated from the notebook and stored in the project's `outputs/` directory.

---

## 💡 Key Findings

- **2011-11** was the strongest revenue month.
- **2011Q4** was the strongest revenue quarter.
- **PAPER CRAFT , LITTLE BIRDIE** was the highest-volume product by units sold.
- The **United Kingdom contributes approximately 84.6% of total revenue**.
- The **top 10 countries contribute approximately 97.2% of total revenue**.
- Average revenue per invoice is approximately **534.40**, compared with a median of approximately **303.84**.

These results indicate substantial revenue concentration in the UK market and a noticeable difference between average and median invoice revenue.

---

## 🚀 Business Recommendations

1. **Plan around peak periods** — Align inventory, staffing and promotional activity with periods of stronger demand.
2. **Protect high-volume products** — Prioritise stock availability and explore cross-selling and bundling opportunities.
3. **Focus market investment** — Retain customers in major revenue markets while selectively testing smaller markets.
4. **Improve customer identification** — Increasing `CustomerID` capture would support stronger retention, frequency and customer-lifetime-value analysis.

---

## 🛠️ Tools & Technologies

- **Python** — Analysis and programming
- **Pandas** — Data manipulation
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualisation
- **Seaborn** — Statistical visualisation
- **Jupyter Notebook** — Interactive analysis

---

## 📁 Project Structure

```text
DataAnalytics-L1-EDARetailSales/
│
├── 📂 data/
│   └── 📂 cleaned/
│       └── online_retail_cleaned.csv
│
├── 📂 outputs/
│   ├── before_after_cleaning.csv
│   ├── findings.md
│   └── *.png
│
├── 📓 EDA_Retail_Sales.ipynb
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Ros3-0SS/OIBSIP.git
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Open Jupyter Notebook

```bash
jupyter notebook
```

### 4. Open

```text
EDA_Retail_Sales.ipynb
```

Run the notebook cells from top to bottom to reproduce the analysis and visualisations.

---

## 📈 Skills Demonstrated

This project demonstrates an end-to-end exploratory data analysis workflow:

**Data inspection → Data cleaning → Feature creation → Descriptive statistics → Trend analysis → Product analysis → Market analysis → Correlation analysis → Visualisation → Business insights → Recommendations**

---

## 📋 Task Alignment

The project addresses the applicable requirements of the **OASIS INFOBYTE Data Analytics Level 1 retail-sales task**, including data inspection, descriptive statistics, monthly/quarterly trends, product/category analysis, correlation analysis, additional visualisation, observations and actionable recommendations.

Where the original task refers to demographic analysis, the project explicitly documents that **age and gender are not present in the supplied dataset** rather than fabricating demographic findings.

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ *Explore the repository to see the complete notebook, supporting data files and visualisations.*
