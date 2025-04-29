from customtkinter import *
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import customtkinter as ct
import tkcalendar as tc
from datetime import datetime

def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def plot_stock_data_with_moving_averages(stock_data, symbol):
    stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['200_MA'] = stock_data['Close'].rolling(window=200).mean()
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=f'{symbol} Close Price', color='blue')
    plt.plot(stock_data['50_MA'], label='50-Day Moving Average', color='orange')
    plt.plot(stock_data['200_MA'], label='200-Day Moving Average', color='red')
    plt.title(f'{symbol} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_candlestick_chart(stock_data, symbol):
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                        open=stock_data['Open'],
                                        high=stock_data['High'],
                                        low=stock_data['Low'],
                                        close=stock_data['Close'])])
    fig.update_layout(title=f'{symbol} Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)')
    fig.show()

def main():
    stock_symbol = StockSymbolEntry.get().strip().upper()  # Get symbol, remove whitespace, and uppercase
    start_date = StartTimeCalendar.get_date()
    end_date = EndTimeCalendar.get_date()

    # Convert tkcalendar dates to 'YYYY-MM-DD' string format
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    stock_data = fetch_stock_data(stock_symbol, start_date_str, end_date_str)

    if stock_data is None or stock_data.empty:
        print(f"No data found for symbol: {stock_symbol}, Start Date: {start_date_str}, End Date: {end_date_str}")
    else:
        plot_stock_data_with_moving_averages(stock_data, stock_symbol)
        plot_candlestick_chart(stock_data, stock_symbol)

app = ct.CTk()
app.title("Stocks Visualizer")
app.geometry("900x600")
ct.set_appearance_mode("dark")

title = ct.CTkLabel(app, text="Stocks Visualizer")
title.pack(pady=10)

stock_frame = ct.CTkFrame(app)
stock_frame.pack(pady=5)

StockSymbolInstructions = ct.CTkLabel(stock_frame, text="Enter stock symbol (e.g., AAPL):")
StockSymbolInstructions.pack(side="left", padx=5)

StockSymbolEntry = ct.CTkEntry(stock_frame, width=100)
StockSymbolEntry.pack(side="left", padx=5)

start_frame = ct.CTkFrame(app)
start_frame.pack(pady=5)

StartTimeCalendar = tc.DateEntry(start_frame, date_pattern='yyyy-mm-dd')
StartTimeCalendar.pack(side="left", padx=5)
StartTimeEntryInstructions = ct.CTkLabel(start_frame, text="Start Date:")
StartTimeEntryInstructions.pack(side="left", padx=5)

end_frame = ct.CTkFrame(app)
end_frame.pack(pady=5)

EndTimeCalendar = tc.DateEntry(end_frame, date_pattern='yyyy-mm-dd')
EndTimeCalendar.pack(side="left", padx=5)
EndTimeEntryInstructions = ct.CTkLabel(end_frame, text="End Date:")
EndTimeEntryInstructions.pack(side="left", padx=5)

visualizeBtn = ct.CTkButton(app, width=100, text="Visualize", command=main)
visualizeBtn.pack()

app.mainloop()