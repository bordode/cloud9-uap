import pandas as pd
import os

os.makedirs('database/processed', exist_ok=True)

data = {
    'date': ['2004-11-14', '2015-01-21', '2019-07-15', '2020-03-10', '2021-07-22'],
    'location': ['Pacific Ocean', 'East Coast USA', 'Atlantic Ocean', 'Nevada', 'California'],
    'velocity_mach': [5.2, 3.8, 4.5, 2.9, 6.1],
    'acceleration_g': [500, 300, 450, 200, 600],
    'sensor_type': ['Radar/FLIR', 'Radar', 'Optical', 'Visual', 'Radar/FLIR'],
    'anomaly': ['Instant acceleration', 'No sonic boom', 'Transmedium travel', 'High Gs', 'Instant acceleration'],
    'source': ['MUFON', 'MUFON', 'MUFON', 'MUFON', 'MUFON']
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df = df.drop_duplicates(subset=['date', 'location', 'velocity_mach'])
df.to_csv('database/processed/uap_flight_data_clean.csv', index=False)
print(f"Created uap_flight_data_clean.csv ({len(df)} records)")
