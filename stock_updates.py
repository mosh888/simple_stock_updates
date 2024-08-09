import yfinance as yf
import time
from datetime import datetime

# List of stock tickers including ^NDX
tickers = ['^NDX', 'BTC-USD', 'TSLA']
# other_tickers = ['^FTSE', 'AAPL', 'GOOGL', 'MSFT', 'AMZN']

def get_stock_updates(tickers):
    print(f"\n{'Ticker':<10}{'Price':<12}{'Change':<12}{'% Change':<12}{'Volume':<20}")
    print('-' * 70)
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='1d', interval='1m')
        
        if not hist.empty:
            current_data = hist['Close'].iloc[-1]
            previous_close = stock.info['previousClose']
            volume = int(hist['Volume'].sum())  # Total volume for the day
            
            price = current_data
            change = current_data - previous_close
            percentage_change = round((change / previous_close) * 100, 2)  # Round to 2 decimal places
            
            # Adding signs for change and percentage change
            change_str = f"{change:+.2f}"
            percentage_change_str = f"{percentage_change:+.2f}"
            
            print(f"{ticker:<10}{price:<12.2f}{change_str:<12}{percentage_change_str:<12}{volume:,}")
        else:
            print(f"{ticker:<10}{'No data':<12}{'No data':<12}{'No data':<12}{'No data':<20}")
    
    # Print the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\nLast updated: {current_time}")
    print('-' * 70)

while True:
    get_stock_updates(tickers)
    time.sleep(60)  # Wait time in seconds
