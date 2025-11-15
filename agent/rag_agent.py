from llama_index.core import VectorStoreIndex, Document, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
import pandas as pd

def build_rag_index(csv_path="data/sample_catalog.csv"):
    df = pd.read_csv(csv_path)
    documents = []
    for _, row in df.iterrows():
        text = f"Product: {row['name']}, Price: ${row['price']}, Category: {row['category']}, Features: {row['features']}"
        documents.append(Document(text=text))
    
    # Set both embedding model and LLM to Ollama
    Settings.embed_model = OllamaEmbedding(model_name="llama3.1:8b")
    Settings.llm = Ollama(model="llama3.1:8b", temperature=0)
    
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine()
