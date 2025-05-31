import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Simulation parameters
np.random.seed(2)
num_trades = 100
num_mms = 3  # Number of market makers
inventory_limit = 20
starting_price = 100
spread = 0.05
price_volatility = 0.3

# Initialize each market maker's inventory and PnL
mms_inventory = [[0] for _ in range(num_mms)]
mms_pnl = [[0] for _ in range(num_mms)]
mms_price = [[starting_price] for _ in range(num_mms)]
trade_log = []

# Simulate trades
for i in range(num_trades):
    direction = np.random.choice([-1, 1])  # -1 = client sells to MM (MM buys), +1 = client buys from MM (MM sells)

    # Each MM provides a quote based on spread and direction
    quotes = []
    for mm_id in range(num_mms):
        quote_price = mms_price[mm_id][-1] + direction * spread
        quotes.append((mm_id, quote_price))

    # Select MM with best price for the client
    if direction == -1:  # Client sells → MM should buy at highest price
        chosen_mm_id, trade_price = max(quotes, key=lambda x: x[1])
    else:  # Client buys → MM should sell at lowest price
        chosen_mm_id, trade_price = min(quotes, key=lambda x: x[1])

    # Inventory update
    new_inventory = mms_inventory[chosen_mm_id][-1] + direction
    if abs(new_inventory) > inventory_limit:
        # Trade rejected
        for mm_id in range(num_mms):
            mms_inventory[mm_id].append(mms_inventory[mm_id][-1])
            new_price = mms_price[mm_id][-1] + np.random.normal(0, price_volatility)
            mms_price[mm_id].append(new_price)
            mms_pnl[mm_id].append(mms_pnl[mm_id][-1])
        trade_log.append((i, direction, "Rejected", None, None, None))
        continue

    # Trade accepted
    for mm_id in range(num_mms):
        if mm_id == chosen_mm_id:
            mms_inventory[mm_id].append(new_inventory)
            new_price = mms_price[mm_id][-1] + np.random.normal(0, price_volatility)
            mms_price[mm_id].append(new_price)
            current_pnl = new_inventory * (new_price - trade_price)
            mms_pnl[mm_id].append(current_pnl)
        else:
            mms_inventory[mm_id].append(mms_inventory[mm_id][-1])
            new_price = mms_price[mm_id][-1] + np.random.normal(0, price_volatility)
            mms_price[mm_id].append(new_price)
            mms_pnl[mm_id].append(mms_pnl[mm_id][-1])
    trade_log.append((i, direction, "Accepted", chosen_mm_id, trade_price, new_inventory))

# Convert trade log to DataFrame
df = pd.DataFrame(trade_log, columns=["Trade #", "Direction", "Status", "Chosen MM", "Trade Price", "Inventory"])
print(df)

# Plot inventory and PnL for each MM
plt.figure(figsize=(14, 8))

for mm_id in range(num_mms):
    plt.subplot(2, num_mms, mm_id + 1)
    plt.plot(mms_inventory[mm_id], label=f"MM {mm_id} Inventory")
    plt.axhline(inventory_limit, color='red', linestyle='--')
    plt.axhline(-inventory_limit, color='red', linestyle='--')
    plt.title(f"MM {mm_id} Inventory")
    plt.legend()

    plt.subplot(2, num_mms, mm_id + 1 + num_mms)
    plt.plot(mms_pnl[mm_id], label=f"MM {mm_id} PnL", color='green')
    plt.title(f"MM {mm_id} Unrealized PnL")
    plt.legend()

plt.tight_layout()
plt.show()
