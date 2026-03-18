# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective

Executed a multivariate hedonic pricing model on 2026 California real estate data to empirically demonstrate the Frisch-Waugh-Lovell (FWL) theorem, proving that manual residual partialling produces coefficients mathematically identical to full multivariate OLS — and diagnosing the severe omitted variable bias introduced when controlling variables are excluded from the specification.

---

## Data

**Source:** Zillow synthetic dataset — 2026 California residential real estate  
**Outcome variable:** `Sale_Price` (USD)  
**Regressors:** `Property_Age` (years), `Distance_to_Tech_Hub` (miles)  
**Stack:** Python 3.10+, `pandas`, `statsmodels.formula.api`, `matplotlib`

---

## Methodology

**Stage 1 — Baseline Multivariate OLS**
- Specified and estimated a hedonic pricing model of the form:

  `Sale_Price ~ β₀ + β₁·Property_Age + β₂·Distance_to_Tech_Hub + ε`

- Recovered full-model OLS coefficients using `statsmodels.formula.api.ols`, establishing the benchmark estimates against which the FWL proof is validated.

**Stage 2 — Manual Residual Extraction (FWL Partialling)**
- Regressed `Property_Age` on `Distance_to_Tech_Hub` to isolate the component of property age that is *orthogonal* to tech hub proximity — stripping out all shared covariance between the two regressors.
- Extracted the residuals from this auxiliary regression, representing the *net* variation in `Property_Age` unexplained by location.
- Regressed `Sale_Price` on those residuals alone (a univariate OLS on the partialled regressor), recovering the isolated marginal effect of property age under strict ceteris paribus conditions.

**Stage 3 — Coefficient Verification**
- Compared the FWL-derived coefficient on `Property_Age` to the corresponding estimate from the full multivariate model.
- Confirmed exact numerical equivalence to floating-point precision, constituting a formal empirical proof of the FWL theorem.

---

## Key Findings

**Omitted Variable Bias (OVB) — Magnitude and Direction**

When `Distance_to_Tech_Hub` was omitted from the specification, the coefficient on `Property_Age` was significantly inflated in absolute magnitude. The bias arose because older properties in this dataset are systematically located farther from tech employment centers — a structural correlation embedded in California's development geography. In a bivariate model, the age coefficient silently absorbed the negative location premium, misattributing a distance penalty to physical depreciation. The direction of the OVB was exactly as theory predicts: the omitted variable (`Distance_to_Tech_Hub`) is negatively correlated with `Sale_Price` and positively correlated with `Property_Age`, producing a downward bias in the bivariate age estimate.

**FWL Correction — Algorithmic Ceteris Paribus**

The FWL theorem resolves this by enforcing orthogonality. By regressing `Property_Age` on `Distance_to_Tech_Hub` first and working exclusively with the resulting residuals, the procedure mechanically removes the collinear component before estimating the effect of age on price. The residuals carry zero correlation with `Distance_to_Tech_Hub` by construction — meaning the final regression on `Sale_Price` cannot conflate the two effects. The resulting coefficient is a clean, uncontaminated estimate of the age–price relationship, holding location fixed. The exact match to the multivariate coefficient is not a numerical coincidence; it is a direct consequence of the Frisch-Waugh-Lovell theorem's algebraic guarantee, which holds for any OLS estimator operating on a correctly specified design matrix.

> **Takeaway:** Multivariate OLS does not simply "add more variables" — it performs this partialling operation simultaneously across all regressors. The FWL theorem makes that latent mechanism explicit, and this lab proves it holds empirically to machine precision.

---

## Technical Environment

| Component | Version |
|---|---|
| Python | 3.10+ |
| pandas | — |
| statsmodels | — |
| matplotlib | — |

---

*Econ 3916 — Econometrics Lab · Northeastern University · 2026*
