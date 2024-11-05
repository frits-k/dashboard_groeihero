import streamlit as st
import pandas as pd
import json

st.title("Groeihero Dashboard")
st.image("logo.png", width=200)  # Place your logo here

st.write("This is a prototype dashboard displaying dummy data.")

# Create a row with 3 equal-width columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Impressions", value="1,500")

with col2:
    st.metric(label="Clicks", value="300")

with col3:
    st.metric(label="Conversions", value="60")


# Load dummy data
with open("dummy_data.json") as f:
    data = json.load(f)
df = pd.DataFrame([data])

# Display KPIs
st.metric(label="Impressions", value=df["impressions"][0])
st.metric(label="Clicks", value=df["clicks"][0])
st.metric(label="Bounce Rate", value=f"{df['bounce_rate'][0]*100}%")
st.metric(label="Conversions", value=df["conversions"][0])

# Date filter
date_options = ["2023-10-01", "2023-10-02", "2023-10-03"]
selected_date = st.selectbox("Select Date", date_options)

# Filter df by date
filtered_df = df[df['date'] == selected_date]