# First-Time Setup — Procurement Mastery with Cursor

Instructions for **course creators** who package this repo and for **students** who consume it.

---

## For course creators

### 1. Folder structure

Ensure the repository contains:

```text
procurement-mastery-course/
├── .cursorrules
├── README.md
├── FIRST_TIME_SETUP.md
├── requirements.txt
├── course_data_generator.py
├── course-data/
├── module-1-data-cleaning/
├── module-2-web-scraping/
├── module-3-spend-analysis/
├── module-4-dashboards/
├── module-5-insights/
└── reference-materials/
```

Empty module folders may contain `.gitkeep` so Git preserves them.

### 2. Install dependencies

```bash
cd procurement-mastery-course
python -m venv .venv
```

**Windows:** `.venv\Scripts\activate`  
**macOS/Linux:** `source .venv/bin/activate`

```bash
pip install -r requirements.txt
```

### 3. Generate training data

```bash
python course_data_generator.py
```

Confirm **`course-data/messy_spend_data.xlsx`** exists.

### 4. Verify readiness

- [ ] `.cursorrules` loads in Cursor (project root open).  
- [ ] `requirements.txt` installs without errors.  
- [ ] Excel file opens; row count ~**1,240** (includes `_CourseBlank` rows); learners target **~1,193** unique clean rows after documented steps.  
- [ ] `reference-materials/` contains the three guides.

### 5. Start the course in Cursor

1. Open the **`procurement-mastery-course`** folder in Cursor.  
2. Ensure `.cursorrules` is present (Cursor picks up project rules).  
3. Open Chat and type: **`I'm ready to start the Procurement Mastery Course`**  
4. Follow Module **0** orientation, then **`Start Module 1`** when prompted.

---

## For students

### 1. Get the course folder

Download/unzip the package or clone the repo into a path **without** special permission issues (avoid synced folders that lock Excel if possible).

### 2. Open a terminal in the course folder

**Windows:** Right-click folder → Open in Terminal, or `cd` to the path.

### 3. Install Python dependencies

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

(On Mac/Linux use `source .venv/bin/activate`.)

### 4. Generate messy data

```bash
python course_data_generator.py
```

### 5. Open in Cursor

**File → Open Folder** → select **`procurement-mastery-course`**.

### 6. Start the instructor

In Cursor Chat, type exactly:

**`I'm ready to start the Procurement Mastery Course`**

Then follow steps until you type **`Start Module 1`** after orientation.

---

## Troubleshooting

| Issue | What to try |
|-------|--------------|
| `pip` fails | Use `python -m pip install -r requirements.txt` |
| Missing Excel file | Re-run `course_data_generator.py`; check `course-data/` exists |
| Cursor ignores rules | Confirm `.cursorrules` is in the **root** you opened |
| Locked Excel | Close workbook before regenerating data |

---

## Next steps

Read **`README.md`** for the scenario overview and module map. Keep deliverables in the **module-* folders** as you progress.
