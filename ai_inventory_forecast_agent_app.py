import streamlit as st
import pandas as pd
from agent.inventory_forecast_engine import ForecastEngine
import plotly.express as px

st.title("AI Inventory Forecast Agent")

# Load sales history
uploaded_file = st.file_uploader("Upload sales_history.csv", type="csv")
if uploaded_file:
    sales_df = pd.read_csv(uploaded_file)
else:
    sales_df = pd.read_csv("data/sales_history.csv")

item_id = st.selectbox("Select Item ID", sales_df['item_id'].unique())
periods = st.slider("Forecast Periods (days)", 1, 30, 7)

if st.button("Forecast Inventory"):
    engine = ForecastEngine(sales_df[sales_df['item_id'] == item_id])
    forecast = engine.forecast(periods)
    fig = px.line(forecast, x='ds', y='yhat', title=f"Forecast for Item {item_id}")
    st.plotly_chart(fig)
    st.write(forecast)