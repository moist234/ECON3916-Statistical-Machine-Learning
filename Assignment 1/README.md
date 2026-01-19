# The Cost of Living Crisis: A Data-Driven Analysis

## The Problem
The official Consumer Price Index (CPI) is a national average built for an “average consumer” that doesn’t really exist. As a student in Boston, my expenses are concentrated in categories like rent, tuition, and food away from home—costs that can rise differently (and often faster) than the national CPI suggests.

## Methodology (Python, APIs, and Index Theory)
- **Data Source:** Federal Reserve Economic Data (FRED) via the `fredapi` Python library.
- **Proxies:** Because FRED does not track specific brands (e.g., Chipotle/Spotify), I used CPI category proxies (tuition, rent, streaming, food away from home) and compared them to the official CPI benchmark.
- **Index Theory (Laspeyres):** CPI is constructed as a weighted “basket” index (Laspeyres-style). I replicated that idea by building a custom **Student Price Index (Student SPI)** with weights that better reflect student spending.
- **Normalization:** CPI series can have different base years. To compare trends fairly, I re-indexed all series to a common baseline: **2016 = 100**.

## Key Findings
- My custom **Student SPI** diverges from the **National CPI** by approximately **[X]%** over the period **2016–2024**, showing that student-relevant costs increased faster than the national benchmark.
- Adding regional context, **Boston CPI** shows **[higher/lower]** inflation than the national CPI over the same window, suggesting the national average can hide local pressure.
- The largest drivers of the gap were **[Tuition / Rent / Food Away From Home / Streaming]**, which outpaced the national CPI trend after normalization.

## Visual Results
- **Figure 1:** Normalized category trends (2016 = 100) for tuition, rent, streaming, food away from home, and national CPI.
- **Figure 2:** Student SPI vs National CPI with the inflation gap highlighted.
- **Figure 3:** “Bad chart” demonstration showing why comparing raw indices with different base years is misleading.
- **Figure 4:** Boston CPI vs National CPI vs Student SPI (regional + personal reality check).

## Next Steps
- Replace “reasonable” weights with survey-based estimates or actual spending data.
- Extend the framework to additional student costs (transportation, textbooks, healthcare).
- Compare multiple metro areas to quantify how much regional inflation differs from national averages.
