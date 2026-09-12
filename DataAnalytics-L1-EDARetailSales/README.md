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

The project explicitly documents dataset limitations instead of inventing unavailable information. Two requested analyses are **impossible with the supplied dataset**: **age/gender analysis** because there are no age or gender fields, and **product-category analysis** because there is no dedicated product-category field.

---

## 🎯 Objectives

- 🔍 Inspect and understand the structure and quality of the dataset
- 🧹 Clean and prepare transaction-level data for analysis
- 📊 Calculate mean, median, mode and standard deviation for key numerical variables
- 📈 Analyse monthly and quarterly revenue trends
- 💷 Analyse monthly **Average Order Value (AOV)** to understand changes in average customer basket size
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

## 📐 Descriptive Statistics — Why These Measures Matter

The descriptive-statistics requirement is applied to the three numerical variables with direct business meaning: **Quantity, UnitPrice and Revenue**. The CSV `index` column is a technical row identifier, not a business measure, so it is intentionally excluded.

The project reports all four requested measures because each provides different information:

- **Mean:** the arithmetic average and a useful measure of overall transaction scale, but sensitive to unusually large purchases.
- **Median:** the middle transaction value and a better indicator of a typical transaction when values are skewed.
- **Mode:** the most frequently occurring value, useful for identifying the most common quantity, price or revenue value.
- **Standard deviation:** measures how widely transactions vary around the mean.

| Variable | Mean | Median | Mode | Standard deviation |
|---|---:|---:|---:|---:|
| Quantity | 10.54 | 3.00 | 1.00 | 155.52 |
| UnitPrice | £3.91 | £2.08 | £1.25 | £35.92 |
| Revenue | £20.12 | £9.90 | £15.00 | £270.36 |

The large mean–median gaps, especially for **Quantity (10.54 vs 3)** and **Revenue (£20.12 vs £9.90)**, indicate that transaction-level values are right-skewed and influenced by larger purchases. The relatively large standard deviations also show substantial transaction variability. Therefore, using the mean alone would not adequately describe the typical transaction; the median and dispersion measure are necessary for a more complete interpretation.

---

## 📈 Analysis Performed

### 📐 Descriptive Statistics

For `Quantity`, `UnitPrice` and calculated `Revenue`, the notebook reports **mean, median, mode and standard deviation**, with a written justification for why each statistic is relevant.

### 📈 Sales Trends

Monthly and quarterly revenue trends were analysed to identify periods of stronger and weaker sales performance.

### 💷 Average Order Value (AOV)

AOV is calculated as **monthly revenue divided by monthly unique invoices**. The analysis identifies the highest and lowest AOV months and compares average basket value over time.

- **Overall AOV:** £534.40
- **Highest monthly AOV:** 2011-12 — £779.97
- **Lowest monthly AOV:** 2011-04 — £431.63

The AOV chart provides an additional visualisation that helps distinguish changes in revenue caused by transaction volume from changes caused by average spend per order.

### 🛍️ Product Analysis

Products are ranked by **Quantity Sold** and **Revenue**. **Quantity Sold is the definition used for best-selling products.** Revenue is reported separately because a product can generate high revenue without being the highest-volume item.

### 🌍 Market Analysis

Country-level revenue and order counts were analysed to understand market concentration. This is retained as an additional business insight.

### 🔗 Correlation Analysis

A correlation heatmap examines relationships between `Quantity`, `UnitPrice`, and `Revenue`. The notebook includes a written interpretation and notes that `Revenue` is mechanically calculated as `Quantity × UnitPrice`.

### 👥 Customer Data

Where `CustomerID` is available, customer-level information is explored. However, the dataset does **not** contain age or gender fields, so those analyses are intentionally excluded.

---

## ⚠️ Explicit Dataset Limitations — Two Impossible Requirements

### 1. Age and gender analysis — impossible with the supplied dataset

The dataset contains **no age field and no gender field**. There is therefore no reliable variable from which to calculate age groups or gender-based sales patterns. Inferring these attributes from names, descriptions, countries or other fields would introduce unsupported assumptions. **Age/gender analysis is omitted because the required data does not exist.**

### 2. Product-category analysis — impossible with the supplied dataset

