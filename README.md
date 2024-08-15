Stock Price Monitor

This script retrieves real-time stock prices and displays them in the terminal. It shows the current price, price change, percentage change, and trading volume for each specified ticker. The display is updated every 60 seconds. Positive changes are highlighted in green, while negative changes are highlighted in red.

Features:

- Real-time Stock Prices: Fetches up-to-the-minute stock prices using the yfinance library.
- Price Change and Percentage Change: Calculates and displays the price change and percentage change relative to the previous close. It uses safe handling to avoid crashes   
  when data is temporarily unavailable.
- Volume: Displays the total trading volume for the day.
- Color-coded Output:
- Positive price changes are displayed in green.
- Negative price changes are displayed in red.
- Error Handling: Robust error handling ensures the script continues to run even if data retrieval for a specific ticker fails.
- Automatic Updates: The display refreshes every 5 minutes (300 seconds).

Prerequisites:

Python 3.x
yfinance library
