import yfinance as yf
import pandas as pd
import os


def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)

    # Get project root folder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Create data folder path
    data_folder = os.path.join(base_dir, "data")
    os.makedirs(data_folder, exist_ok=True)

    filename = os.path.join(data_folder, f"{ticker.replace('.', '_')}.csv")

    data.to_csv(filename)

    print(f"Saved data to {filename}")
    return data


if __name__ == "__main__":
    stock = fetch_stock_data("RELIANCE.NS", "2023-01-01", "2026-04-17")
    print(stock.head())