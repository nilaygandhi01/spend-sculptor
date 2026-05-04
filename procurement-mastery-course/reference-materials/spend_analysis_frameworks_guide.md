# Spend Analysis Frameworks — Reference Guide

Use this guide when building Module 3 analyses. Each framework answers a different procurement question; together they form a complete category story.

---

## 1. Spend profiling

**What it reveals**  
Where money goes by **dimension**: supplier, site/region, material/spec cluster, spend type (Opex/Capex), and **time** (month/quarter).

**Data required**  
Clean rows with **Spend** (or PO value), **Date**, **Vendor / Vendor Clean**, **Site or Country**, **Classification**, optional **Material #**.

**Typical outputs**  
- Pivot tables or summaries: Spend by supplier, by region, by month  
- Waterfall or stacked column chart: composition of spend  
- Pareto prep (often paired with fragmentation)

**Example insights**  
- “Top 5 suppliers = 72% of centrifugal spend.”  
- “Americas grew 18% YoY vs flat EMEA.”

**Excel patterns**  
`SUMIFS`, pivot tables, timeline slicers. Charts: stacked columns, treemap (if few segments).

---

## 2. Supplier fragmentation

**What it reveals**  
Whether spend is **concentrated** among few suppliers or **fragmented** across many—tail spend risk, negotiation leverage, and rationalization candidates.

**Data required**  
Vendor identifier (cleaned), Spend.

**Typical outputs**  
- Pareto chart (cumulative % spend)  
- Metrics: **CR3/CR5** (share of top 3 / 5 suppliers), count of suppliers above threshold  
- Tail list: suppliers below $X or Y% cumulative

**Example insights**  
- “47 suppliers under $50k each—prime tail consolidation.”  
- “Top 2 OEMs are 55%; remainder long tail.”

**Excel patterns**  
Sorted spend column, running total %, combo chart (bars + cumulative line).

---

## 3. Spend commonality

**What it reveals**  
**Similar buys** across locations or plants—standardization, bulk negotiation, or BOM cleanup opportunities.

**Data required**  
Material ID or **normalized description**, Site/Country, Spend, Qty.

**Typical outputs**  
- Matrix: material cluster × region → spend or count  
- Duplicate buys: same normalized material across **3+** sites with different prices or vendors

**Example insights**  
- “SS316 15HP ANSI bought in 8 sites with 6 different prices.”  
- “Common motor frame sizes purchased as custom in two regions.”

**Excel patterns**  
Text normalization helper column, `COUNTIFS` / pivots; cluster tags via keywords (HP, material grade).

---

## 4. Price arbitrage

**What it reveals**  
Same or **similar item**, **different unit prices** across vendors, sites, or time—**margin reset** and negotiation targets.

**Data required**  
Comparable item key (material # or normalized description + key specs), **Price per item** or unit spend, Vendor, Site.

**Typical outputs**  
- Price dispersion: min/median/max by cluster  
- Gap vs median or vs best observed price × volume → **addressable savings**

**Example insights**  
- “Duplex 25HP: Site A pays 22% above cluster median.”  
- “Same OEM SKU: two subsidiaries differ by 14%.”

**Excel patterns**  
Median by cluster (`AGGREGATE`, pivot median), conditional formatting on % vs median.

---

## 5. Price index correlation

**What it reveals**  
Whether paid prices **track** external indices (commodity, FX, industry PPI) or drift—**market alignment** and timing of contracts.

**Data required**  
Time series of spend or unit price; external index series (Module 2 scrape or public CSV); optional FX.

**Typical outputs**  
- Indexed chart: internal unit price vs index (rebased to 100)  
- Correlation coefficient or qualitative alignment pre/post negotiation

**Example insights**  
- “Unit prices flat while nickel proxy up 12%—good containment.”  
- “JPY sites diverge from FX—contract currency risk.”

**Excel patterns**  
`CORREL`, scatter with trendline; dual-axis line chart with aligned periods.

---

## 6. Volume–price relationship

**What it reveals**  
Whether larger **quantities** earn better **unit pricing**—leverage health and bundling opportunities.

**Data required**  
Qty, Price per item (or Spend/Qty), cluster key (supplier + material family).

**Typical outputs**  
- Scatter: Qty vs unit price with trendline  
- Bucket analysis (bands of Qty) with median price per band

**Example insights**  
- “No discount slope above 10 units—negotiate tier breaks.”  
- “Regional DC could consolidate 4 POs into one release.”

**Excel patterns**  
Bins (`ROUNDUP`/`FLOOR`), pivot by bucket; scatter + trendline.

---

## 7. Linear performance pricing

**What it reveals**  
Whether price aligns with **technical drivers** (HP, GPM, material tier)—fairness vs **spec creep** or mis-pricing.

**Data required**  
Numeric specs (HP, GPM, mass), material tier, **Price in USD** or unit price, ideally homogeneous family (centrifugal).

**Typical outputs**  
- Regression-style scatter: e.g., Price vs HP (by supplier or region)  
- Residuals: **over/under** vs fitted expectation → outliers for sourcing review

**Example insights**  
- “Premium vs ‘fair’ line: same HP band pays 19% more at Vendor X.”  
- “Hastelloy uplift ~1.4x vs SS316—consistent with market.”

**Excel patterns**  
`LINEST`, scatter + trendline; residual column = Actual − Predicted (from simple model).

---

## Combining frameworks

| Stage | Frameworks |
|-------|------------|
| Baseline story | 1, 2 |
| Cross-site savings | 3, 4 |
| Market & leverage | 5, 6 |
| Technical fairness | 7 |

Deliver **one insight paragraph per framework** minimum—quantified where possible.
