# Stock All-Time High Market Cap Calculator

This project calculates the all-time high market capitalization of stocks (Argentine in this case) using the Yahoo Finance API and generates a CSV file with the processed data.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- pandas
- yfinance
- tqdm

You can install the required packages using pip:

```
pip install pandas yfinance tqdm
```

## Configuration

The project uses a `config.py` file to store the configuration parameters. Update the values in the `config.py` file according to your requirements:

- `TICKERS`: A list of Argentine stock tickers to process.
- `DATE_FORMAT`: The date format used in the input CSV file.
- `CSV_FILE_PATH`: The path to the input CSV file containing the stock data.
- `OUTPUT_CSV_FILE_PATH`: The path to the output CSV file where the processed stock data will be saved.

## Input Data

The script requires an input CSV file containing the stock data. The file should have a column named 'date' representing the date and columns for each stock ticker's shares outstanding.

Example:
```
date,PAM_shr_outs (m),SUPV_shr_outs (m),...
01-Jan-22,100,200,...
02-Jan-22,105,210,...
...
```

Ensure that the input CSV file path is correctly specified in the `CSV_FILE_PATH` variable in the `config.py` file.

## Usage

1. Clone the repository or download the project files.

2. Install the required dependencies as mentioned in the Prerequisites section.

3. Update the `config.py` file with the desired configuration parameters, including the list of Argentine stock tickers.

4. Place the input CSV file containing the stock data in the specified location.

5. Run the script using the following command:
   ```
   python stock_data_processing.py
   ```

6. The script will process the stock data for each Argentine stock ticker and calculate the all-time high market capitalization.

7. The output CSV file will be saved at the location specified in the `OUTPUT_CSV_FILE_PATH` variable in the `config.py` file.

## Output

The script generates an output CSV file with the following columns:

- `ticker`: The Argentine stock ticker symbol.
- `ath_px`: The all-time high price of the stock.
- `ath_shares`: The number of shares outstanding at the all-time high date.
- `ath_mkt_cap`: The market capitalization at the all-time high price and shares outstanding.
- `ath_date`: The date of the all-time high price.
- `last_px`: The latest closing price of the stock.
- `last_shrs`: The latest number of shares outstanding.
- `last_mkt_cap`: The latest market capitalization.

## Logging

The script uses the `logging` module to log informational and error messages. The log messages are displayed in the console and include timestamps, log levels, and relevant information.

## License

This project is licensed under the [MIT License](LICENSE).
```

This updated README file focuses on the specific purpose of the project, which is calculating the all-time high market capitalization of Argentine stocks. It provides an overview of the project, prerequisites, configuration, input data format, usage instructions, output details, logging information, and the license.

Feel free to further customize the README file based on your project's specific requirements and provide any additional information that would be helpful for users or contributors.