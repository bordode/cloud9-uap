# 🗃️ Cloud 9 UAP Database
**Open-source UAP dataset from public sources.**

## 📂 Structure
```
database/
├── raw/               # Raw data (Pentagon, MUFON, FAA)
├── processed/         # Cleaned, standardized data
└── scripts/           # Data scraping/cleaning scripts
```

## 📊 Datasets
| File | Source | Columns |
|------|--------|---------|
| `pentagon_reports.csv` | U.S. DoD | `date`, `location`, `description`, `sensor_type`, `anomaly` |
| `uap_flight_data_clean.csv` | MUFON | `velocity_mach`, `acceleration_g`, `sensor_type`, `anomaly` |

## 🔧 How to Use
```bash
python database/scripts/scrape_pentagon.py
python database/scripts/clean_mufon_data.py
python database/scripts/merge_datasets.py
```
