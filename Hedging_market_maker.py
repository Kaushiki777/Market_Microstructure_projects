import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
np.random.seed(3)
num_trades = 100
inventory_limit = 20
starting_price = 100
spread = 0.05
price_volatility = 0.3
hedge_threshold = 10  # Inventory level beyond which MM initiates hedge
hedge_cost_per_unit = 0.01  # Hedging cost per unit hedged

# Tracking variables
inventory = [0]
price = [starting_price]
pnl = [0]
hedged = [0]  # Track how much inventory has been hedged
trade_log = []

for i in range(num_trades):
    direction = np.random.choice([-1, 1])  # -1 = MM buys (client sells), +1 = MM sells (client buys)
    trade_price = price[-1] + direction * spread
    new_inventory = inventory[-1] + direction

    # Inventory risk control
    if abs(new_inventory) > inventory_limit:
        # Reject trade
        inventory.append(inventory[-1])
        price.append(price[-1] + np.random.normal(0, price_volatility))
        pnl.append(pnl[-1])
        hedged.append(hedged[-1])
        trade_log.append((i, "Rejected", inventory[-1], price[-1], pnl[-1], hedged[-1], 0))
        continue

    # Accept trade
    inventory.append(new_inventory)
    new_price = price[-1] + np.random.normal(0, price_volatility)
    price.append(new_price)

    # Hedging logic: If inventory exceeds threshold, hedge to bring it back below threshold
    hedge_amount = 0
    if abs(new_inventory) > hedge_threshold:
        hedge_direction = -1 if new_inventory > 0 else 1
        hedge_amount = abs(new_inventory) - hedge_threshold
        new_inventory += hedge_direction * hedge_amount
        hedge_cost = hedge_amount * hedge_cost_per_unit
    else:
        hedge_cost = 0

    # Update inventory after hedging
    inventory[-1] = new_inventory
    hedged.append(hedged[-1] + hedge_amount)

    # PnL includes unrealized + hedge cost
    current_pnl = new_inventory * (new_price - trade_price) - hedge_cost
    pnl.append(current_pnl)

    trade_log.append((i, "Accepted", new_inventory, new_price, current_pnl, hedged[-1], hedge_amount))

# DataFrame log
df = pd.DataFrame(trade_log, columns=["Trade #", "Status", "Inventory", "Price", "PnL", "Cumulative Hedge", "Hedge Amount"])
print(df)

# Plotting
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
plt.plot(inventory, label="Inventory")
plt.axhline(inventory_limit, color='red', linestyle='--', label="Inventory Limit")
plt.axhline(-inventory_limit, color='red', linestyle='--')
plt.axhline(hedge_threshold, color='orange', linestyle='--', label="Hedge Threshold")
plt.axhline(-hedge_threshold, color='orange', linestyle='--')
plt.title("Inventory Over Time with Hedging")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(pnl, color='green', label="Unrealized PnL (with Hedge Cost)")
plt.title("PnL Over Time")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(hedged, color='purple', label="Cumulative Hedge Executed")
plt.title("Cumulative Hedging Over Time")
plt.legend()

plt.tight_layout()
plt.show()
