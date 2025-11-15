
# **agent/sql_dashboard.py**

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import duckdb
import plotly.express as px
import pandas as pd

def generate_sql_query(nl_query: str, schema: str):
 llm = ChatOllama(model="llama3.1:8b", temperature=0)
 prompt = ChatPromptTemplate.from_messages([
     ("system", f"You are a SQL expert. Use DuckDB syntax. {schema}. The table name is 'catalog'. Columns 'price' and 'cost' are DOUBLE type. Return ONLY SQL, no markdown, no explanations."),
     ("human", nl_query)
 ])
 chain = prompt | llm
 sql = chain.invoke({}).content.strip()
 if sql.startswith("```sql"):
     sql = sql[6:]
 if sql.startswith("```"):
     sql = sql[3:]
 if sql.endswith("```"):
     sql = sql[:-3]
 return sql.strip()

def run_query_and_plot(sql, csv_path="data/sample_catalog.csv"):
 df = pd.read_csv(csv_path)
 
 # Ensure numeric columns are properly typed
 df['price'] = pd.to_numeric(df['price'], errors='coerce')
 df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
 
 con = duckdb.connect()
 con.register('catalog', df)
 result = con.execute(sql).df()
 
 # Handle different result shapes
 if len(result.columns) >= 2:
     # Standard case: use first column as x, second as y
     fig = px.bar(result, x=result.columns[0], y=result.columns[1], title="Sales Insight")
 elif len(result.columns) == 1:
     # Single column: use index as x-axis, column as y-axis
     fig = px.bar(result, x=result.index, y=result.columns[0], title="Sales Insight")
 else:
     # Empty result or unexpected shape
     fig = px.bar(title="No data to display")
 
 return fig, result
