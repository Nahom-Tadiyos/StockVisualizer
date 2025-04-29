# TradeLens
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 	![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![YFINANCE](https://img.shields.io/badge/YFINANCE-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

## Overview

TradeLens is a Python-based desktop application that allows users to visualize historical stock data. It fetches stock information using the `yfinance` library and presents it through interactive charts embedded directly within the application window. Currently, TradeLens displays two types of charts:

* **Line Graph with Moving Averages:** Shows the closing price of a stock along with its 50-day and 200-day moving averages, generated using `matplotlib`.
* **Candlestick Chart:** Provides a detailed view of the stock's open, high, low, and closing prices for a given period, generated using `plotly`.

## Features

* **Stock Symbol Input:** Users can enter any valid stock ticker symbol (e.g., AAPL, MSFT, GOOG).
* **Date Range Selection:** Users can select a specific start and end date for the historical data using interactive calendar widgets.
* **Moving Averages:** The line graph includes 50-day and 200-day moving averages to help identify trends.
* **Embedded Charts:** Both the line graph and the candlestick chart are displayed directly within the application window, eliminating the need for external browsers.
* **Clean and Dark User Interface:** Built with `customtkinter` for a modern and visually appealing dark theme.

## Prerequisites

Before running TradeLens, ensure you have the following Python libraries installed:

* `customtkinter`: For creating the graphical user interface.
* `yfinance`: For downloading historical stock data from Yahoo Finance.
* `matplotlib`: For generating the line graph.
* `plotly`: For generating the interactive candlestick chart.
* `tkcalendar`: For providing the interactive date selection widgets.

You can install these libraries using pip:

```bash
pip install customtkinter yfinance matplotlib plotly tkcalendar