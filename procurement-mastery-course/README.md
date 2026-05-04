# Procurement Spend Analysis - Cursor AI Course

## Quick description

A **15–30 minute** hands-on course that teaches **McKinsey-style procurement analysis** in **Cursor AI**. You learn by building real deliverables: clean a messy dataset, run **three** spend frameworks, build an **Excel dashboard**, and produce a **short recommendations deck**—not by reading long manuals.

## What you'll build

- **Clean procurement dataset** — 1,193 clean transactions, ~$16.5M spend (after fixing messy source data)
- **Spend analysis** using **3 frameworks** — spend profiling, supplier fragmentation, price arbitrage
- **Interactive Excel dashboard** — KPIs, charts, slicers
- **4-slide recommendations** — `recommendations.pptx` for a CPO-style readout

## Quick start

### Installation (3 steps)

1. **Clone** this repository.
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Open the folder in Cursor** (File → Open Folder).

### How to start the course (2 steps)

1. Open **Cursor chat** (Ctrl+L on Windows, Cmd+L on Mac).
2. Type: **`Start procurement course`**

That is it. The **fast-track** AI instructor (rule: `procurement-fast-track`) guides the next steps. If you use the full multi-module path instead, see `.cursorrules` in the repo.

**Data:** From the project root, run `python fast_track_data_generator.py` to create `course-data/messy_spend_data.xlsx` if you need a fresh file.

## What happens next

**3 modules** in about **15–30 minutes:**

1. **Clean messy data** (~8 min)
2. **Analyze spend** (~12 min)
3. **Create deliverables** — dashboard + deck (~10 min)

## Requirements

- **Cursor IDE**
- **Python 3.8+**
- **About 15–30 minutes**

Optional: Microsoft Excel for formulas/charts; **python-pptx** is listed in `requirements.txt` if you generate slides from Python.

## Repo contents (short)

| Item | Role |
|------|------|
| `.cursor/rules/procurement-fast-track.mdc` | Fast-track instructor behavior |
| `.cursorrules` | Longer “Procurement Mastery” course (optional) |
| `fast_track_data_generator.py` | Builds messy training data |
| `course_data_generator.py` | Alternate full-course data generator |
| `course-data/` | Messy Excel input after you run a generator |
| `FIRST_TIME_SETUP.md` | Extra setup notes |

## License / use

Synthetic GDH-style data only—safe for training. Replace with your own client data under your firm’s rules.
