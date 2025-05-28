import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set random seed for reproducibility
np.random.seed(1)
       
# Parameters
num_trades = 100
inventory_limit = 20
starting_price = 100
spread = 0.05
price_volatility = 0.3
# Initialize tracking variables
inventory = [0]
price = [starting_price]
pnl = [0]
trades = []

for i in range(num_trades):
    direction = np.random.choice([-1, 1])  # -1 = sell, 1 = buy (from MM's perspective)
    trade_price = price[-1] + direction * spread  # Apply spread
    new_inventory = inventory[-1] + direction
    
    # Risk control: skip trade if inventory exceeds limit
    if abs(new_inventory) > inventory_limit:
        inventory.append(inventory[-1])
        price.append(price[-1] + np.random.normal(0, price_volatility))
        pnl.append(pnl[-1])
        trades.append((i, "Rejected", inventory[-1], price[-1], pnl[-1]))
        continue

    # Accept trade
    inventory.append(new_inventory)
    
    # Simulate price move due to market volatility
    new_price = price[-1] + np.random.normal(0, price_volatility)
    price.append(new_price)

    # Unrealized PnL = Inventory * (New Price - Trade Price)
    current_pnl = new_inventory * (new_price - trade_price)
    pnl.append(current_pnl)

    trades.append((i, "Accepted", new_inventory, new_price, current_pnl))

# Create DataFrame of trade log
df = pd.DataFrame(trades, columns=["Trade #", "Status", "Inventory", "Price", "Unrealized PnL"])
print(df)

# Plot inventory and PnL over time
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(inventory, label="Inventory")
plt.axhline(inventory_limit, color='red', linestyle='--', label='Inventory Limit')
plt.axhline(-inventory_limit, color='red', linestyle='--')
plt.title("Market Maker Inventory Over Time")
plt.ylabel("Inventory")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(pnl, label="Unrealized PnL", color='green')
plt.title("Unrealized PnL Over Time")
plt.xlabel("Trade Number")
plt.ylabel("PnL")
plt.legend()

plt.tight_layout()
plt.show()
