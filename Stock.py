import yfinance as yf
from yahoo_fin import stock_info as si

# Downloading US stock data
us_stocks = ["GOOGL"]  # Add more symbols as needed
us_data = yf.download(us_stocks, start="2024-01-01", end="2024-01-31")

#us_data.info()

# Downloading India stock data
#nse = Nse()
#india_stocks = ["TCS", "RELIANCE", "HDFCBANK"]  # Add more symbols as needed
#india_data = {symbol: nse.get_quote(symbol)['dayHigh'] for symbol in india_stocks}

# Downloading German stock data
#german_stocks = ["ADS.DE", "BMW.DE", "SAP.DE"]  # Add more symbols as needed
#german_data = {symbol: si.get_live_price(symbol) for symbol in german_stocks}

# Displaying the downloaded data
print("US Stock Data:")
print(us_data.head())

#print("\nIndia Stock Data:")
#for symbol, high_price in india_data.items():
#    print(f"{symbol}: Day High - {high_price}")

#print("\nGerman Stock Data:")
#for symbol, live_price in german_data.items():
#    print(f"{symbol}: Live Price - {live_price}")