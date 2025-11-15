import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

class PriceEngine:
    def __init__(self, comp_df):
        self.df = comp_df.copy()
        le = LabelEncoder()
        self.df['demand_encoded'] = le.fit_transform(self.df['demand_level'])
        X = self.df[['demand_encoded']]
        y = self.df['competitor_price']
        self.model = LinearRegression().fit(X, y)

    def optimize_price(self, item, demand, event):
        demand_code = {'High': 0, 'Medium': 1, 'Low': 2}[demand]
        base_price = self.model.predict([[demand_code]])[0]
        # Simple adjustment for event
        adjustment = 0.9 if 'black' in event.lower() else 1.0
        return base_price * adjustment