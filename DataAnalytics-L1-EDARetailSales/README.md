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

The analysis follows a reproducible **raw → clean → analyse → visualise → recommend** workflow. The notebook starts from the raw transaction file, applies the documented cleaning steps, saves the resulting cleaned dataset to `data/cleaned/`, and then performs the analysis.

The project documents important data limitations rather than making unsupported assumptions. The supplied dataset does not contain customer age, gender or a dedicated product-category field, so those analyses are not fabricated.

---

## 🎯 Objectives

- 🔍 Inspect and understand the structure and quality of the dataset
- 🧹 Clean and prepare transaction-level data for analysis
- 📊 Calculate mean, median, mode and standard deviation for key numerical variables
- 📈 Analyse monthly and quarterly revenue trends
- 🛍️ Identify high-volume and high-revenue products, with **Quantity Sold** as the definition of best-selling
- 🌍 Analyse revenue and order concentration across countries
- 📊 Examine relationships between quantity, unit price and revenue
- 💡 Identify useful business insights
- ✅ Provide actionable recommendations based on the analysis

---

## 📂 Dataset

The **Online Retail** dataset used for this project was originally obtained from Kaggle:

**Source:** [Kaggle — Online Retail Transaction Data](https://www.kaggle.com/datasets/thedevastator/online-retail-transaction-data)

The repository keeps both stages of the dataset:

```text
data/raw/online_retail.csv
data/cleaned/online_retail_cleaned.csv
```

The **raw dataset** is the input to the notebook. The **cleaned dataset** is the reproducible output of the notebook's cleaning stage and is retained as a project deliverable.

Because the CSV files are large, they are tracked with **Git LFS** rather than normal Git object storage. After cloning the repository, run `git lfs pull` before running the notebook so the actual datasets are downloaded instead of leaving only LFS pointer files in the working tree.

---

## 🧹 Data Cleaning

The notebook starts from `data/raw/online_retail.csv` and performs the following preparation steps:

1. Convert `InvoiceDate` to datetime.
2. Standardise relevant text fields by trimming whitespace.
3. Remove exact duplicate records where applicable.
4. Create a `Revenue` variable:

```text
Revenue = Quantity × UnitPrice
```

5. Identify cancelled invoices using the `C` invoice prefix.
6. Exclude cancellations/returns, non-positive quantities/prices and invalid dates from sales-performance analysis.
7. Retain transactions with missing `CustomerID` because a customer identifier is not required for transaction-level revenue analysis.
8. Save the resulting clean sales dataset to `data/cleaned/online_retail_cleaned.csv`.

For **product-level rankings**, the notebook additionally excludes shipping, service and administrative lines using the dataset's non-product stock codes (including postage, carriage, fees, discounts, manual entries and adjustments). This prevents logistics and administrative charges from being presented as products.

---

## 🔬 Analysis Performed

### 📐 Descriptive Statistics

For `Quantity`, `UnitPrice` and calculated `Revenue`, the notebook reports **mean, median, mode and standard deviation**.

### 📈 Sales Trends

Monthly and quarterly revenue trends were analysed to identify periods of stronger and weaker sales performance.

### 🛍️ Product Analysis

Products are ranked by **Quantity Sold** and **Revenue**. **Quantity Sold is the definition used for best-selling products.** Revenue is reported separately because a product can generate high revenue without being the highest-volume item.

### 🌍 Market Analysis

Country-level revenue and order counts were analysed to understand market concentration. This is retained as an additional business insight.

### 🔗 Correlation Analysis

A correlation heatmap examines relationships between `Quantity`, `UnitPrice`, and `Revenue`. The notebook includes an actual written interpretation and notes that `Revenue` is mechanically calculated as `Quantity × UnitPrice`.

### 👥 Customer Data

Where `CustomerID` is available, customer-level information is explored. However, the dataset does **not** contain age or gender fields, so those analyses are intentionally excluded.

### 🗂️ Product Category Limitation

The supplied dataset does **not** contain a dedicated product-category field. Therefore, revenue by product category cannot be calculated reliably without inventing categories. Product-level revenue and unit-volume analysis is provided instead. This is a documented dataset limitation, not a missing calculation.

---

## 📊 Visualisations

The project includes:

- Monthly revenue trend
- Quarterly revenue trend
- Top 10 products by units sold
- Top 10 products by revenue, corrected to exclude non-product lines
- Top 10 countries by revenue
- Top 10 countries by number of orders
- Correlation heatmap

The visualisations are generated from the notebook and stored in the project's `outputs/` directory, with a written interpretation placed underneath every visualization in the notebook.

---

## 💡 Key Findings

- **2011-11** was the strongest revenue month.
- **2011Q4** was the strongest revenue quarter.
- **PAPER CRAFT , LITTLE BIRDIE** was the best-selling product by **Quantity Sold**, with **80,995 units**.
- After excluding non-product lines, **REGENCY CAKESTAND 3 TIER** was the highest-revenue product at approximately **£174,484.74**.
- The **United Kingdom contributes approximately 84.6% of total revenue**.
- The **top 10 countries contribute approximately 97.2% of total revenue**.
- The dataset does not support age/gender analysis or reliable product-category analysis.

These results indicate substantial revenue concentration in the UK market and a meaningful difference between product volume and product revenue rankings.

---

## 🚀 Business Recommendations

1. **Plan around peak periods** — Align inventory, staffing and promotional activity with periods of stronger demand.
2. **Protect high-volume products** — Prioritise stock availability and explore cross-selling and bundling opportunities.
3. **Separate volume from value** — Use Quantity Sold to identify best-selling products while using Revenue to identify high-value products.
4. **Focus market investment** — Retain customers in major revenue markets while selectively testing smaller markets.
5. **Improve customer identification** — Increasing `CustomerID` capture would support stronger retention, frequency and customer-lifetime-value analysis.
6. **Collect missing business fields** — If age, gender or product-category analysis is required in future, obtain reliable fields rather than inferring them.

---

## 🛠️ Tools & Technologies

- **Python** — Analysis and programming
- **Pandas** — Data manipulation
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualisation
- **Seaborn** — Statistical visualisation
- **Jupyter Notebook** — Interactive analysis
- **Git LFS** — Large dataset versioning

---

## 📁 Project Structure

```text
DataAnalytics-L1-EDARetailSales/
│
├── 📂 data/
│   ├── 📂 raw/
│   │   └── online_retail.csv          ← Raw input • Git LFS tracked
│   └── 📂 cleaned/
│       └── online_retail_cleaned.csv  ← Notebook cleaning output • Git LFS tracked
│
├── 📂 outputs/
│   ├── before_after_cleaning.csv
│   ├── findings.md
│   └── *.png                           ← Generated visualisations
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
cd OIBSIP/DataAnalytics-L1-EDARetailSales
```

### 2. Make sure Git LFS is installed

```bash
git lfs install
```

### 3. Download the LFS-tracked datasets

```bash
git lfs pull
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Open Jupyter Notebook

```bash
jupyter notebook
```

### 6. Open and run

```text
EDA_Retail_Sales.ipynb
```

Run the notebook cells from top to bottom. The notebook reads the **raw** dataset from `data/raw/online_retail.csv`, performs the cleaning steps, writes the cleaned dataset to `data/cleaned/online_retail_cleaned.csv`, and generates the analysis outputs and visualisations.

> **Important:** Do not replace the raw input with the cleaned dataset. The two files serve different purposes in the project pipeline.

---

## 📈 Skills Demonstrated

This project demonstrates an end-to-end exploratory data analysis workflow:

**Raw data → Data inspection → Data cleaning → Feature creation → Descriptive statistics → Trend analysis → Product analysis → Market analysis → Correlation analysis → Visualisation → Business insights → Recommendations**

---

## 📋 Task Alignment

The project addresses the applicable requirements of the **OASIS INFOBYTE Data Analytics Level 1 retail-sales task**, including:

- data inspection and quality checks
- mean, median, mode and standard deviation
- monthly and quarterly trends
- top-product analysis by volume and revenue
- market analysis by country
- correlation analysis
- additional visualisation
- written observations accompanying the visualisations
- actionable business recommendations

Where the original task refers to **age/gender** and **product-category** analysis, the project explicitly documents that those fields are not present in the supplied dataset rather than fabricating findings. Product-level postage/non-product lines are also excluded from product rankings.

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ *Explore the repository to see the complete notebook, supporting data files and visualisations.*
