# ⚔️ Multiple Market Makers — Inventory & PnL Simulation

This simulation models a quote-driven market with **three competing market makers (MMs)**. Each MM independently quotes prices and manages risk while serving incoming client trades. Clients always choose the best available price, simulating a realistic competitive liquidity environment.

---
![Simulation Output]
(![multiple_market_makers](https://github.com/user-attachments/assets/fa2881f3-b95d-45bc-98a4-3af42a73c273))


---

## 💡 Core Idea

- MMs **quote bid/ask prices** using a fixed spread around their local view of the price.
- Incoming **buy/sell orders** are directed to the MM offering the best price.
- Inventory and unrealized PnL are tracked **separately** for each MM.
- Trades are **rejected** if they would breach an MM’s inventory risk limit (±20 units).

---

## 📊 What the Simulation Shows

**Top Row (Inventory Plots):**
- Tracks how each MM’s inventory fluctuates as they fill trades.
- Red dashed lines = hard inventory limits.

**Bottom Row (Unrealized PnL Plots):**
- Reflects how inventory exposure and market volatility drive unrealized profits or losses.
- Captures per-MM risk based on their trade flow and fill quality.

---

## 🧠 Logic Summary

- **Client direction** is randomly chosen (buy or sell).
- Each MM quotes:  
  `quote_price = last_price ± spread`
- **Best quote wins** the trade:
  - If client sells → MM with **highest bid** wins.
  - If client buys → MM with **lowest ask** wins.
- The winning MM updates inventory, price, and PnL.
- Others only update price.
- PnL = `Inventory × (New Market Price - Trade Price)`

---
