import streamlit as st
import pandas as pd
from agent.price_optimization_engine import PriceEngine

st.title("AI Price Optimization Agent")

# Load competitor data
uploaded_file = st.file_uploader("Upload competitor_pricing.csv", type="csv")
if uploaded_file:
    comp_df = pd.read_csv(uploaded_file)
else:
    comp_df = pd.read_csv("data/competitor_pricing.csv")

item = st.selectbox("Select Item", comp_df['item'].unique())
demand = st.selectbox("Demand Level", ['High', 'Medium', 'Low'])
event = st.text_input("Event (e.g., Black Friday)")

if st.button("Optimize Price"):
    engine = PriceEngine(comp_df)
    optimized_price = engine.optimize_price(item, demand, event)
    st.metric("Optimized Price", f"${optimized_price:.2f}")