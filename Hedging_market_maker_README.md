# 📈 Hedging Market Maker Inventory Risk in a Quote-Driven Market

This simulation models how a **market maker (MM)** operating in a **quote-driven market** actively manages **excessive inventory risk** by executing **hedging trades** once a predefined threshold is breached. The MM adapts to trade flow, inventory constraints, and market volatility, balancing execution with risk control.

---

## 🎯 Objective

To demonstrate how **hedging strategies** help a market maker:
- Stay within inventory risk limits
- Minimize exposure during large client imbalances
- Incorporate cost of hedging into profit & loss (PnL)
---

## 🧠 Key Concepts

- **Quote-Driven Market**: MM sets bid/ask prices and absorbs incoming buy/sell flow.
- **Inventory Risk**: Accumulation of directional exposure leads to significant PnL volatility.
- **Hedging Strategy**: When absolute inventory exceeds a threshold, MM executes hedge trades to reduce risk.
- **Unrealized PnL**: Tracks mark-to-market gain/loss post-trade including hedge costs.
---

## 🔧 Parameters & Controls

| Parameter | Description | Value |
|----------|-------------|--------|
| `num_trades` | Number of client trades simulated | 100 |
| `inventory_limit` | Hard cap on inventory (trade rejected if breached) | 20 units |
| `hedge_threshold` | Hedge initiates when inventory exceeds this | 10 units |
| `hedge_cost_per_unit` | Cost incurred per unit hedged | 0.01 |
| `spread` | MM earns spread on trades (fixed) | 0.05 |
| `price_volatility` | Random walk volatility of market price | 0.3 |

---

## 🧾 Outputs

The simulation tracks and visualizes:

1. **Inventory over time**  
   Shows accepted/rejected trades and hedging behavior near threshold.

2. **Unrealized PnL over time**  
   Reflects trade gain/loss post price change minus hedge cost.

3. **Cumulative hedging actions**  
   Indicates how much inventory the MM has offloaded for risk control.
---

## 📊 Visualization

- **Red dashed lines**: Inventory limits  
- **Orange dashed lines**: Hedge trigger levels  
- **PnL chart**: Captures volatility + hedging impact  
- **Hedging chart**: Shows cumulative hedge volume executed
---

## 🧠 Insights & Takeaways

- Market makers **cannot passively absorb client flow** without risk.
- **Dynamic hedging** acts as a circuit breaker against large inventory swings.
- While **hedging reduces directional risk**, it incurs real cost and impacts net profitability.
- This project simulates a **real-world microstructure tension** between liquidity provision and inventory risk.
---

## 🏁 Next Extensions (WIP)

- Dynamic spread adjustment based on inventory
- Multi-agent simulation with competing MMs
- Inclusion of latency and adverse selection models
---