The dataset contains **no dedicated product-category field**. Stock codes and descriptions identify individual products but do not provide an authoritative category taxonomy. Creating categories manually would introduce subjective classifications. **Product-category revenue analysis is omitted because the required data does not exist.**

These are documented **dataset limitations**, not missing calculations.

---

## 📊 Visualisations & Written Observations

Every chart has a corresponding visible observation in the notebook and `outputs/findings.md`:

| Chart | Observation |
|---|---|
| Monthly revenue trend | **2011-11** is the peak month at **£1,509,496.33**, showing a strong late-year sales peak. |
| Quarterly revenue trend | **2011Q4** is the strongest quarter at **£3,303,268.31**, confirming the late-year increase extends beyond one month. |
| Monthly AOV | **2011-12** has the highest AOV at **£779.97**, while **2011-04** has the lowest at **£431.63**; overall AOV is **£534.40**. |
| Top 10 countries by revenue | The **United Kingdom contributes 84.6%** of total revenue, showing strong market concentration. |
| Top 10 countries by orders | The UK leads with **18,019 unique invoices**, reinforcing its importance. |
| Top 10 products by units sold | **PAPER CRAFT , LITTLE BIRDIE** leads with **80,995 units**. |
| Top 10 products by revenue | **REGENCY CAKESTAND 3 TIER** leads at **£174,484.74** after non-product lines are excluded. |
| Correlation heatmap | **Quantity–Revenue r = 0.91**; the strong relationship is expected because Revenue = Quantity × UnitPrice. |

---

## 💡 Key Findings

- **2011-11** was the strongest revenue month.
- **2011Q4** was the strongest revenue quarter.
- **December 2011** had the highest monthly AOV at **£779.97**, compared with the overall AOV of **£534.40**.
- **PAPER CRAFT , LITTLE BIRDIE** was the best-selling product by **Quantity Sold**, with **80,995 units**.
- After excluding non-product lines, **REGENCY CAKESTAND 3 TIER** was the highest-revenue product at approximately **£174,484.74**.
- The **United Kingdom contributes approximately 84.6% of total revenue**.
- The **top 10 countries contribute approximately 97.2% of total revenue**.
- The large mean–median differences show that transaction values are skewed, so median and standard deviation are important alongside the mean.
- The dataset does not support age/gender analysis or reliable product-category analysis.

These results indicate substantial revenue concentration in the UK market, a meaningful difference between product volume and product revenue rankings, and variation in average basket value across months.

---

## 🚀 Business Recommendations

1. **Plan around peak periods** — Align inventory, staffing and promotional activity with periods of stronger demand.
2. **Protect high-volume products** — Prioritise stock availability and explore cross-selling and bundling opportunities.
3. **Use AOV to grow basket size** — Monitor AOV alongside order volume and test bundles, cross-selling and targeted promotions during lower-AOV periods.
4. **Separate volume from value** — Use Quantity Sold to identify best-selling products while using Revenue to identify high-value products.
5. **Focus market investment** — Retain customers in major revenue markets while selectively testing smaller markets.
6. **Improve customer identification** — Increasing `CustomerID` capture would support stronger retention, frequency and customer-lifetime-value analysis.
7. **Collect missing business fields** — If age, gender or product-category analysis is required in future, obtain reliable fields rather than inferring them.

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
│   ├── monthly_aov.svg
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

**Raw data → Data inspection → Data cleaning → Feature creation → Descriptive statistics → Trend analysis → AOV analysis → Product analysis → Market analysis → Correlation analysis → Visualisation → Business insights → Recommendations**

---

## 📋 Task Alignment

The project addresses the applicable requirements of the **OASIS INFOBYTE Data Analytics Level 1 retail-sales task**, including:

- data inspection and quality checks
- mean, median, mode and standard deviation with numerical justification
- monthly and quarterly trends
- top-product analysis by volume and revenue
- market analysis by country
- correlation analysis
- additional AOV visualisation revealing variation in average basket value
- visible written observations accompanying every visualization
- actionable business recommendations
- explicit documentation of unavailable dataset fields

The two unavailable analyses are intentionally marked as dataset limitations: **age/gender analysis** cannot be performed because those fields do not exist, and **product-category analysis** cannot be performed because no dedicated category field exists. Product-level postage/non-product lines are also excluded from product rankings.

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**  
Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ *Explore the repository to see the complete notebook, supporting data files and visualisations.*
