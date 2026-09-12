# Findings

## Dataset and cleaning
- Original transaction lines: **541,909**.
- Exact duplicate rows identified after loading the supplied project CSV: **0** (the CSV contains a unique `index` field, so exact-row duplicates are not detected here).
- Cancelled invoices, non-positive quantities/prices and invalid dates were excluded from sales-performance analysis.
- Clean sales transaction lines: **530,104**.
- CustomerID is missing for **132,220** cleaned transaction lines.
- The dataset does **not** contain age or gender fields, so age-group and gender analysis is not fabricated.

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

## Product category limitation
- The supplied dataset contains **no dedicated product-category field**. Revenue by category cannot be calculated reliably without inventing categories, so category analysis is intentionally omitted.

## Age/gender limitation
- The supplied dataset contains **no age or gender variables**. Demographic analysis by age or gender is therefore not supported by the available data and is intentionally omitted.

## Actionable recommendations
1. Plan inventory, staffing, and campaigns around peak periods.
2. Protect high-volume products while separately monitoring high-revenue products.
3. Prioritise the UK market while selectively testing international growth.
4. Improve CustomerID capture to strengthen retention, frequency, and lifetime-value analysis.
5. Collect reliable category and demographic fields if those analyses are required in future.
