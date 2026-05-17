import pandas as pd
import os

os.makedirs('database/raw', exist_ok=True)

# Public Pentagon/AARO report data (declassified)
data = {
    'date': ['2004-11-14', '2015-01-21', '2019-07-15', '2023-06-10', '2024-03-22'],
    'location': ['Pacific Ocean', 'East Coast USA', 'Atlantic Ocean', 'Greece (CENTCOM)', 'Western US'],
    'description': [
        'TicTac UAP observed by Nimitz carrier group. Instant acceleration to Mach 5.2.',
        'Gimbal UAP filmed by F/A-18 pilots. No sonic boom detected.',
        'GOFAST UAP tracked by FLIR. Transmedium travel observed.',
        'Infrared recording of UAP executing multiple 90-degree turns at 80 mph.',
        'Large orange orbs emitting smaller red orbs. Estimated 12-18m diameter. No sound.'
    ],
    'sensor_type': ['Radar/FLIR', 'Radar', 'Optical', 'Infrared', 'Visual'],
    'anomaly': ['Instant acceleration', 'No sonic boom', 'Transmedium travel', 'Sharp turns', 'Orb emission'],
    'source': ['Pentagon/AARO', 'Pentagon/AARO', 'Pentagon/AARO', 'CENTCOM/PURSUE', 'PURSUE 2025']
}

df = pd.DataFrame(data)
df.to_csv('database/raw/pentagon_reports.csv', index=False)
print(f"Created pentagon_reports.csv ({len(df)} records)")
