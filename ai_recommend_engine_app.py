import streamlit as st
import pandas as pd
from agent.recommend_engine import RecommendEngine

st.title("AI Product Recommendation Agent")

# Upload or load user history
uploaded_file = st.file_uploader("Upload user_history.csv", type="csv")
if uploaded_file:
    user_history = pd.read_csv(uploaded_file)
else:
    user_history = pd.read_csv("data/user_history.csv")

query = st.text_input("User Query (e.g., 'Similar jackets under $200')")

if st.button("Get Recommendations") and query:
    engine = RecommendEngine(user_history)
    recs = engine.get_recommendations(query)
    st.dataframe(recs)