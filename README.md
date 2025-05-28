# Market_Microstructure_projects

Welcome to the Market Microstructure project repository! Here I am building Python-based simulations and models designed to deeply explore the inner workings of modern financial markets — particularly in the context of quote-driven markets, dealer behavior, and liquidity provision for now.

I am currently building this repository to support my academic and industry-level understanding of how to manage risk, compete, and hedge under real-world microstructure dynamics. I also simultaneously try to apply the logics to different asset classes and transaction mechanisms.

---

## 📁 Current Projects

### 1. 🧮 Excessive Inventory Risk (Single Market Maker)
A simulation of a single market maker managing client flow while enforcing hard inventory limits. Illustrates:
- How trades affect MM inventory and unrealized PnL
- Rejection of trades due to risk constraints
- Volatility impact on profit

### 2. ⚔️ Excessive Inventory Risk with Multiple Market Makers
A multi-agent version where multiple MMs compete for client orders:
- Dynamic quote-based competition
- Best-price selection logic
- Per-MM inventory and PnL visualization

### 3. 🛡️ Excessive Inventory Risk with Hedging Logics
Adds the logic of **hedging** to manage excessive inventory risk:
- MM triggers hedges when inventory breaches threshold
- Tracks hedge costs and their effect on PnL
- Shows smoother risk profiles using hedging strategies

---

## 🔬 Future Plans

As I progress through the subject, I plan on expanding this repository to include:

### 🔄 Order-Driven Market Simulations
- Continuous double auction (CDA) mechanics
- Limit order book construction and event-based order flow
- Market depth, bid-ask spread evolution, and sniping behavior

### ⏱️ Latency Arbitrage and Adverse Selection
- Model fast vs slow traders
- Simulate toxic flow detection
- Adverse selection cost analysis for passive liquidity providers

### 🧠 Smart MM Strategy Development
- Adaptive quoting logic using statistical edge
- Reinforcement learning agents for inventory control
- Skewing quotes based on inventory and client flow predictions

### 🧪 Transaction Mechanism Experiments
- Book-building simulations for IPO demand curves
- Dutch and uniform-price auction pricing logic
- OTC price discovery under opacity and information asymmetry

### 📊 Analytics and Metrics
- Real-time dashboards for MM performance
- Heatmaps for spread and volume concentration
- Execution quality vs quote aggressiveness trade-offs

---

## 🚀 Getting Started!!

