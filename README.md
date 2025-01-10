# Stock Data Visualization with Moving Averages and Candlestick Charts

## Overview
This Python script allows users to fetch stock price data for a given symbol over a specific date range and visualize it using two different methods:
1. **Stock price with Moving Averages**: A line chart showing the stock's closing price along with 50-day and 200-day moving averages.
2. **Candlestick chart**: A detailed candlestick chart displaying the stock's open, high, low, and close prices.

## Requirements
Before running the script, ensure you have the following libraries installed:

- `yfinance`: For fetching stock price data.
- `matplotlib`: For plotting the line charts.
- `plotly`: For creating interactive candlestick charts.

You can install the required libraries using pip:

```bash
pip install yfinance matplotlib plotly
Script Breakdown
1. fetch_stock_data(symbol, start_date, end_date)
This function fetches historical stock data for the provided stock symbol within the given date range using the yfinance library.

2. plot_stock_data_with_moving_averages(stock_data, symbol)
This function takes the stock data and plots a line chart showing:

The stock's closing price.
The 50-day and 200-day moving averages.
3. plot_candlestick_chart(stock_data, symbol)
This function uses the plotly library to create an interactive candlestick chart that displays:

The open, high, low, and close prices for the stock.
4. main()
This is the entry point of the script. It prompts the user for the stock symbol, start date, and end date, fetches the stock data, and calls the plotting functions.

Usage Instructions
Run the script: Execute the script from the terminal or your Python environment.

Input prompts: The script will ask for two inputs:

Stock Symbol: Enter the stock symbol (e.g., AAPL for Apple, GOOGL for Alphabet).
Start Date: Enter the start date in the format YYYY-MM-DD (e.g., 2020-01-01).
End Date: Enter the end date in the format YYYY-MM-DD (e.g., 2021-01-01).
Example:

sql
Copy code
Enter stock symbol (e.g., AAPL): AAPL
Enter start date (YYYY-MM-DD): 2020-01-01
Enter end date (YYYY-MM-DD): 2021-01-01
Visualization:

The script will fetch the stock data from Yahoo Finance and display:
A line chart with the stock's closing price, 50-day, and 200-day moving averages.
A candlestick chart showing the open, high, low, and close prices for each day within the specified date range.
Error handling:

If no data is found for the given symbol and date range, the script will notify you with an appropriate message.
Example Output
When you input a valid stock symbol and date range, the script will output two visualizations:

Stock Price with Moving Averages (in a line chart format)
Candlestick Chart (interactive plotly chart)
License
This project is licensed under the MIT License - see the LICENSE file for details.
