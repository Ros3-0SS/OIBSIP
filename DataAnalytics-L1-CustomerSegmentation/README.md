#  Online Retail Customer Segmentation

### OASIS INFOBYTE SIP — Data Analytics Level 1 • Task 2

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

> **A customer segmentation project using RFM analysis and K-Means clustering to turn retail transaction data into actionable customer insights.**

---

## 📌 Project Overview

Understanding **who your customers are, how often they buy, and how much they spend** is essential for effective customer retention and marketing.

In this project, I analyse the **UCI Online Retail dataset** and use **Recency, Frequency and Monetary (RFM) analysis** together with **K-Means clustering** to identify groups of customers with similar purchasing behaviour.

The final segments can help a business design more targeted retention, reactivation, cross-selling and customer-value strategies.

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

## 🔬 Methodology

### 1️⃣ Data acquisition
The Online Retail dataset is loaded directly from the UCI Machine Learning Repository.

### 2️⃣ Data cleaning
The analysis removes:

- Cancelled invoices
- Returned/negative-quantity transactions
- Non-positive prices
- Transactions without a customer ID
- Duplicate records

A `Revenue` variable is then calculated as:

```text
Revenue = Quantity × UnitPrice
```

### 3️⃣ RFM analysis
Each customer is evaluated using:

| Metric | Meaning |
|---|---|
| 🕐 **Recency** | How recently the customer purchased |
| 🔁 **Frequency** | How often the customer purchased |
| 💷 **Monetary** | How much revenue the customer generated |

### 4️⃣ Feature preparation
Because RFM variables can be highly skewed, a log transformation is applied before standardisation.

### 5️⃣ Cluster selection
Candidate values of **k** are compared using:

- 📉 Elbow Method / inertia
- 📈 Silhouette Score

### 6️⃣ K-Means clustering
The selected number of clusters is used to train the final K-Means model.

### 7️⃣ Customer profiling
The resulting groups are compared using their RFM characteristics so that each cluster can be interpreted from a business perspective.

---

## 💡 Business Insights

The customer profiles can support strategies such as:

| Customer behaviour | Potential strategy |
|---|---|
| ⭐ High-value and loyal | Retention rewards, early access and personalised offers |
| 💎 High monetary value but less frequent | Cross-selling and repeat-purchase campaigns |
| ⚠️ Inactive / at-risk | Reactivation campaigns and targeted incentives |
| 🛒 Frequent but lower-value purchases | Bundles and recommendations to increase basket value |

> **Note:** K-Means cluster numbers are arbitrary. The segments should therefore be interpreted from their RFM profiles rather than simply by cluster number.

---

## 🛠️ Tools & Technologies

- **Python** — Programming and analysis
- **Pandas** — Data manipulation
- **NumPy** — Numerical computing
- **Matplotlib** — Visualisation
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

### 1. Clone the repository

```bash
git clone https://github.com/Ros3-0SS/OIBSIP.git
```

### 2. Open the project folder

```bash
cd OIBSIP/DataAnalytics-L1-CustomerSegmentation
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Open the notebook

Open:

```text
notebooks/Online_Retail_Customer_Segmentation.ipynb
```

### 5. Run the notebook from top to bottom

An internet connection is required because the notebook retrieves the dataset from the UCI Machine Learning Repository.

---

## 📈 Portfolio Skills Demonstrated

This project demonstrates an end-to-end data analytics and machine learning workflow:

**Data acquisition → Data cleaning → Exploratory analysis → Feature engineering → RFM analysis → Feature scaling → Unsupervised machine learning → Cluster evaluation → Customer profiling → Business recommendations**

---

## 👩🏽‍💻 Author

**Ntsako Sibanda**

Data Analytics Portfolio • OASIS INFOBYTE SIP

---

⭐ *If you find this project useful, feel free to explore the other analytics projects in this repository.*
