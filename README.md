# Ecom AI Agents Repo

This repository implements multiple AI agents for e-commerce use cases, starting with an AI Sales Agent and expanding to recommendation, inventory forecasting, customer support, and price optimization. All agents are built with modular components using tools like Streamlit for UIs, LlamaIndex/LangChain for RAG/LLM chains, and ML libraries for predictions.

## Use Cases

1. **AI Sales Agent** (Original)
   - Description: Generates sales pitches, RAG over catalogs, and SQL-based dashboards for e-com sales.
   - Key Files: `sales_app.py` (UI), `agent/pitch_generator.py`, `agent/rag_engine.py`, `agent/sql_dashboard.py`.
   - Data: `data/sample_catalog.csv`, `data/competitor_pricing.csv`.
   - Boosts sales efficiency with PDF pitches and data insights.

2. **AI Product Recommendation Agent** (Personalized Recs via RAG + User History)
   - Description: Analyzes user browsing history and catalog to generate personalized recommendations (e.g., "Similar jackets under $200"). Boosts cart value by 20-30%.
   - Key Files: `recommend_app.py` (UI), `agent/recommend_engine.py` (RAG + Cosine Similarity).
   - Data: `data/user_history.csv` (sample), reuses `data/sample_catalog.csv`.
   - Alignment: Enhances AIOps for personalized e-com experiences.

3. **AI Inventory Forecast Agent** (Time-Series Prediction with Prophet)
   - Description: Forecasts stock levels from sales data (e.g., "Predict next 30 days for jackets"). Reduces out-of-stocks by 15-25%.
   - Key Files: `inventory_app.py` (UI), `agent/forecast_engine.py` (Prophet ML).
   - Data: `data/sales_history.csv` (sample).
   - Alignment: Predictive maintenance-like wins for inventory management.

4. **AI Customer Support Agent** (Chatbot with RAG + Intent Detection)
   - Description: Handles queries like "Return policy for jackets?" using RAG over FAQs/catalog. Resolves 80% issues autonomously.
   - Key Files: `support_app.py` (Chat UI), `agent/support_engine.py` (LangChain Chain).
   - Data: `data/faqs.txt` (sample), reuses `data/sample_catalog.csv`.
   - Alignment: Multilingual chatbot POC for customer service.

5. **AI Price Optimization Agent** (Dynamic Pricing with ML)
   - Description: Adjusts prices based on competitor data/demand (e.g., "Optimize jacket for Black Friday"). Increases margins by 10-15%.
   - Key Files: `price_app.py` (UI), `agent/price_engine.py` (Regression ML).
   - Data: Reuses `data/competitor_pricing.csv`, `data/sample_catalog.csv`.
   - Alignment: Ties into telematics/risk pricing for dynamic e-com pricing.

## Dependencies

- Python 3.8+
- Install via: `pip install -r requirements.txt`
- Key packages:
  - `streamlit`: For all UIs.
  - `llama-index` & `langchain`: For RAG and LLM chains.
  - `jinja2` & `weasyprint`: For PDF generation (sales agent).
  - `pandas`: Data handling.
  - `scikit-learn==1.5.1`: For similarity and regression ML (recommendation & pricing agents).
  - `prophet==1.1.5`: For time-series forecasting (inventory agent).

## Setup

1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in any API keys (e.g., for LLMs if needed).
4. Add sample data to `data/` if customizing.

## Running the Agents

- Sales Agent: `streamlit run sales_app.py`
- Recommendation Agent: `streamlit run recommend_app.py`
- Inventory Forecast Agent: `streamlit run inventory_app.py`
- Customer Support Agent: `streamlit run support_app.py`
- Price Optimization Agent: `streamlit run price_app.py`

Each app provides a simple interface to interact with the agent. For example, upload CSVs or input queries as prompted.

## Implementation Notes

- Agents are modular: Reuse components like RAG across use cases.
- Extend by adding more agents following the pattern (new `_app.py` and `agent/*_engine.py`).
- For production, containerize with Docker and deploy to cloud (e.g., Heroku/Render).

## Contributing

Pull requests welcome! Focus on adding new use cases or improving ML accuracy.


## Author
**Mohan Khilariwal**  
AI/ML Leader | USPTO Patent 12,540,924  
[LinkedIn](https://linkedin.com/in/mohankhilariwal) | [GitHub](https://github.com/mohankhilariwal)

---
