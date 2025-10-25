import yfinance as yf
import pandas as pd
from datetime import datetime

class StockDataFetcher:
    def __init__(self, ticker='NVDA'):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
    
    def get_historical_data(self, start_date=None, end_date=None, period='5y'):
        try:
            if start_date and end_date:
                df = self.stock.history(start=start_date, end=end_date)
            else:
                df = self.stock.history(period=period)
            
            df.reset_index(inplace=True)
            
            print(f"Successfully fetched {len(df)} rows for {self.ticker}")
            return df
            
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return None
    
    def get_company_info(self):
        try:
            info = self.stock.info
            return {
                'name': info.get('longName'),
                'sector': info.get('sector'),
                'industry': info.get('industry'),
                'market_cap': info.get('marketCap')
            }
        except Exception as e:
            print(f"Error getting company info: {str(e)}")
            return None

if __name__ == "__main__":
    fetcher = StockDataFetcher('NVDA')
    
    data = fetcher.get_historical_data(period='2y')
    
    if data is not None:
        print("\nFirst 5 rows:")
        print(data.head())
        
        print(f"\nColumns: {data.columns.tolist()}")
        print(f"\nDate range: {data['Date'].min()} to {data['Date'].max()}")
        
        info = fetcher.get_company_info()
        if info:
            print(f"\nCompany: {info['name']}")
            print(f"Sector: {info['sector']}")