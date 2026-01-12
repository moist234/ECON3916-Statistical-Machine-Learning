# 🌍 Global Purchasing Power Parity Analysis via the Big Mac Index

## Objective
This project applies the **Law of One Price** to international data by using the Big Mac Index as a proxy for testing **Purchasing Power Parity (PPP)** across currencies.

---

## Methodology
- Constructed a cross-country dataset using **The Economist’s 2015 Big Mac Index** data.
- Ingested raw price and exchange rate data into Python using manually defined dictionaries.
- Calculated **implied PPP exchange rates** based on relative Big Mac prices.
- Computed **currency misalignment** by comparing implied PPP rates to observed market exchange rates.
- Classified currencies as **overvalued** or **undervalued** relative to the U.S. dollar.

---

## Key Findings
The analysis reveals meaningful deviations from Purchasing Power Parity across countries. For example:

- The **Norwegian Krone** was found to be **overvalued by approximately _X_%** relative to the U.S. dollar, suggesting that goods priced in Norway were more expensive than implied by PPP.
- Other currencies exhibited varying degrees of **undervaluation**, indicating potential price level differences that may persist due to trade barriers, non-tradable goods, or market frictions.

These deviations highlight the practical limitations of the Law of One Price in real-world markets and suggest that **arbitrage opportunities**, while theoretically present, may be constrained by transaction costs, regulation, and structural economic differences.

---

## Economic Insight
This project demonstrates how a simple consumer good can be used to operationalize a core macroeconomic theory. While Purchasing Power Parity provides a useful long-run benchmark, the observed mispricings reinforce the importance of institutional, geographic, and behavioral factors in determining exchange rates.
