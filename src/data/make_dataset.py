import requests
import json
import pandas as pd


with open("src/data/config.json", "r") as file:
    config = json.load(file)
    API_KEY = config['api']['iex_key']
    BASE_URL = config['api']['base_url']


RAW_DATA_PATH = "data/raw"

def save_raw_stock_data_to_csv(symbol, selected_time_range="1y"):
    # Prepare request parameters
    params = {"token": API_KEY}
    # Make the API request
    response = requests.get(f"{BASE_URL}stock/{symbol}/chart/{selected_time_range}", params=params)
    data = response.json()

    if "error" not in data:
            stock_data = pd.DataFrame(data)
            if not stock_data.empty:
                stock_data["date"] = pd.to_datetime(stock_data["date"])
                stock_data.set_index("date", inplace=True)
                
                first_date = stock_data.index.min().strftime('%Y_%m_%d')
                last_date = stock_data.index.max().strftime('%Y_%m_%d')

                # Save the raw data to CSV
                csv_filename = f"{symbol}_{first_date}_to_{last_date}.csv"

                # Save the raw data to CSV
                # csv_filename = f"{symbol}_{selected_time_range}.csv"
                csv_path = RAW_DATA_PATH + "/" + csv_filename
                stock_data.to_csv(csv_path)
                print(f"Raw Data of {symbol} from {first_date} to {last_date} saved to {csv_path}")
            else:
                print(f"No available data for symbol: {symbol} for {selected_time_range} time range")


def load_sp500_symbols(csv_path):
    try:
        df = pd.read_csv(csv_path)
        return df['Symbol'].tolist()  # Assuming 'Symbol' is the column name holding the stock symbols
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return []

def fetch_all_sp500_stock_data(symbols, time_range="1y"):
    # for symbol in tqdm(symbols, desc="Processing S&P 500 Companies"):   
    for symbol in symbols:    
        print(f"Fetching data for {symbol}...")
        try:
            save_raw_stock_data_to_csv(symbol, time_range)
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {e}")
    print("Fetching completed!")

# Load symbols from the CSV
sp500_symbols = load_sp500_symbols("data/interim/sp500_list.csv")
print(sp500_symbols)
# Fetch stock data for all loaded symbols
fetch_all_sp500_stock_data(sp500_symbols, "max")
