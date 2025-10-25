from src.data_fetcher import StockDataFetcher
from src.features import FeatureEngineer
import pandas as pd

def main():
    print("="*60)
    print("NVIDIA stock analysis tool")
    print("="*60)
    
    ticker = 'NVDA'
    period = '2y'
    
    print(f"\nFetching {ticker} data for the last {period}...")
    fetcher = StockDataFetcher(ticker)
    df = fetcher.get_historical_data(period=period)
    
    if df is None:
        print("failed to fetch data. Exiting.....")
        return
    
    print(f"\nData Summary:")
    print(f"  Total trading days: {len(df)}")
    print(f"  Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"  Price range: ${df['Close'].min():.2f} - ${df['Close'].max():.2f}")
    
    print(f"\nAdding technical indicators...")
    fe = FeatureEngineer(df)
    df_features = (fe
                   .add_moving_averages([7, 30, 50])
                   .add_rsi()
                   .add_macd()
                   .add_volume_features()
                   .add_price_features()
                   .get_features())
    
    print(f"\nlatest data:")
    print(df_features[['Date', 'Close', 'SMA_7', 'SMA_30', 'RSI', 'MACD']].tail(5))
    
    print("\n" + "="*60)
    print("analysis complete! check notebooks for detailed insights!")
    print("="*60)

if __name__ == "__main__":
    main()