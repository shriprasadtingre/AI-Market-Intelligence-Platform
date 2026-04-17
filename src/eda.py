import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# SETTINGS
# -----------------------
ticker = "RELIANCE.NS"

# -----------------------
# FETCH LIVE DATA
# -----------------------
df = yf.download(ticker, start="2023-01-01", end="2026-04-17")

# Reset index
df.reset_index(inplace=True)

# -----------------------
# FIX MULTIINDEX COLUMNS
# -----------------------
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# -----------------------
# KEEP REQUIRED COLUMNS
# -----------------------
df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

# -----------------------
# CLEAN TYPES
# -----------------------
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

for col in ["Open", "High", "Low", "Close", "Volume"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop missing rows
df.dropna(inplace=True)

# Sort
df.sort_values("Date", inplace=True)
df.reset_index(drop=True, inplace=True)

# Save CSV
df.to_csv("../data/RELIANCE_NS.csv", index=False)

# Output
print(df.head())
df.info()

# Plot
plt.figure(figsize=(12,6))
plt.plot(df["Date"], df["Close"])
plt.title("RELIANCE.NS Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show(block=False)
plt.pause(5)
plt.savefig("../docs/reliance_chart.png", dpi=300, bbox_inches="tight")
print("Chart saved successfully")