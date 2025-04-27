from customtkinter import *
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import customtkinter as ct

app = ct.CTk()
app.title("Stocks Visualizer")
app.geometry("900x600")

app.mainloop()
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
    stock_symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    stock_data = fetch_stock_data(stock_symbol, start_date, end_date)

    if stock_data.empty:
        print("No data found for the given stock symbol and date range.")
    else:
        plot_stock_data_with_moving_averages(stock_data, stock_symbol)
        plot_candlestick_chart(stock_data, stock_symbol)

