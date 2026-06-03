import pandas as pd

# --- LOAD DATA ---
df = pd.read_csv("mer_data.csv", encoding="latin1")

print("Original shape:", df.shape)
print("Columns:", df.columns.tolist())

# --- FILTER TO KENYA ONLY ---
kenya = df[df["Country"] == "Kenya"].copy()
print("Kenya rows:", len(kenya))

# --- KEEP ONLY RELEVANT INDICATORS ---
indicators_we_need = ["HTS_TST", "HTS_TST_POS", "TX_CURR", "TB_STAT", "TB_ART"]
kenya = kenya[kenya["Indicator"].isin(indicators_we_need)]

# --- KEEP ONLY NUMERATORS (actual results, not denominators) ---
kenya = kenya[kenya["Numerator/Denominator"] == "N"]

# --- KEEP ONLY TOTAL NUMERATOR ROWS (not age/sex breakdowns) ---
kenya = kenya[kenya["Standardized Disaggregate"] == "Total Numerator"]

# --- SELECT USEFUL COLUMNS ---
kenya = kenya[[
    "Country", "Funding Agency", "Mechanism Name",
    "Indicator", "Fiscal Year",
    "Targets", "Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"
]].copy()

# --- CLEAN COLUMN NAMES ---
kenya.columns = [
    "Country", "Funding_Agency", "Partner",
    "Indicator", "Fiscal_Year",
    "Targets", "Q1", "Q2", "Q3", "Q4"
]

# --- CONVERT NUMERIC COLUMNS ---
for col in ["Targets", "Q1", "Q2", "Q3", "Q4"]:
    kenya[col] = pd.to_numeric(kenya[col], errors="coerce")

# --- ADD ANNUAL TOTAL COLUMN ---
kenya["Annual_Total"] = kenya[["Q1", "Q2", "Q3", "Q4"]].sum(axis=1, skipna=True)

# --- FILTER TO RECENT YEARS ---
kenya = kenya[kenya["Fiscal_Year"] >= 2020]

# --- SORT ---
kenya = kenya.sort_values(["Indicator", "Fiscal_Year", "Partner"])

# --- CHECK RESULTS ---
print("\nCleaned data shape:", kenya.shape)
print("\nIndicators included:")
print(kenya["Indicator"].value_counts())
print("\nYears included:")
print(kenya["Fiscal_Year"].value_counts().sort_index())
print("\nPreview:")
print(kenya.head(10))

# --- SAVE ---
kenya.to_csv("kenya_hiv_cleaned.csv", index=False)
print("\nDone! Saved as kenya_hiv_cleaned.csv")