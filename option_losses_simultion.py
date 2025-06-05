import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
np.random.seed(42)
num_traders = 1000
option_premium = 5       # Retail pays ₹5 per option
strike_price = 100
underlying_start = 100
time_to_expiry = 10      # Days until expiry
volatility = 0.02        # Daily volatility (2%)
mm_cash = 0
retail_pnl = []

# Simulate each trader's option trade
for _ in range(num_traders):
    # Retail buys 1 call option
    mm_cash += option_premium  # MM receives premium

    # Simulate underlying price over time_to_expiry days (random walk)
    price_path = underlying_start + np.cumsum(
        np.random.normal(0, volatility * underlying_start, time_to_expiry)
    )
    final_price = price_path[-1]

    # Retail profit/loss = intrinsic value - premium
    intrinsic_value = max(final_price - strike_price, 0)
    pnl = intrinsic_value - option_premium
    retail_pnl.append(pnl)

# Market maker profit = premiums received - payoff to winning traders
retail_pnl = np.array(retail_pnl)
mm_pnl = mm_cash - np.sum(np.maximum(retail_pnl + option_premium, 0))

# Plotting PnL distribution
plt.figure(figsize=(12, 6))
plt.hist(retail_pnl, bins=50, color='blue', alpha=0.6, label="Retail PnL")
plt.axvline(x=0, color='black', linestyle='--')
plt.title("PnL Distribution for 1000 Retail Call Option Buyers")
plt.xlabel("Profit/Loss per Trader (₹)")
plt.ylabel("Number of Traders")
plt.legend()
plt.grid(True)
plt.show()

# Summary stats
print(f"Market Maker Total PnL: ₹{mm_pnl:.2f}")
print(f"Average Retail PnL: ₹{retail_pnl.mean():.2f}")
print(f"Percentage of Profitable Retail Traders: {100 * (retail_pnl > 0).mean():.1f}%")
