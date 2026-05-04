# Excel Dashboard — Professional Guidelines

Apply these standards in Module 4 so `Centrifugal_Pumps_Dashboard.xlsx` is executive-ready.

---

## Structure & layout

- **One Executive Summary** sheet: KPIs + 2–4 charts max—lead with answer, not process.  
- **Dedicated tabs** for each framework or logical group (avoid one overloaded sheet).  
- **Consistent column headers**: clear units (USD, EA), period label in header or title.  
- **Freeze panes** below header row on large tables.

---

## Color coding (cell conventions)

Many teams adopt:

| Meaning | Font / fill |
|---------|----------------|
| **Inputs** (assumptions, slicer selections) | Blue text or labeled “Inputs” section |
| **Formulas** | Default black; avoid hardcoding numbers inside formulas |
| **Links** (other sheets / external) | Green text or note in legend |
| **External / risky** | Red or amber border + note |

Pick **one scheme** and document it on a **Legend** or README tab.

---

## Number formatting

- **Currency:** Accounting format; thousands separator; symbol consistent (USD).  
- **Percentages:** 0–1 decimal unless precision needed; label axis “%”.  
- **Zeros:** Often display **“–”** for readability (use format code or `IF`).  
- **Dates:** Short date + consistent timezone assumption (course data is calendar 2025).

---

## Formula best practices

- **No magic numbers** in formulas—put drivers in an **Assumptions** range and reference cells.  
- Use **`IFERROR`** / **`IFNA`** on lookups to avoid broken dashboards (surface errors in a QA column instead).  
- **Named ranges** for KPI blocks when reused across charts.  
- **One formula row** copied down vs inconsistent manual edits.

---

## Charts

| Purpose | Chart type |
|---------|------------|
| Composition | Stacked column, treemap (few segments) |
| Trend | Line |
| Concentration | Pareto (column + cumulative line) |
| Relationship | Scatter (volume vs price, price vs HP) |

- Chart titles state **what, where, when**.  
- Axis titles include units.  
- Avoid 3D effects for executive packs.

---

## Slicers & filters

- Connect slicers to **all** relevant pivot tables/charts or document exceptions.  
- Group time slicers by month/quarter consistently.  
- Test: change slicer → KPIs and charts update with **no #REF!**.

---

## Validation before sign-off

- [ ] Full calculation mode; no circular refs  
- [ ] Trace dependents from KPI cells  
- [ ] Slicer stress test (extreme filters)  
- [ ] Print/PDF check optional—readable titles and footnotes  

---

## File hygiene

- External links only if intentional; **break links** before sending if required by IT.  
- Remove hidden sheets used for scratch unless labeled “Working”.  
- Final deliverable name: **`Centrifugal_Pumps_Dashboard.xlsx`** in `module-4-dashboards/`.
