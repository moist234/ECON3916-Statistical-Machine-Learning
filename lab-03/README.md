# Lab 3: The Illusion of Growth & The Power of Benchmarking  
**Visualizing Development with WBGAPI**

---

## Objective

I built a Python-based data visualization pipeline to analyze Guatemala’s economic development using live data from the **World Bank API**. The goal of this lab was to demonstrate how economic trends can be misleading when viewed in isolation, and how **benchmarking against global reference groups** (Upper Middle Income economies and the world average) reveals a more accurate and nuanced story of development.

This lab emphasizes **comparative thinking**: a line going “up” does not necessarily imply success without proper context.

---

## Tech Stack

- **Python**
- **wbgapi** (World Bank API)
- **pandas**
- **matplotlib**
- **seaborn**

---

## Methodology

1. **API-Based Data Ingestion (Manual, No AI)**  
   - Connected directly to the World Bank API using `wbgapi`.
   - Pulled multi-indicator, multi-economy data for Guatemala (GTM), Upper Middle Income (UMC), and the World (WLD) from 2000–2024.
   - Manually handled the wide-to-long transformation and cleaned the MultiIndex structure into a usable panel dataset.

2. **Indicator Mapping & Cleaning**  
   - Converted cryptic World Bank indicator codes into readable economic variables (GDP, inflation, labor, trade, fiscal policy).
   - Extracted Guatemala-specific data for deeper country-level analysis.

3. **Derived Economic Metrics**  
   - Computed higher-level indicators by hand:
     - Natural rate of unemployment (5-year moving average)
     - Productivity (GDP per worker)
     - Net capital outflow (exports minus imports)
     - Fiscal balance (tax revenue minus government spending)

4. **Narrative-Driven Visualization**  
   - Designed a sequence of plots to show how visualization choices affect interpretation:
     - “Narrow view” charts showing Guatemala alone
     - Benchmark charts adding UMC and World comparisons
     - Vertical and horizontal subplot layouts to compare growth vs. living standards
   - Built a final **2×3 Executive Dashboard** synthesizing wealth, labor, inflation, savings, trade, and fiscal policy.

5. **Data Literacy & Ethics**  
   - Explicitly demonstrated misleading techniques (truncated axes, pie charts for rates) to highlight how charts can manipulate perception.

---

## Key Findings

- **The Illusion of Growth:**  
  Guatemala’s GDP and GDP per capita show steady upward trends when plotted alone, creating the appearance of strong economic progress.

- **The Benchmark Reality:**  
  Once Upper Middle Income and World averages are added, Guatemala’s growth is revealed to be **relative stagnation**—the country is growing, but not catching up.

- **Growth vs. Living Standards:**  
  Total GDP expansion does not translate proportionally into improvements in GDP per capita, underscoring the importance of population-adjusted metrics.

- **Structural Constraints:**  
  Persistent gaps between savings and investment, exports and imports, and tax revenue and government spending point to long-run structural limitations rather than short-term volatility.

- **Visualization as Argument:**  
  The same data can tell radically different stories depending on scale, benchmarks, and chart design—making data literacy as important as technical skill.

---

## Takeaway

This lab shows that **economic storytelling is inseparable from comparison**. Development cannot be assessed in isolation; benchmarks transform “growth” into insight. The final executive dashboard demonstrates how multiple macroeconomic dimensions interact to shape long-run outcomes—and how poor visualization choices can distort that reality.
