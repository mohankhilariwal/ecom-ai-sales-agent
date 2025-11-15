
# **app.py** (Main Streamlit App)
import streamlit as st
from agent.rag_agent import build_rag_index
from agent.sql_dashboard import generate_sql_query, run_query_and_plot
from agent.pitch_generator import generate_pitch_deck
import pandas as pd

st.set_page_config(page_title="eCom AI Sales Agent", layout="wide")
st.title("🚀 eCom AI Sales Agent")
st.caption("Built by Mohan Khilariwal | USPTO 12,540,924")

@st.cache_resource
def load_data():
 return pd.read_csv("data/sample_catalog.csv")

df = load_data()
query_engine = build_rag_index()

col1, col2 = st.columns(2)

with col1:
 st.subheader("🎯 Target Market")
 market = st.text_input("e.g., Mid-market fashion brands in Canada")

 st.subheader("🔍 Ask Anything")
 nl_query = st.text_area("Natural Language Query", "Show top 5 products by margin")

if st.button("Generate Sales Package"):
 with st.spinner("Generating..."):
     insights = query_engine.query(f"Best products for {market}")
     
     schema = "Table name: catalog. Columns: name, price, cost, category, features"
     sql = generate_sql_query(nl_query, schema)
     fig, result = run_query_and_plot(sql)
     
     top_products = result.head(3).to_dict('records')
     for p in top_products:
         p['edge'] = "AI-Optimized Pricing"
     pdf_path = generate_pitch_deck(market, top_products)

     st.success("Done!")
     st.plotly_chart(fig, use_container_width=True)
     st.download_button("Download Pitch Deck", open(pdf_path, 'rb'), "pivotree_pitch.pdf")