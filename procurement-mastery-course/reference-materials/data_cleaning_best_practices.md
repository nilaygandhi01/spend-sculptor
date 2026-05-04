# Data Cleaning — Best Practices (Procurement Spend)

Professional cleaning is **repeatable**, **documented**, and **validated**. Use this in Module 1.

---

## Common data quality issues

| Issue | Symptoms |
|-------|-----------|
| Duplicates | Same PO/line/material/vendor/date repeated |
| Inconsistent entities | “Grundfos A/S” vs “GRUNDFOS” |
| Missing keys | Blank vendor, material, or site |
| Text corruption | `#REF!`, `$$ERR`, stray encoding |
| Unit / logic errors | Spend ≠ Qty × unit price; mixed UOM |
| Structural junk | Fully blank rows, Excel export artifacts (`_CourseBlank` flags) |

---

## Cleaning strategies

1. **Profile first** — Row count, null rates, distinct counts for Vendor, Material #, duplicate keys.  
2. **Define rules** — Order matters: often **drop structural blanks → dedupe → normalize text → impute keys → recalculate metrics**.  
3. **Golden keys** — Decide duplicate key (e.g., PO + Material # + Date + Vendor + Qty) or statistical fuzzy dedupe for messy exports.  
4. **Normalization** — Vendor mapping table (messy → canonical); trim; upper/lower policy; strip punctuation.  
5. **Derived fields** — `Price per item` = `Spend / Qty` or from native currency consistently; single source of truth for USD.  
6. **Audit trail** — Keep original columns or `_raw` where useful; log dropped row counts.

---

## Python (pandas) techniques

- `df.info()`, `df.describe()`, `df.isna().mean()` for profile  
- `df.dropna(how="all")` for empty rows  
- `df.duplicated(subset=[...], keep=False)` to inspect duplicate clusters  
- `df.drop_duplicates(subset=[...])` once keys are defined  
- String: `str.strip()`, `str.upper()`, `replace` with mapping dict  
- Safe math: `np.where` / `round` after float fixes; watch divide-by-zero on Qty  

**Course file note:** If `_CourseBlank == 1`, drop those rows before analysis (or exclude from row-count KPIs).

---

## Validation approaches

- **Reconciliation:** Sum of line Spend vs recomputed `Qty * Price per item` within tolerance (rounding).  
- **Bounds:** Negative spend, zero qty with positive spend, dates outside fiscal window.  
- **Cross-check:** Distinct vendor count before/after mapping; top suppliers stable unless intended.  
- **Spot audit:** 10 random rows traced to raw export.

---

## Documentation requirements

Produce a short **cleaning spec** (Module 1.2) that includes:

1. Source file and generation assumptions  
2. Each transformation with **why**  
3. Row counts: raw → after each major step  
4. Outstanding limitations (e.g., FX rate frozen; scraping not applied yet)

Store **`verification_report`** with before/after metrics and sample exceptions list.

---

## Professional habits

- Version your script (`cleaning_script.py`) and output filename with date if iterating  
- Never overwrite raw extract—keep **`messy_spend_data.xlsx`** pristine in `course-data/`  
- Write for an auditor: could someone else reproduce your numbers from the spec?
