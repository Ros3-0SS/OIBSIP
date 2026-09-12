# Findings

## Dataset and cleaning
- Original transaction lines: **541,909**.
- Exact duplicate rows identified after loading the supplied project CSV: **0** (the CSV contains a unique `index` field, so exact-row duplicates are not detected here).
- Cancelled invoices, non-positive quantities/prices and invalid dates were excluded from sales-performance analysis.
- Clean sales transaction lines: **530,104**.
- CustomerID is missing for **132,220** cleaned transaction lines.

## Descriptive statistics — numerical justification
The descriptive-statistics requirement is applied to the three numerical variables that have direct business meaning: **Quantity, UnitPrice and Revenue**. The CSV `index` column is only a technical row identifier, so including it would produce statistics with no commercial interpretation.

For each business variable, the project reports **mean, median, mode and standard deviation** because they answer different questions:
- **Mean:** average transaction-level value, useful for estimating typical arithmetic scale but sensitive to unusually large transactions.
- **Median:** middle transaction value, useful for describing the typical transaction when the distribution is skewed.
- **Mode:** most frequently occurring value, useful for identifying the most common quantity, price or revenue value.
- **Standard deviation:** measures transaction-to-transaction dispersion around the mean and shows how variable the observations are.

The results are:

| Variable | Mean | Median | Mode | Standard deviation |
|---|---:|---:|---:|---:|
| Quantity | 10.54 | 3.00 | 1.00 | 155.52 |
| UnitPrice | £3.91 | £2.08 | £1.25 | £35.92 |
| Revenue | £20.12 | £9.90 | £15.00 | £270.36 |

The large gap between mean and median, especially for **Quantity (10.54 vs 3)** and **Revenue (£20.12 vs £9.90)**, indicates that the transaction-level distributions are right-skewed and influenced by larger purchases. Therefore, the median is important alongside the mean; reporting only the mean would hide the typical transaction experience. The relatively large standard deviations reinforce that transaction values vary substantially across orders.

## Average Order Value (AOV)
Average Order Value is calculated as **total monthly revenue divided by the number of unique invoices in that month**. This provides a customer-spending perspective that complements total revenue and order volume.

- **Overall AOV:** £534.40.
- **Highest monthly AOV:** **2011-12 — £779.97**.
- **Lowest monthly AOV:** **2011-04 — £431.63**.

The AOV trend is an additional visualisation that reveals whether changes in revenue are associated with larger or smaller average customer baskets. Tracking AOV alongside order counts can help management distinguish transaction-volume growth from increased spend per order.

## Dataset limitations — two impossible requirements
The following two requested analyses are **impossible with the supplied dataset**, rather than merely unfinished:

### 1. Age and gender analysis — impossible from the supplied fields
The dataset contains **no age field and no gender field**. There is therefore no reliable variable from which to calculate age groups or gender-based sales patterns. Inferring these attributes from names, descriptions, countries or other fields would introduce unsupported assumptions and would not be valid EDA. **Age/gender analysis is explicitly omitted because the required data does not exist.**

### 2. Product-category analysis — impossible from the supplied fields
The dataset contains **no dedicated product-category field**. Stock codes and descriptions identify individual products but do not provide an authoritative category taxonomy. Creating categories manually would introduce subjective classifications and could change the results. **Revenue by product category is explicitly omitted because the required data does not exist.**

These are documented **dataset limitations**, not missing calculations.

## Product-level methodology
- **Best-selling products are defined by total Quantity Sold**, not revenue.
- Product revenue is calculated as **Quantity × UnitPrice**.
- Shipping/service/administrative lines were excluded from product-level rankings using the non-product stock codes: `POST`, `DOT`, `C2`, `23444`, `BANK CHARGES`, `AMAZONFEE`, `B`, `S`, `D`, `M`/`m`.
- This correction removes non-product lines such as `DOTCOM POSTAGE`, `POSTAGE`, `CARRIAGE`, `AMAZON FEE`, `Discount`, `Manual`, `Samples` and `Adjust bad debt` from product-level analysis.

