# 🧮 Excessive Inventory Risk — Single Market Maker

This simulation models a single market maker in a quote-driven market, handling random client buy/sell orders while enforcing a hard inventory limit (±20 units).

---

![Simulation]![excessive_inventory_risk](https://github.com/user-attachments/assets/b9736ef7-714d-4ecf-a5ca-3185e69b6340)


---

## 🧠 What It Shows

- Inventory fluctuates as trades occur.
- Trades are rejected when inventory breaches limits.
- Unrealized PnL changes based on market price movements and position.

---

## ⚙️ How It Works

- Each trade randomly increases or decreases inventory.
- If new inventory exceeds the risk threshold, the trade is rejected.
- Price follows a random walk.
- PnL is calculated as:  
  `PnL = Inventory × (New Price − Trade Price)`

---
