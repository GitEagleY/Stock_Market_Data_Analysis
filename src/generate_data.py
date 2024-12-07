import pandas as pd
import numpy as np
import random


# Generate Raw Data
def generate_raw_data():
    n_rows = 50  # The number of rows for the data
    n_missing = 5  # Number of missing rows to add at the end

    # Generate random data
    stock_data = random.choices(["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"], k=n_rows)
    date_data = pd.date_range(start="2023-01-01", periods=n_rows).to_list() + [None] * n_missing
    open_data = np.round(np.random.uniform(100, 300, size=n_rows), 2).tolist() + [None] * n_missing
    close_data = np.round(np.random.uniform(100, 300, size=n_rows), 2).tolist() + [None] * n_missing
    volume_data = [random.randint(1000, 10000) for _ in range(n_rows)] + [None] * n_missing

    # Ensure all columns have the same length
    max_length = max(len(stock_data), len(date_data), len(open_data), len(close_data), len(volume_data))

    # Make sure all lists are the same length by padding with None if needed
    stock_data += [None] * (max_length - len(stock_data))
    date_data += [None] * (max_length - len(date_data))
    open_data += [None] * (max_length - len(open_data))
    close_data += [None] * (max_length - len(close_data))
    volume_data += [None] * (max_length - len(volume_data))

    # Creating DataFrame
    raw_data = {
        "Stock": stock_data,
        "Date": date_data,
        "Open": open_data,
        "Close": close_data,
        "Volume": volume_data,
    }

    raw_df = pd.DataFrame(raw_data)
    raw_df = raw_df.sample(frac=1).reset_index(drop=True)  # Shuffle rows
    return raw_df


# Generate Processed Data
def generate_processed_data(raw_df):
    # Drop missing values
    processed_data = raw_df.dropna().copy()
    # Format dates
    processed_data["Date"] = pd.to_datetime(processed_data["Date"])
    # Sort by stock and date
    processed_data = processed_data.sort_values(by=["Stock", "Date"])
    # Add daily change column
    processed_data["Daily Change"] = (processed_data["Close"] - processed_data["Open"]).round(2)
    return processed_data


# Save Data to CSV files
def save_data(raw_df, processed_data):
    raw_file_path = "../Data/stock_raw_data.csv"
    processed_file_path = "../Data/stock_processed_data.csv"
    raw_df.to_csv(raw_file_path, index=False)
    processed_data.to_csv(processed_file_path, index=False)
    print(f"Data saved: {raw_file_path} and {processed_file_path}")


# Main function to run the script
def main():
    raw_df = generate_raw_data()
    processed_data = generate_processed_data(raw_df)
    save_data(raw_df, processed_data)


if __name__ == "__main__":
    main()
