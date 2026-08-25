# Online Retail Customer Segmentation

**OASIS INFOBYTE SIP — Data Analytics Level 1, Task 2**

This project analyses the **UCI Online Retail** dataset and segments customers according to purchasing behaviour using **RFM analysis and K-Means clustering**.

## Objectives

- Explore and clean transactional retail data.
- Calculate customer-level Recency, Frequency and Monetary (RFM) measures.
- Visualise sales trends, product performance and country-level revenue.
- Standardise RFM features and evaluate cluster counts with the Elbow Method and silhouette score.
- Apply K-Means clustering.
- Profile customer segments and translate them into practical marketing recommendations.

## Dataset

Source: UCI Machine Learning Repository, **Online Retail (Dataset 352)**.

The dataset contains 541,909 transaction rows covering 1 December 2010 to 9 December 2011. The retailer is a UK-based non-store online business. UCI identifies the dataset as suitable for clustering and provides the citation: Chen, D. (2015). *Online Retail*. UCI Machine Learning Repository. DOI: `10.24432/C5BW33`. The dataset is licensed under CC BY 4.0.

The raw Excel file is not committed to this repository because it is approximately 22.6 MB. The notebook downloads it through `ucimlrepo`.

## Project Structure

```text
DataAnalytics-L1-CustomerSegmentation/
├── README.md
├── requirements.txt
├── data/
│   └── README.md
└── notebooks/
    └── Online_Retail_Customer_Segmentation.ipynb
```

## Methodology

1. Load the UCI dataset.
2. Inspect missing values, duplicates, cancellations, returns and invalid prices.
3. Remove cancelled transactions, returns, invalid prices, missing customer IDs and duplicate rows for the segmentation model.
4. Create `Revenue = Quantity × UnitPrice`.
5. Build customer-level RFM features.
6. Apply log transformation and standardisation.
7. Compare candidate K-Means cluster counts using inertia and silhouette score.
8. Fit the final K-Means model.
9. Profile the customer groups.
10. Recommend retention, reactivation, cross-selling and basket-value strategies based on the segment profiles.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- UCI ML Repository / `ucimlrepo`

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then open:

`notebooks/Online_Retail_Customer_Segmentation.ipynb`

Run the notebook from top to bottom. An internet connection is required for the automatic UCI dataset download.

## Portfolio Outcome

The notebook demonstrates an end-to-end analytics workflow: data acquisition, data cleaning, exploratory analysis, feature engineering, RFM analysis, unsupervised machine learning, cluster evaluation, customer profiling and business recommendations.