## Corrected top products by revenue
1. **REGENCY CAKESTAND 3 TIER** — **£174,484.74**
2. **PAPER CRAFT , LITTLE BIRDIE** — **£168,469.60**
3. **WHITE HANGING HEART T-LIGHT HOLDER** — **£106,292.77**
4. **PARTY BUNTING** — **£99,504.33**
5. **JUMBO BAG RED RETROSPOT** — **£94,340.05**
6. **MEDIUM CERAMIC TOP STORAGE JAR** — **£81,700.92**
7. **RABBIT NIGHT LIGHT** — **£66,964.99**
8. **PAPER CHAIN KIT 50'S CHRISTMAS** — **£64,952.29**
9. **ASSORTED COLOUR BIRD ORNAMENT** — **£59,094.93**
10. **CHILLI LIGHTS** — **£54,117.76**

The previous revenue leader, **DOTCOM POSTAGE**, is intentionally absent because it is a shipping/service charge rather than a product.

## Best-selling products by Quantity Sold
- Leading product by units: **PAPER CRAFT , LITTLE BIRDIE**, with **80,995 units**.
- Best-selling status is therefore based on **Quantity Sold**, while revenue is a separate performance measure.

## Visible chart observations
Every project chart has a corresponding written observation in the notebook and this findings file:

1. **Monthly revenue trend:** **2011-11** is the peak month at **£1,509,496.33**, showing a strong late-year sales peak.
2. **Quarterly revenue trend:** **2011Q4** is the strongest quarter at **£3,303,268.31**, confirming that the late-year increase extends beyond a single month.
3. **Monthly AOV:** **2011-12** has the highest average order value at **£779.97**, while **2011-04** has the lowest at **£431.63**; the overall AOV is **£534.40**.
4. **Top 10 countries by revenue:** the **United Kingdom contributes 84.6%** of total revenue, showing strong market concentration.
5. **Top 10 countries by orders:** the United Kingdom leads with **18,019 unique invoices**, reinforcing the importance of the domestic market.
6. **Top 10 products by units sold:** **PAPER CRAFT , LITTLE BIRDIE** leads with **80,995 units**, making it the highest-volume product.
7. **Top 10 products by revenue:** **REGENCY CAKESTAND 3 TIER** leads at **£174,484.74** after non-product lines are excluded, demonstrating that the revenue leader differs from the volume leader.
8. **Correlation heatmap:** **Quantity and Revenue correlate at 0.91**, while **UnitPrice and Revenue correlate at 0.14**; the strong Quantity–Revenue relationship is expected because Revenue is calculated as Quantity × UnitPrice.

## Sales trends
- Highest-revenue month: **2011-11**, revenue **£1,509,496.33**.
- Highest-revenue quarter: **2011Q4**, revenue **£3,303,268.31**.

## Country analysis — additional insight
- United Kingdom revenue share: approximately **84.6%**.
- Top 10 countries revenue share: approximately **97.2%**.
- United Kingdom unique invoices: **18,019**.

## Correlation interpretation
- Quantity and Revenue have a strong positive correlation of **0.91**.
- UnitPrice and Revenue have a weak positive correlation of **0.14**.
- Quantity and UnitPrice are essentially uncorrelated at **-0.00**.
- These relationships should not be interpreted as independent causation because **Revenue is mechanically calculated as Quantity × UnitPrice**.

## Actionable recommendations
1. Plan inventory, staffing, and campaigns around peak periods.
2. Protect high-volume products while separately monitoring high-revenue products.
3. Prioritise the UK market while selectively testing international growth.
4. Monitor AOV alongside order volume and test bundles/cross-selling during lower-AOV periods to increase basket size.
5. Improve CustomerID capture to strengthen retention, frequency, and lifetime-value analysis.
6. Collect reliable category and demographic fields if those analyses are required in future.
