from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import matplotlib.pyplot as plt

# Display MetaTrader5 package info
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# Set pandas display options
pd.set_option('display.max_columns', 500) # Number of columns to be displayed
pd.set_option('display.width', 1500)      # Max table width to display

# Establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Get 200 GBPUSD D1 bars from the current day
bars = mt5.copy_rates_from_pos("GBPUSDz", mt5.TIMEFRAME_M5, 0, 200)

# Shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# Display obtained data 'as is'
print("Display obtained data 'as is'")
for bar in bars:
    print(bar)

# Create DataFrame out of the obtained data
bars_frame = pd.DataFrame(bars)
# Convert time in seconds into the datetime format
bars_frame['time'] = pd.to_datetime(bars_frame['time'], unit='s')

# Calculate 200-day and 20-day moving averages
bars_frame['200MA'] = bars_frame['close'].rolling(window=200).mean()
bars_frame['20MA'] = bars_frame['close'].rolling(window=20).mean()

# Display the DataFrame with moving averages
print(bars_frame[['200MA', '20MA']][199:])