# 🛍️ Online Retail Customer Segmentation

### OASIS INFOBYTE SIP — Data Analytics Level 1 • Task 2

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-11557C?logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualisation-4C72B0)](https://seaborn.pydata.org/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

> **Turning retail transaction data into meaningful customer segments using RFM analysis and K-Means clustering.**

---

## 📌 Project Overview

Understanding **who your customers are, how recently they purchase, how frequently they buy, and how much they spend** is essential for effective customer retention and marketing.

In this project, I analyse the **Online Retail dataset** and combine **Recency, Frequency and Monetary (RFM) analysis** with **K-Means clustering** to identify groups of customers with similar purchasing behaviour.

The resulting customer profiles can help a business develop more targeted **retention, reactivation, cross-selling and customer-value strategies**.

---

## 🎯 Objectives

- 🔍 Explore and understand transactional retail data
- 🧹 Clean cancellations, returns, invalid prices, missing customer IDs and duplicate records
- 💰 Calculate transaction revenue
- 👥 Build customer-level RFM metrics
- 📊 Explore sales, product and country-level patterns
- ⚙️ Transform and standardise RFM features
- 📐 Evaluate possible cluster counts using the **Elbow Method** and **Silhouette Score**
- 🤖 Apply **K-Means clustering**
- 🧩 Profile the resulting customer segments
- 💡 Translate the findings into practical business recommendations

---

## 📂 Dataset

**Source:** UCI Machine Learning Repository — [Online Retail, Dataset 352](https://archive.ics.uci.edu/dataset/352/online+retail)

The dataset contains **541,909 transaction records** covering **1 December 2010 to 9 December 2011** from a UK-based non-store online retailer.

**Citation:** Chen, D. (2015). *Online Retail*. UCI Machine Learning Repository. DOI: `10.24432/C5BW33`.

The raw Excel dataset is **not stored in this repository** because of its file size. The notebook retrieves the dataset programmatically using `ucimlrepo`.

---

## 🧹 Data Cleaning & Preparation

Before performing customer segmentation, the transactional data is prepared by removing records that could distort customer-level analysis.

The cleaning process removes:

- ❌ Cancelled invoices
- ❌ Returned / negative-quantity transactions
- ❌ Non-positive prices
- ❌ Transactions without a customer ID
- ❌ Duplicate records

A `Revenue` variable is then calculated using:

```text
Revenue = Quantity × UnitPrice
```

This creates a clean transaction-level foundation for the RFM analysis.

---

## 🔎 Exploratory Data Analysis

The project explores the retail data before clustering customers, including:

### 📦 Product Analysis

Product-level purchasing patterns are examined to understand which items contribute to customer purchasing activity.

### 🌍 Country Analysis

Customer and transaction patterns are explored across countries to provide geographic context for the retailer's customer base.

### 💷 Revenue Analysis

Transaction revenue is calculated to support monetary-value analysis and customer profiling.

---

## 📊 RFM Analysis

Each customer is represented using three core behavioural metrics:

| Metric | Meaning |
|---|---|
| 🕐 **Recency** | How recently the customer purchased |
| 🔁 **Frequency** | How often the customer purchased |
| 💷 **Monetary** | How much revenue the customer generated |

These metrics transform individual transactions into a **customer-level behavioural profile** that can be used for segmentation.

---

## ⚙️ Feature Engineering & Transformation

RFM variables can be highly skewed, particularly **Frequency** and **Monetary** values.

To improve their suitability for clustering:

1. RFM features are calculated at customer level.
2. A **log transformation** is applied to reduce the effect of strong skewness.
3. Features are **standardised** so that variables with different scales do not dominate the clustering process.

---

## 📐 Choosing the Number of Clusters

Two evaluation techniques are used to assess candidate cluster counts:

- 📉 **Elbow Method** — examines within-cluster inertia as the number of clusters increases.
- 📈 **Silhouette Score** — evaluates how well customers fit within their assigned clusters compared with neighbouring clusters.

These measures provide a more evidence-based approach to selecting the final value of **k** rather than choosing the number of segments arbitrarily.

---

## 🤖 K-Means Customer Segmentation

After selecting the cluster count, **K-Means clustering** is applied to the transformed and standardised RFM features.

The algorithm groups customers according to similarities in their purchasing behaviour, producing distinct customer segments that can then be interpreted through their RFM profiles.

> **Important:** K-Means cluster numbers are arbitrary. A cluster labelled `0` is not inherently better or worse than a cluster labelled `1`; interpretation must be based on the actual RFM characteristics of each segment.

---

## 💡 Customer Segment Strategies

The customer profiles can support different business strategies depending on their observed RFM behaviour:

| Customer behaviour | Potential strategy |
|---|---|
| ⭐ **High-value and loyal** | Retention rewards, early access and personalised offers |
| 💎 **High monetary value but less frequent** | Cross-selling and repeat-purchase campaigns |
| ⚠️ **Inactive / at-risk** | Reactivation campaigns and targeted incentives |
| 🛒 **Frequent but lower-value purchases** | Bundles and recommendations to increase basket value |

The objective is to move beyond simply identifying clusters and translate customer behaviour into **actionable marketing decisions**.

---

## 🛠️ Tools & Technologies

- **Python** — Programming and analysis
- **Pandas** — Data manipulation
- **NumPy** — Numerical computing
- **Matplotlib** — Data visualisation
- **Seaborn** — Statistical visualisation
- **Scikit-learn** — Standardisation, K-Means and clustering evaluation
- **Jupyter Notebook** — Interactive analysis
- **UCI ML Repository / ucimlrepo** — Dataset acquisition

---

## 📁 Project Structure

```text
DataAnalytics-L1-CustomerSegmentation/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📂 data/
│   └── 📄 README.md
│
└── 📂 notebooks/
    └── 📓 Online_Retail_Customer_Segmentation.ipynb
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Ros3-0SS/OIBSIP.git
```

### 2️⃣ Open the project folder

```bash
cd OIBSIP/DataAnalytics-L1-CustomerSegmentation
```

### 3️⃣ Install the required packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Open the notebook

Open:

```text
notebooks/Online_Retail_Customer_Segmentation.ipynb
```

### 5️⃣ Run the notebook from top to bottom

An internet connection is required because the notebook retrieves the dataset from the UCI Machine Learning Repository.

---

## 📈 Skills Demonstrated

This project demonstrates an end-to-end **data analytics and unsupervised machine learning workflow**:

**Data acquisition → Data cleaning → Exploratory analysis → Revenue calculation → RFM analysis → Feature engineering → Data transformation → Feature scaling → Cluster evaluation → K-Means clustering → Customer profiling → Business recommendations**

---

## ✅ Oasis Infobyte Task Alignment

This project addresses the core customer segmentation workflow through:

- ✔️ Data exploration and preparation
- ✔️ Customer-level analysis
- ✔️ RFM analysis
- ✔️ Feature transformation and standardisation
- ✔️ Elbow Method evaluation
- ✔️ Silhouette Score evaluation
- ✔️ K-Means clustering
- ✔️ Customer segment profiling
- ✔️ Business-oriented interpretation and recommendations

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**

Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ *If you find this project useful, feel free to explore the other analytics projects in this repository.*
