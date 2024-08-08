import yfinance as yf
import time
from datetime import datetime

# List of stock tickers including ^NDX
tickers = ['TSLA', '^NDX']
# tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', '^NDX']

def get_stock_updates(tickers):
    print(f"\n{'Ticker':<10}{'Price':<10}{'Change':<10}{'% Change':<10}")
    print('-' * 45)
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='1d', interval='1m')
        
        if not hist.empty:
            current_data = hist['Close'].iloc[-1]
            previous_close = stock.info['previousClose']
            price = current_data
            change = current_data - previous_close
            percentage_change = (change / previous_close) * 100
            
            print(f"{ticker:<10}{price:<10.2f}{change:+10.2f}{percentage_change:+10.2f}")
        else:
            print(f"{ticker:<10}{'No data':<10}{'No data':<10}{'No data':<10}")
    
    # Print the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\nLast updated: {current_time}")
    print('-' * 45)

while True:
    get_stock_updates(tickers)
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
