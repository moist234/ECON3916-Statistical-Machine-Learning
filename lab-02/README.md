# 📉 The Illusion of Growth & the Composition Effect

## Objective
This project examines long-run U.S. wage stagnation by correcting nominal wage data for inflation and identifying statistical distortions that can misrepresent true labor market dynamics.

---

## Methodology
- Built a Python data pipeline to ingest **live macroeconomic time series** from the Federal Reserve Economic Data (FRED) API.
- Retrieved **nominal wage data (AHETPI)** and **Consumer Price Index (CPI)** series to compute inflation-adjusted **real wages**.
- Identified an anomalous spike in real wages during 2020 that was inconsistent with underlying labor market conditions.
- Incorporated the **Employment Cost Index (ECI)** to control for changes in workforce composition and isolate true wage growth.
- Visualized nominal wages, real wages, and corrected wage measures to highlight differences between perceived and actual economic outcomes.

---

## Key Findings — The Pandemic Paradox
The analysis reveals a persistent pattern of **flat real wage growth** in the United States over the past five decades, despite steady increases in nominal wages. This divergence illustrates the phenomenon of **money illusion**, where rising paychecks mask stagnant purchasing power.

A notable exception appears during the early stages of the COVID-19 pandemic, when real wages spiked sharply in 2020. However, further analysis shows this surge to be a **statistical artifact rather than genuine wage growth**. By controlling for workforce composition using the Employment Cost Index, the project demonstrates that the apparent wage boom was driven by the disproportionate exit of lower-wage workers from employment, artificially inflating average wages.

This “**Pandemic Paradox**” underscores the importance of careful measurement in macroeconomic analysis and highlights how aggregate statistics can mislead when underlying population dynamics shift rapidly.

---

## Economic Insight
This project emphasizes that meaningful economic analysis requires moving beyond surface-level indicators. Correcting for inflation and composition effects is essential for accurately interpreting labor market trends and avoiding false conclusions about economic progress.
