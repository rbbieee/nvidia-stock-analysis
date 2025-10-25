import pandas as pd
import numpy as np

class FeatureEngineer:
    def __init__(self, df):
        self.df = df.copy()
    
    def add_moving_averages(self, windows=[7, 14, 30, 50]):
        for window in windows:
            self.df[f'SMA_{window}'] = self.df['Close'].rolling(window=window).mean()
        return self
    
    def add_exponential_ma(self, spans=[12, 26]):
        for span in spans:
            self.df[f'EMA_{span}'] = self.df['Close'].ewm(span=span, adjust=False).mean()
        return self
    
    def add_rsi(self, period=14):
        delta = self.df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        self.df['RSI'] = 100 - (100 / (1 + rs))
        return self
    
    def add_macd(self):
        ema_12 = self.df['Close'].ewm(span=12, adjust=False).mean()
        ema_26 = self.df['Close'].ewm(span=26, adjust=False).mean()
        
        self.df['MACD'] = ema_12 - ema_26
        self.df['MACD_Signal'] = self.df['MACD'].ewm(span=9, adjust=False).mean()
        self.df['MACD_Hist'] = self.df['MACD'] - self.df['MACD_Signal']
        return self
    
    def add_bollinger_bands(self, window=20, num_std=2):
        sma = self.df['Close'].rolling(window=window).mean()
        std = self.df['Close'].rolling(window=window).std()
        
        self.df['BB_Upper'] = sma + (std * num_std)
        self.df['BB_Middle'] = sma
        self.df['BB_Lower'] = sma - (std * num_std)
        return self
    
    def add_volume_features(self):
        self.df['Volume_SMA_20'] = self.df['Volume'].rolling(window=20).mean()
        self.df['Volume_Ratio'] = self.df['Volume'] / self.df['Volume_SMA_20']
        return self
    
    def add_price_features(self):
        self.df['Daily_Return'] = self.df['Close'].pct_change()
        self.df['Volatility_10'] = self.df['Daily_Return'].rolling(window=10).std()
        self.df['Volatility_30'] = self.df['Daily_Return'].rolling(window=30).std()
        self.df['HL_Range'] = (self.df['High'] - self.df['Low']) / self.df['Close']
        self.df['OC_Diff'] = (self.df['Close'] - self.df['Open']) / self.df['Open']
        return self
    
    def add_lag_features(self, lags=[1, 2, 3, 5]):
        for lag in lags:
            self.df[f'Close_Lag_{lag}'] = self.df['Close'].shift(lag)
        return self
    
    def get_features(self, drop_na=True):
        if drop_na:
            original_len = len(self.df)
            self.df = self.df.dropna()
            dropped = original_len - len(self.df)
            print(f"Dropped {dropped} rows with missing values")
            print(f"Final dataset: {len(self.df)} rows, {len(self.df.columns)} columns")
        return self.df

if __name__ == "__main__":
    from data_fetcher import StockDataFetcher
    
    fetcher = StockDataFetcher('NVDA')
    df = fetcher.get_historical_data(period='2y')
    
    if df is not None:
        print("\nApplying feature engineering...")
        
        fe = FeatureEngineer(df)
        df_features = (fe
                       .add_moving_averages()
                       .add_exponential_ma()
                       .add_rsi()
                       .add_macd()
                       .add_bollinger_bands()
                       .add_volume_features()
                       .add_price_features()
                       .add_lag_features()
                       .get_features())
        
        print("\nNew columns added:")
        new_cols = [col for col in df_features.columns if col not in df.columns]
        for col in new_cols:
            print(f"  - {col}")
        
        print("\nSample data:")
        print(df_features[['Date', 'Close', 'SMA_7', 'RSI', 'MACD']].tail())