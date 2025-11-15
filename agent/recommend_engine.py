import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

class RecommendEngine:
    def __init__(self, user_history_df):
        self.user_history = user_history_df
        self.catalog = pd.read_csv("data/sample_catalog.csv")
        # Simple RAG-like: TF-IDF on features + name (combine for better matching)
        self.vectorizer = TfidfVectorizer()
        # Combine name and features for better text matching - ensure all are strings
        self.catalog['description'] = (
            self.catalog['name'].astype(str) + ' ' + 
            self.catalog['features'].fillna('').astype(str)
        )
        # Store vectors as a 2D array for cosine_similarity
        self.catalog_vectors = self.vectorizer.fit_transform(self.catalog['description']).toarray()

    def get_recommendations(self, query, top_k=5):
        query_vec = self.vectorizer.transform([query]).toarray()
        # Use the 2D array directly
        similarities = cosine_similarity(query_vec, self.catalog_vectors)
        self.catalog['score'] = similarities[0]
        # Filter by user history (e.g., category prefs)
        user_cat = self.user_history['category'].mode()[0] if not self.user_history.empty else 'Apparel'
        filtered = self.catalog[self.catalog['category'] == user_cat].sort_values('score', ascending=False).head(top_k)
        return filtered[['name', 'price', 'description', 'score']]