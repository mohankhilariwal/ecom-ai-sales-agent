import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Try to import Prophet, but have a fallback
try:
    from prophet import Prophet
    import cmdstanpy
    # Check if cmdstan is available
    try:
        cmdstanpy.find_cmdstan()
        PROPHET_AVAILABLE = True
    except Exception:
        print("Warning: cmdstan not found. Installing cmdstan (this may take a few minutes)...")
        try:
            cmdstanpy.install_cmdstan()
            PROPHET_AVAILABLE = True
        except Exception as e:
            print(f"Could not install cmdstan: {e}. Using simple linear regression instead.")
            PROPHET_AVAILABLE = False
except ImportError:
    PROPHET_AVAILABLE = False

class ForecastEngine:
    def __init__(self, sales_df):
        self.sales_df = sales_df.copy()
        self.sales_df['ds'] = pd.to_datetime(self.sales_df['date'])
        self.sales_df['y'] = self.sales_df['sales_quantity']
        # Sort by date
        self.sales_df = self.sales_df.sort_values('ds')

    def forecast(self, periods=7):
        if PROPHET_AVAILABLE:
            try:
                m = Prophet()
                m.fit(self.sales_df[['ds', 'y']])
                future = m.make_future_dataframe(periods=periods)
                forecast = m.predict(future)
                return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
            except Exception as e:
                print(f"Prophet failed: {e}. Falling back to linear regression.")
                return self._simple_forecast(periods)
        else:
            return self._simple_forecast(periods)
    
    def _simple_forecast(self, periods=7):
        """Fallback forecasting method using linear regression"""
        # Create numeric index for regression
        self.sales_df['day_num'] = (self.sales_df['ds'] - self.sales_df['ds'].min()).dt.days
        
        X = self.sales_df[['day_num']].values
        y = self.sales_df['y'].values
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Generate future dates
        last_date = self.sales_df['ds'].max()
        future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=periods, freq='D')
        last_day_num = self.sales_df['day_num'].max()
        future_day_nums = np.arange(last_day_num + 1, last_day_num + 1 + periods).reshape(-1, 1)
        
        # Predict
        yhat = model.predict(future_day_nums)
        
        # Calculate confidence intervals
        residuals = y - model.predict(X)
        std_error = np.std(residuals)
        yhat_lower = yhat - 1.96 * std_error
        yhat_upper = yhat + 1.96 * std_error
        
        # Create forecast dataframe
        forecast = pd.DataFrame({
            'ds': future_dates,
            'yhat': yhat,
            'yhat_lower': yhat_lower,
            'yhat_upper': yhat_upper
        })
        
        return forecast