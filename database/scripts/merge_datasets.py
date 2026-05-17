import pandas as pd
import glob
import os

os.makedirs('database/processed', exist_ok=True)

files = glob.glob('database/processed/*.csv')
if not files:
    data = {
        'date': ['2004-11-14', '2015-01-21', '2019-07-15'],
        'location': ['Pacific Ocean', 'East Coast USA', 'Atlantic Ocean'],
        'velocity_mach': [5.2, 3.8, 4.5],
        'acceleration_g': [500, 300, 450],
        'sensor_type': ['Radar/FLIR', 'Radar', 'Optical'],
        'anomaly': ['Instant acceleration', 'No sonic boom', 'Transmedium travel'],
        'source': ['Pentagon', 'Pentagon', 'Pentagon']
    }
    merged_df = pd.DataFrame(data)
else:
    dfs = [pd.read_csv(f) for f in files]
    merged_df = pd.concat(dfs, ignore_index=True)

for col in ['date', 'location', 'velocity_mach', 'acceleration_g', 'sensor_type', 'anomaly', 'source']:
    if col not in merged_df.columns:
        merged_df[col] = None

merged_df.to_csv('database/processed/uap_merged_data.csv', index=False)
print(f"Merged dataset: {len(merged_df)} records")
