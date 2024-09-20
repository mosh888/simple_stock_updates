import yfinance as yf
import time
from datetime import datetime

# List of stock tickers including ^NDX
tickers = ['NQ=F', '^FTSE', 'GOOGL', 'BTC-USD', 'GOOGL', 'TSLA']
# tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', '^NDX']

# ANSI escape codes for coloring
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def get_stock_updates(tickers):
    print(f"\n{'Ticker':<10}{'Price':<12}{'Change':<12}{'% Change':<12}{'Volume':<20}")
    print('-' * 70)
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period='1d', interval='1m')
            
            if not hist.empty:
                current_data = hist['Close'].iloc[-1]
                
                # Safely get the previous close
                previous_close = stock.info.get('previousClose', None)
                
                if previous_close is not None:
                    volume = int(hist['Volume'].sum())  # Total volume for the day
                    
                    price = current_data
                    change = current_data - previous_close
                    percentage_change = round((change / previous_close) * 100, 2)  # Round to 2 decimal places
                    
                    # Determine color based on the change value
                    color = GREEN if change >= 0 else RED
                    
                    # Adding signs for change and percentage change
                    change_str = f"{change:+.2f}"
                    percentage_change_str = f"{percentage_change:+.2f}%"
                    
                    # Print the values with the selected color
                    print(f"{ticker:<10}{color}{price:<12.2f}{change_str:<12}{percentage_change_str:<12}{volume:,}{RESET}")
                else:
                    print(f"{ticker:<10}{'No data':<12}{'No data':<12}{'No data':<12}{'No data':<20}")
            else:
                print(f"{ticker:<10}{'No data':<12}{'No data':<12}{'No data':<12}{'No data':<20}")
        
        except KeyError as e:
            print(f"KeyError for {ticker}: {e}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    # Print the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S %p')
    print(f"\nLast updated: {current_time}")
    print('-' * 70)

while True:
    get_stock_updates(tickers)
    time.sleep(300)  # Wait time in seconds
