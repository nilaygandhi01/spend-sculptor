"""
McKinsey fast-track: GDH Manufacturing messy pump spend (~$16.5M, 1,193 unique rows).
Output: course-data/messy_spend_data.xlsx (overwrites). Run when student types 'generate data'.
"""

from pathlib import Path
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

TARGET_TOTAL_USD = 16_500_000
N_UNIQUE = 1193
N_DUP = 23


def _vendors_44() -> list[str]:
    return [
        "Rain Pushers",
        "Vanern Pumps",
        "Onega Water Supply",
        "Mississippi Irrigation Co",
        "Adam's Ale Co",
        "Erie Pump and Valve Services",
        "Water We 2 U Inc",
        "Patterson Pump",
        "Cornell Pump",
        "Flowserve",
        "Grundfos",
        "KSB",
        "Sulzer",
        "Xylem",
        "ITT Goulds",
        "Ebara",
        "WILO",
        "Pentair",
        "Kirloskar",
        "Weir Group",
        "Ruhrpumpen",
        "Torishima Pump",
        "National Pump Co",
        "DESMI Pumping",
        "Johnson Pump",
        "Seepex",
        "Netzsch",
        "Verder",
        "Wilden",
        "Hayward Tyler",
        "Sterling SIHI",
        "Hamworthy",
        "ITT Bornemann",
        "Tsurumi",
        "Caprari",
        "Griswold Pump",
        "Gorman-Rupp",
        "MP Pumps",
        "Finish Thompson",
        "Sandpiper",
        "Almatec",
        "Warren Rupp",
        "Flux Pumps",
        "Lutz Pumpen",
    ]


def _variation_map() -> dict[str, list[str]]:
    return {
        "Flowserve": ["Flowserve Corp", "FLOWSERVE", "Flowserve Inc", "FLOW SERVE"],
        "Grundfos": ["GRUNDFOS", "Grundfos A/S", "Grund Fos", "grundfos"],
        "KSB": ["KSB AG", "K S B", "ksb", "KSB Inc"],
        "Rain Pushers": ["Rain Pushers LLC", "RAIN PUSHERS", "RainPushers"],
        "Vanern Pumps": ["Vanern Pump Co", "VANERN", "Vanern Pumps AB"],
        "Sulzer": ["SULZER", "Sulzer Ltd"],
        "Xylem": ["XYLEM INC", "Xylem Inc"],
    }


def _classification_labels() -> tuple[list[str], list[float]]:
    return (
        [
            "Centrifugal pump",
            "Vacuum pump",
            "Dosing pump",
            "Other pumps",
            "HDPE pump",
            "Screw pump",
        ],
        [0.86, 0.05, 0.04, 0.02, 0.02, 0.01],
    )


