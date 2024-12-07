import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
def load_data():
    raw_df = pd.read_csv("../Data/stock_raw_data.csv")
    processed_data = pd.read_csv("../Data/stock_processed_data.csv")
    return raw_df, processed_data

# Plot Stock Price Trends
def plot_price_trends(processed_data):
    plt.figure(figsize=(10, 6))
    for stock in processed_data["Stock"].unique():
        stock_data = processed_data[processed_data["Stock"] == stock]
        plt.plot(stock_data["Date"], stock_data["Close"], label=stock)
    plt.title("Stock Price Trends")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.legend(loc="best")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot Volatility (Rolling Standard Deviation)
def plot_volatility(processed_data):
    plt.figure(figsize=(10, 6))
    for stock in processed_data["Stock"].unique():
        stock_data = processed_data[processed_data["Stock"] == stock]
        stock_data.set_index("Date", inplace=True)
        volatility = stock_data["Close"].rolling(window=7).std()
        plt.plot(stock_data.index, volatility, label=f"Volatility ({stock})")
    plt.title("Stock Price Volatility (7-Day Rolling Std Dev)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend(loc="best")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot Correlation Heatmap
def plot_correlation(processed_data):
    stock_data_pivot = processed_data.pivot_table(values="Close", index="Date", columns="Stock")
    correlation_matrix = stock_data_pivot.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Stock Price Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# Main function to run the analysis
def main():
    raw_df, processed_data = load_data()
    plot_price_trends(processed_data)
    plot_volatility(processed_data)
    plot_correlation(processed_data)

if __name__ == "__main__":
    main()
