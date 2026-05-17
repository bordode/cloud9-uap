import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Cloud 9 UAP Dashboard", page_icon="🛸", layout="wide")

try:
    data = pd.read_csv('database/processed/uap_merged_data.csv')
    data['date'] = pd.to_datetime(data['date'])
except:
    data = pd.DataFrame({
        'date': ['2004-11-14', '2015-01-21', '2019-07-15'],
        'location': ['Pacific Ocean', 'East Coast USA', 'Atlantic Ocean'],
        'velocity_mach': [5.2, 3.8, 4.5],
        'acceleration_g': [500, 300, 450],
        'sensor_type': ['Radar/FLIR', 'Radar', 'Optical'],
        'anomaly': ['Instant acceleration', 'No sonic boom', 'Transmedium travel']
    })
    data['date'] = pd.to_datetime(data['date'])

st.title("🛸 Cloud 9 UAP Dashboard")
st.markdown("Explore global UAP sightings, propulsion data, and anomalies.")

st.sidebar.header("Filters")
sensor_type = st.sidebar.multiselect("Sensor Type", options=data['sensor_type'].unique(), default=list(data['sensor_type'].unique()))
anomaly = st.sidebar.multiselect("Anomaly", options=data['anomaly'].unique(), default=list(data['anomaly'].unique()))

filtered = data[data['sensor_type'].isin(sensor_type) & data['anomaly'].isin(anomaly)]

st.header("📈 UAP Flight Characteristics")
fig = px.scatter(filtered, x='velocity_mach', y='acceleration_g', color='anomaly', hover_data=['date', 'location'])
st.plotly_chart(fig, use_container_width=True)

st.subheader("Data Table")
st.dataframe(filtered, use_container_width=True)
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