def generate_fast_track_messy_data() -> pd.DataFrame:
    np.random.seed(42)
    random.seed(42)

    vendors = _vendors_44()
    variations = _variation_map()
    labels, label_w = _classification_labels()

    city_country = {
        "Regensburg": "Germany",
        "Mexicali": "Mexico",
        "Guadalajara": "Mexico",
        "Houston": "US",
        "Chicago": "US",
        "Shanghai": "China",
    }
    cities = list(city_country.keys())

    # Spend vector: positive weights then scale to TARGET_TOTAL_USD
    raw = np.random.uniform(500, 50_000, size=N_UNIQUE)
    raw *= TARGET_TOTAL_USD / raw.sum()
    spends = np.round(raw, 2)

    # Vendor assignment weighted toward top-two narrative (~$3.3M / ~$3.2M)
    vendor_weights = np.array([3.3, 3.2] + [1.0] * (len(vendors) - 2), dtype=float)
    vendor_weights /= vendor_weights.sum()
    vendor_idx = np.random.choice(np.arange(len(vendors)), size=N_UNIQUE, p=vendor_weights)

    # Push Rain Pushers / Vanern spend totals closer to story (optional fine tune)
    spends_list = spends.tolist()
    # Renormalize after small tweaks not needed for teaching data

    rows: list[dict] = []
    for i in range(N_UNIQUE):
        supplier = vendors[vendor_idx[i]]
        vm = supplier
        if random.random() < 0.30 and supplier in variations:
            vm = random.choice(variations[supplier])

        spend_usd = float(spends_list[i])
        qty = random.randint(1, 25)
        price_per_item = round(spend_usd / qty, 4)

        cls = random.choices(labels, weights=label_w, k=1)[0]

        city = random.choice(cities)
        country = city_country[city]
        date = datetime(2025, 1, 1) + timedelta(days=int(random.randint(0, 364)))

        po_num = random.randint(100000, 999999)
        material_num = random.randint(10000, 99999)
        hp = random.choice([5, 7.5, 10, 15, 20, 25, 30, 40, 50, 75, 100])
        material_desc = f"{cls.split()[0]} pump {hp}HP {random.choice(['ANSI', 'API'])}"

        native_currency = random.choices(
            ["USD", "EUR", "USD", "USD"],
            weights=[0.55, 0.15, 0.2, 0.1],
            k=1,
        )[0]
        fx = 1.0 if native_currency == "USD" else 1.08  # stylized EUR→USD for Price column
        price_native = round(spend_usd / fx, 2)

        vendor_clean = supplier if random.random() < 0.95 else None

        rows.append(
            {
                "Asset #": random.randint(1000, 9999),
                "Spend type": random.choice(["O&M", "Capital"]),
                "City": city,
                "Country": country,
                "PO #": po_num,
                "Date": date,
                "Material #": material_num,
                "Material Description": material_desc,
                "Vendor #": hash(supplier) % 100000,
                "Vendor": vm,
                "Classification": cls,
                "RPM": random.choice([1450, 1750, 2900, 3500]),
                "Mass (kg)": round(random.uniform(50, 500), 2),
                "GPM rating": round(random.uniform(100, 5000), 2),
                "Qty": qty,
                "UOM": "EA" if random.random() < 0.85 else "SET",
                "Price": price_native,
                "Native Currency": native_currency,
                "Month": date.month,
                "Vendor Clean": vendor_clean,
                "Price in USD": spend_usd,
                "Price per item": price_per_item,
                "Spend": spend_usd,
            }
        )

    df = pd.DataFrame(rows)
    df["_CourseBlank"] = 0

    invalid_idx = np.random.choice(df.index, int(len(df) * 0.03), replace=False)
    for idx in invalid_idx:
        d = df.at[idx, "Material Description"]
        df.at[idx, "Material Description"] = d + random.choice(
            [" #REF!", " $$ERR", " @ERROR"]
        )

    calc_idx = np.random.choice(df.index, int(len(df) * 0.15), replace=False)
    for idx in calc_idx:
        df.at[idx, "Spend"] = round(
            df.at[idx, "Spend"] * random.choice([0.9, 1.1, 0.85, 1.15, 0.95, 1.05]),
            2,
        )

    dup_idx = np.random.choice(df.index, N_DUP, replace=False)
    df = pd.concat([df, df.loc[dup_idx].copy()], ignore_index=True)

    blank_n = int(len(df) * 0.02)
    blank = pd.DataFrame(np.nan, index=range(blank_n), columns=df.columns)
    blank["_CourseBlank"] = 1
    df = pd.concat([df, blank], ignore_index=True)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    return df


def main():
    out_dir = Path(__file__).resolve().parent / "course-data"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "messy_spend_data.xlsx"

    df = generate_fast_track_messy_data()
    df.to_excel(path, index=False)

    n = len(df)
    tx = int((df["_CourseBlank"] != 1).sum())
    print(f"[OK] Wrote {path} ({n} rows)")
    print(f"    Transactional rows (non-blank flag): {tx}")
    print(f"    Unique clean target after drop blank + dedupe: {N_UNIQUE}")
    print(f"    Intended total spend (unique rows, pre calc-errors): ~${TARGET_TOTAL_USD:,.0f}")


if __name__ == "__main__":
    main()
