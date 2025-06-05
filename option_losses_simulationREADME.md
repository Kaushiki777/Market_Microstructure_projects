
# 📈 Options Market Maker Simulation

This simulation models the **profit dynamics** between retail traders and a **market maker** in a call options market.

---

## 💡 Overview

* 1000 **retail traders** each buy a **call option** on the same underlying asset.
* A **market maker** sells these options, collecting premiums.
* The stock price follows a **random walk** over 10 days.
* At expiry, each option is evaluated, and payouts are made if **in-the-money**.

---

## 🧮 What It Demonstrates

* **Retail traders** have limited upside and frequent losses (most options expire worthless).
* **Market makers** earn consistent profits through:

  * Collecting option premiums
  * Paying out only on statistically rare outcomes
* This reflects real-world data: **91%+ of retail options expire at a loss**.

---

## 📊 Output Metrics

* **Market Maker Total Profit**
* **Average Retail Trader Profit/Loss**
* **Percentage of Retail Traders Who Win**
* **Histogram** of retail PnL distribution

---

## 🔧 Key Parameters

| Parameter      | Value         |
| -------------- | ------------- |
| Traders        | 1000          |
| Option Type    | European Call |
| Strike Price   | ₹100          |
| Premium        | ₹5            |
| Time to Expiry | 10 days       |
| Volatility     | 2% daily      |
| Initial Price  | ₹100          |

---
