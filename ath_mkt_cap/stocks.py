import yfinance as yf
import pandas as pd
import logging
from tqdm import tqdm
from config import TICKERS, DATE_FORMAT, CSV_FILE_PATH, OUTPUT_CSV_FILE_PATH

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read the CSV file into a DataFrame using the correct date format
df = pd.read_csv(CSV_FILE_PATH, parse_dates=['date'], date_format=DATE_FORMAT)

# Normalize time zone by stripping it if present
df['date'] = df['date'].dt.tz_localize(None)

# Prepare an empty list to store the data
stock_data = []

# Process each ticker
for ticker in tqdm(TICKERS, desc="Processing Tickers"):
    try:
        logging.info(f"Processing {ticker}")
        ticker_data = yf.Ticker(ticker)
        history = ticker_data.history(period="max")

        # Normalize the index to remove the timezone information
        history.index = history.index.tz_localize(None)

        ath_px = history['High'].max()
        ath_date = history['High'].idxmax()
        last_px = history['Close'].iloc[-1]
        last_shrs = ticker_data.info['sharesOutstanding'] / 1e6  # Convert to millions
        last_mkt_cap = last_px * last_shrs

        # Find the closest dates to ath_date in the 'date' column
        closest_dates = df['date'].subtract(ath_date).abs().nsmallest(2).index
        ticker_column = f"{ticker}_shr_outs (m)"
        ath_shares = df.loc[closest_dates, ticker_column].mean()
        ath_mkt_cap = ath_px * ath_shares

        # Append the new row to the stock_data list
        stock_data.append({
            'ticker': ticker,
            'ath_px': ath_px,
            'ath_shares': ath_shares,
            'ath_mkt_cap': ath_mkt_cap,
            'ath_date': ath_date.strftime('%Y-%m-%d'),
            'last_px': last_px,
            'last_shrs': last_shrs,
            'last_mkt_cap': last_mkt_cap
        })

    except Exception as e:
        logging.error(f"Failed to process {ticker}: {e}")

# Convert the list of dictionaries to a DataFrame
stock_data_df = pd.DataFrame(stock_data)

# Write the DataFrame to a CSV file
stock_data_df.to_csv(OUTPUT_CSV_FILE_PATH, index=False)