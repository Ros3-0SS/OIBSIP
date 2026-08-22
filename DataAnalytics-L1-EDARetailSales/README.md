# EDA on Online Retail Sales

## Oasis Infobyte — Data Analytics Level 1, Task 1

Exploratory Data Analysis of the supplied **Online Retail** transaction dataset.

### Project status

- Dataset loaded and analysed: ✅
- Data cleaning: ✅
- EDA: ✅
- Visualisations: ✅
- Findings and recommendations: ✅
- Professional README: ✅
- GitHub upload: pending repository access

### Dataset summary

| Metric | Result |
|---|---:|
| Original transaction lines | 541,909 |
| Duplicate rows found | 0 |
| Duplicate rows removed | 0 |
| Clean sales transaction lines | 530,104 |
| Unique invoices | 19,960 |
| Unique products | 3,922 |
| Countries | 38 |
| Peak revenue month | 2011-11 |
| Peak revenue quarter | 2011Q4 |

### Key findings

- The strongest revenue month is **2011-11**.
- The strongest revenue quarter is **2011Q4**.
- **PAPER CRAFT , LITTLE BIRDIE** is the highest-volume product by units sold.
- The United Kingdom contributes approximately **84.6%** of total revenue.
- The top 10 countries contribute approximately **97.2%** of total revenue.
- Average revenue per invoice is approximately **534.40**, compared with a median of **303.84**.

### Important dataset limitation

The supplied Online Retail dataset contains `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, and `Country`. It **does not contain customer age or gender**, so those analyses are not fabricated. Country/market analysis is used instead.

### Cleaning approach

1. Converted `InvoiceDate` to datetime.
2. Standardised text fields by trimming whitespace.
3. Removed exact duplicate records.
4. Created `Revenue = Quantity × UnitPrice`.
5. Identified cancelled invoices using the `C` invoice prefix.
6. Excluded cancellations/returns, non-positive quantities/prices, and invalid dates from sales-performance analysis.
7. Retained rows with missing `CustomerID` because transaction-level revenue analysis does not require a customer identifier.

### Visualisations

The project includes:

- Monthly revenue trend
- Quarterly revenue trend
- Top 10 products by units sold
- Top 10 countries by revenue
- Top 10 countries by number of orders
- Correlation heatmap
- Revenue-concentration/customer analysis

### Business recommendations

1. **Plan around peak periods:** align inventory, staffing, and promotions with the strongest monthly and quarterly demand.
2. **Protect high-volume products:** prioritise stock availability and use cross-selling/bundling opportunities.
3. **Focus market investment:** retain customers in major revenue markets while testing smaller markets with targeted campaigns.
4. **Improve customer identification:** increase CustomerID capture to enable stronger retention, frequency, and customer-lifetime-value analysis.

### Repository structure

```text
DataAnalytics-L1-EDARetailSales/
├── data/
│   ├── raw/
│   │   └── online_retail.csv
│   └── cleaned/
│       └── online_retail_cleaned.csv
├── outputs/
│   ├── before_after_cleaning.csv
│   ├── findings.md
│   └── *.png
├── EDA_Retail_Sales.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

### Run locally

```bash
pip install -r requirements.txt
jupyter notebook
```

Then open `EDA_Retail_Sales.ipynb` and run all cells.

### Submission alignment

The Oasis Infobyte Data Analytics Level 1 retail-sales task requires inspection, descriptive statistics, monthly/quarterly trends, demographic analysis, product/category analysis, a correlation heatmap, an additional visualisation, observations, and at least three actionable recommendations. This implementation covers the applicable requirements using the fields actually present in the supplied dataset.
