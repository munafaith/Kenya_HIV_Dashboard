# Kenya HIV/TB Program Dashboard

## Overview
An interactive Power BI dashboard analyzing Kenya's HIV/TB program
performance using real PEPFAR MER (Monitoring, Evaluation and Reporting) 
data from 2020–2025.

Built as a portfolio project demonstrating end-to-end data analysis skills — 
from raw data download and Python cleaning through to Power BI dashboard 
development — targeting public health data analyst roles.

## Tools Used
- **Python (Pandas)** — data cleaning and preparation
- **Power BI Desktop** — dashboard development and visualization
- **Data Source** — PEPFAR Public Partner MER TopLine Dataset  
  (https://data.pepfar.gov/datasets)

## Data Cleaning Steps
The raw dataset contained 102,948 rows of global PEPFAR program data.  
Using Python and Pandas, the data was cleaned down to 957 Kenya-specific rows:

- Filtered to Kenya only
- Selected 5 key HIV/TB indicators: HTS_TST, HTS_TST_POS, TX_CURR, TB_STAT, TB_ART
- Removed denominator rows to avoid double-counting
- Kept only Total Numerator rows for clean aggregates
- Converted mixed-type numeric columns using pd.to_numeric()
- Engineered Annual_Total column by summing Q1+Q2+Q3+Q4
- Filtered to fiscal years 2020–2025

## Dashboard Visuals

| Visual | Type | What It Shows |
|---|---|---|
| Program KPIs | 4 Cards | Overall scale — tests, positives, ART, TB |
| Top Partners | Bar Chart | Implementing partner performance in 2024 |
| Testing Trend | Line Chart | HTS_TST and HTS_TST_POS trend 2020–2025 |
| Funding Breakdown | Stacked Bar | USAID vs HHS/CDC vs DOD ART coverage by year |

## Key Findings
- 25 million HIV tests conducted in Kenya through PEPFAR-supported 
  partners between 2020 and 2025
- 542,000 HIV positive cases identified, reflecting approximately 
  2% positivity rate across the testing period
- HHS/CDC is the dominant funder of ART coverage in Kenya, 
  consistently contributing the larger share across all years
- HIV testing peaked in 2024 — 2025 figures are partial as the 
  dataset was published early in the year

## Data Limitations
- Partner-level data excludes manual deduplication adjustments 
  made by PEPFAR staff at facility level
- 2025 figures are incomplete as the dataset was published early 2025
- Data represents PEPFAR-supported sites only, not all health 
  facilities in Kenya

## Files in This Repository
| File | Description |
|---|---|
| `clean_hiv_data.py` | Python script for data cleaning |
| `kenya_hiv_cleaned.csv` | Cleaned dataset (957 rows) |
| `Kenya_HIV_Dashboard.pbix` | Power BI dashboard file |

## How to Use
1. Download the raw data from https://data.pepfar.gov/datasets  
   (Public Partner MER TopLine.zip)
2. Run `clean_hiv_data.py` to reproduce the cleaned dataset
3. Open `Kenya_HIV_Dashboard.pbix` in Power BI Desktop to explore 
   the dashboard

## Author
Faith Wairimu Muna  
github.com/munafaith