"""
Procurement Mastery Course - Data Generator
Generates messy centrifugal pump spend data for Module 1 (saved to course-data/).
"""

from pathlib import Path
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def generate_messy_spend_data():
    """Generate messy GDH-style centrifugal pump spend data."""

    np.random.seed(42)
    random.seed(42)

    suppliers_clean = [
        "FLOWSERVE CORPORATION",
        "GRUNDFOS",
        "KSB AG",
        "SULZER LTD",
        "XYLEM INC",
        "ITT GOULDS PUMPS",
        "EBARA CORPORATION",
        "WILO SE",
        "PENTAIR",
        "KIRLOSKAR BROTHERS",
        "THE WEIR GROUP",
        "RUHRPUMPEN",
        "PATTERSON PUMP COMPANY",
        "CORNELL PUMP COMPANY",
        "TORISHIMA PUMP",
    ]

    vendor_variations = {
        "FLOWSERVE CORPORATION": [
            "Flowserve Corp",
            "FLOWSERVE",
            "Flowserve Corp.",
            "Flow Serve Corporation",
            "Flowserve  Corp",
            "flowserve",
        ],
        "GRUNDFOS": [
            "GRUNDFOS",
            "Grundfos A/S",
            "Grundfos Inc",
            "Grund Fos",
            "GRUND FOS",
            "grundfos inc.",
        ],
        "KSB AG": ["KSB", "K S B AG", "KSB Inc", "ksb ag", "K.S.B. AG", "KSB  AG"],
        "XYLEM INC": [
            "Xylem",
            "XYLEM INC",
            "Xylem Inc.",
            "Xylem Incorporated",
            "XYLEM  INC",
            "xylem",
        ],
        "SULZER LTD": [
            "Sulzer",
            "SULZER LTD",
            "Sulzer Ltd.",
            "SULZER  LTD",
            "sulzer ltd",
        ],
        "ITT GOULDS PUMPS": [
            "ITT Goulds",
            "GOULDS PUMPS",
            "ITT  Goulds Pumps",
            "itt goulds",
            "Goulds",
        ],
        "PENTAIR": [
            "Pentair",
            "PENTAIR",
            "Pentair Inc",
            "PENTAIR  INC",
            "pentair inc.",
        ],
    }

    cities = [
        "Houston",
        "Chicago",
        "Los Angeles",
        "Regensburg",
        "Shanghai",
        "Tokyo",
        "Singapore",
        "Dubai",
        "Sydney",
        "Toronto",
        "Mexicali",
        "Guadalajara",
        "Mumbai",
        "Rotterdam",
        "Aberdeen",
    ]

    city_country = {
        "Houston": "USA",
        "Chicago": "USA",
        "Los Angeles": "USA",
        "Regensburg": "Germany",
        "Shanghai": "China",
        "Tokyo": "Japan",
        "Singapore": "Singapore",
        "Dubai": "UAE",
        "Sydney": "Australia",
        "Toronto": "Canada",
        "Mexicali": "Mexico",
        "Guadalajara": "Mexico",
        "Mumbai": "India",
        "Rotterdam": "Netherlands",
        "Aberdeen": "UK",
    }

    classifications = [
        "Centrifugal - Single Stage",
        "Centrifugal - Multistage",
        "Centrifugal - Axial Flow",
        "Centrifugal - Mixed Flow",
        "Positive Displacement",
        "Specialty Pumps",
    ]

    n_unique = 1193
    data_rows = []

    currency_probs = {"USD": 0.4, "EUR": 0.2, "GBP": 0.1, "JPY": 0.15, "CNY": 0.15}
    exchange_to_usd = {"USD": 1.0, "EUR": 1.18, "GBP": 1.37, "JPY": 0.0091, "CNY": 0.16}

    for _ in range(n_unique):
        asset_num = random.randint(1000, 9999)
        spend_type = random.choice(["O&M", "Capital"]) if random.random() < 0.7 else "Capital"
        city = random.choice(cities)
        country = city_country[city]
        po_num = random.randint(100000, 999999)

        date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 364))
        month = date.month

        material_num = random.randint(10000, 99999)
        materials = ["SS316", "CI", "Bronze", "Duplex", "Hastelloy"]
        hp = random.choice([1, 2, 3, 5, 7.5, 10, 15, 20, 25, 30, 40, 50, 75, 100])
        material_desc = (
            f"Centrifugal Pump {random.choice(materials)} {hp}HP "
            f'{random.choice(["ANSI", "API", "ISO"])}'
        )

        supplier = random.choice(suppliers_clean)
        vendor_num = hash(supplier) % 100000

        if random.random() < 0.3 and supplier in vendor_variations:
            vendor_messy = random.choice(vendor_variations[supplier])
        else:
            vendor_messy = supplier

        if random.random() < 0.8:
            classification = random.choice(classifications[:4])
        else:
            classification = random.choice(classifications[4:])

        rpm = random.choice([1450, 1750, 2900, 3500])
        mass_kg = round(random.uniform(50, 500), 2)
        gpm_rating = round(random.uniform(100, 5000), 2)

        qty = random.randint(1, 25)
        uom = "EA" if random.random() < 0.8 else "SET"

        native_currency = random.choices(
            list(currency_probs.keys()), weights=list(currency_probs.values())
        )[0]

        # Target USD-equivalent line spend $500 - $50,000 (spec); derive native Price from USD
        price_usd = round(random.uniform(500, 50000), 2)
        rate = exchange_to_usd[native_currency]
        price_native = round(price_usd / rate, 4 if native_currency != "JPY" else 2)
        price_per_item = round(price_usd / qty, 4)
        spend = price_usd

        vendor_clean = supplier if random.random() < 0.95 else None

        row = {
            "Asset #": asset_num,
            "Spend type": spend_type,
            "City": city,
            "Country": country,
            "PO #": po_num,
            "Date": date,
            "Material #": material_num,
            "Material Description": material_desc,
            "Vendor #": vendor_num,
            "Vendor": vendor_messy,
            "Classification": classification,
            "RPM": rpm,
            "Mass (kg)": mass_kg,
            "GPM rating": gpm_rating,
            "Qty": qty,
            "UOM": uom,
            "Price": price_native,
            "Native Currency": native_currency,
            "Month": month,
            "Vendor Clean": vendor_clean,
            "Price in USD": price_usd,
            "Price per item": price_per_item,
            "Spend": spend,
        }

        data_rows.append(row)

    df = pd.DataFrame(data_rows)
    df["_CourseBlank"] = 0

    invalid_indices = np.random.choice(df.index, int(len(df) * 0.03), replace=False)
    for idx in invalid_indices:
        desc = df.at[idx, "Material Description"]
        df.at[idx, "Material Description"] = desc + random.choice(
            [" #REF!", " $$ERR", " @ERROR", " //INVALID"]
        )
    print(f"[OK] Added invalid characters to ~{len(invalid_indices)} material descriptions")

    calc_indices = np.random.choice(df.index, int(len(df) * 0.15), replace=False)
    for idx in calc_indices:
        df.at[idx, "Spend"] = round(
            df.at[idx, "Spend"] * random.choice([0.9, 1.1, 0.85, 1.15, 0.95, 1.05]), 2
        )
    print(f"[OK] Introduced calculation errors in ~{len(calc_indices)} rows")

    duplicate_indices = np.random.choice(df.index, 23, replace=False)
    duplicates = df.loc[duplicate_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    print(f"[OK] Added 23 duplicate rows (now {len(df)} total)")

    blank_count = int(len(df) * 0.02)
    blank_rows = pd.DataFrame(np.nan, index=range(blank_count), columns=df.columns)
    blank_rows["_CourseBlank"] = 1
    df = pd.concat([df, blank_rows], ignore_index=True)
    print(f"[OK] Appended {blank_count} blank rows (~2%), flagged in column _CourseBlank")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    print(f"\n[OK] Generated messy dataset: {len(df)} rows")
    print(f"  - Expected clean rows after removing blanks & duplicates: {n_unique}")
    print(f"  - Vendor name variations (approx): ~{int(n_unique * 0.3)}")
    print(f"  - Missing 'Vendor Clean' (approx): ~{int(n_unique * 0.05)}")
    print(f"  - Blank rows (flagged): {blank_count}")

    return df


def main():
    print("=" * 60)
    print("PROCUREMENT MASTERY COURSE - DATA GENERATOR")
    print("=" * 60)
    print()

    out_dir = Path(__file__).resolve().parent / "course-data"
    out_dir.mkdir(parents=True, exist_ok=True)
    output_file = out_dir / "messy_spend_data.xlsx"

    print("Generating messy spend data with intentional quality issues...")
    print()

    df_messy = generate_messy_spend_data()
    df_messy.to_excel(output_file, index=False)

    print()
    print("=" * 60)
    print(f"[OK] COMPLETE: {output_file}")
    print("=" * 60)
    print()
    print("Use this file in Module 1 (course-data/messy_spend_data.xlsx).")
    print()
    print("Embedded issues:")
    print("  1. Duplicate records (23)")
    print("  2. Inconsistent vendor naming (~30% where variation map applies)")
    print("  3. Missing 'Vendor Clean' (~5%)")
    print("  4. Invalid tokens in Material Description (~3%)")
    print("  5. Spend != Qty * Price per item (~15%, intentional)")
    print("  6. Synthetic blank rows (~2%), column _CourseBlank=1")
    print()
    print("Expected clean unique rows: 1,193 after drops + dedupe (per design).")


if __name__ == "__main__":
    main()
