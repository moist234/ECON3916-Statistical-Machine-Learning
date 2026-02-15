## Audit 02: Deconstructing Statistical Lies

**Role:** Data Quality Auditor, Pareto Ventures  
**Objective:** Identify where “perfect metrics” hide risk by auditing distributions, base rates, and selection bias.

---

### 1) Latency Skew — The Mean Is a Vanity Metric
**Context:** NebulaCloud reported a mean latency of ~35ms.  
**Method:** Simulated 1,000 requests with a heavy-tailed distribution (980 normal, 20 extreme spikes). Compared Standard Deviation (SD) vs. Median Absolute Deviation (MAD) and tail percentiles.

**Findings**
- Median latency stayed low (typical user experience stable).
- SD exploded due to a small number of extreme spikes.
- p99 and p99.9 revealed severe tail risk (multi-second delays).

**Insight**
- **Means hide tails.** In skewed systems, SD and p99+ expose reliability risk.
- **MAD is robust** to outliers and better reflects “normal” variability.

**Takeaway for investors:** Reliability claims must include **tail metrics (p95/p99)** and robust stats, not just averages.

---

### 2) False Positives — Accuracy Without Base Rates Is Misleading
**Context:** IntegrityAI claimed 98% accuracy (98% sensitivity, 98% specificity).  
**Method:** Bayesian audit to compute \( P(\text{Cheater} \mid \text{Flagged}) \) across different cheating base rates.

**Scenarios**
- Bootcamp (50% base rate) → Posterior ≈ 98%
- Econ class (5% base rate) → Posterior ≈ 72%
- Honors seminar (0.1% base rate) → Posterior ≈ 5%

**Insight**
- High accuracy ≠ reliable flags when events are rare.
- In low-prevalence settings, **most flags become false positives**.

**Takeaway for investors:** Always audit **base rates**. “98% accurate” can still produce unusable products.

---

### 3) Survivorship Bias — The “Listed Coins” Illusion
**Context:** Crypto platforms highlight only successful tokens; ~98% fail.  
**Method:** Simulated 10,000 token launches using a Pareto (power-law) distribution for peak market cap.  
Created:
- `df_all` → full graveyard
- `df_survivors` → top 1% only

**Findings**
- Mean market cap for survivors was multiple times larger than the full dataset.
- The “top tokens” view dramatically inflated perceived performance.

**Insight**
- **Deleting failures rewrites reality.**
- Power-law markets (crypto, VC, social platforms) are especially vulnerable to survivorship bias.

**Takeaway for investors:** Always request **full cohort data**, not just winners.

---

## Audit Framework Applied
Across all three cases:

| Risk Pattern | What Companies Show | What the Audit Reveals |
|---|---|---|
| Latency | Mean performance | Tail failures (p99+) |
| AI Accuracy | Aggregate accuracy | Base-rate false positives |
| Market Performance | Winners only | Survivorship bias |

---

## Final Conclusion
The common statistical lie is **overreliance on averages without context**.

Robust auditing requires:
- Distributional thinking (tails > means)
- Bayesian reasoning (base rates matter)
- Cohort completeness (include failures)

**Investor principle:**  
> If a metric looks “perfect,” inspect the distribution, the denominator, and the deleted data.
