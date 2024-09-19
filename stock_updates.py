import yfinance as yf
import time
from datetime import datetime
import pandas as pd
import pandas_ta as ta

# List of stock tickers including ^NDX
tickers = ['NQ=F', 'ES=F', '^FTSE', 'GOOGL', 'BTC-USD', 'GOOGL', 'TSLA']
# tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', '^NDX']

# ANSI escape codes for coloring
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def get_stock_updates(tickers):
    print(f"\n{'Ticker':<10}{'Price':<12}{'Change':<12}{'% Change':<12}{'Volume':<20}{'MA10':<10}{'MA50':<10}{'RSI':<10}")
    print('-' * 110)
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
                    
                    # Calculate technical indicators
                    ma10 = ta.sma(hist['Close'], length=10).iloc[-1]  # 10-period MA
                    ma50 = ta.sma(hist['Close'], length=50).iloc[-1]  # 50-period MA
                    rsi = ta.rsi(hist['Close'], length=14).iloc[-1]   # 14-period RSI
                    
                    # Handle cases where MA or RSI cannot be calculated due to insufficient data
                    ma10 = f"{ma10:.2f}" if not pd.isna(ma10) else "N/A"
                    ma50 = f"{ma50:.2f}" if not pd.isna(ma50) else "N/A"
                    rsi = f"{rsi:.2f}" if not pd.isna(rsi) else "N/A"
                    
                    price = round(current_data, 2)
                    change = round(current_data - previous_close, 2)
                    percentage_change = round((change / previous_close) * 100, 2)  # Round to 2 decimal places
                    
                    # Determine color based on the change value
                    color = GREEN if change >= 0 else RED
                    
                    # Adding signs for change and percentage change
                    change_str = f"{change:+.2f}"
                    percentage_change_str = f"{percentage_change:+.2f}%"
                    
                    # Print the values with the selected color
                    print(f"{ticker:<10}{color}{price:<12.2f}{change_str:<12}{percentage_change_str:<12}{volume:<20,}{RESET}{ma10:<10}{ma50:<10}{rsi:<10}")
                else:
                    print(f"{ticker:<10}{'No data':<12}{'No data':<12}{'No data':<12}{'No data':<20}{'N/A':<10}{'N/A':<10}{'N/A':<10}")
            else:
                print(f"{ticker:<10}{'No data':<12}{'No data':<12}{'No data':<12}{'No data':<20}{'N/A':<10}{'N/A':<10}{'N/A':<10}")
        
        except KeyError as e:
            print(f"KeyError for {ticker}: {e}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    
    # Print the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S %p')
    print(f"\nLast updated: {current_time}")
    print('-' * 110)

while True:
    get_stock_updates(tickers)
    time.sleep(300)  # Wait time in seconds
