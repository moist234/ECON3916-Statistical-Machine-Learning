# AI Capex Diagnostic Modeling

## Objective
Diagnose and correct structural failures in an OLS regression framework predicting AI software revenue from capital expenditure and deployment data, applying robust econometric techniques to recover valid inference under model misspecification.

---

## Data
**2026 Nvidia AI Capital Expenditure and Deployment Dataset** — contains capital expenditure tiers, deployment metrics, and AI software revenue figures across infrastructure segments.

---

## Methodology

- **Baseline OLS Estimation** — Specified and estimated a naive OLS model regressing AI software revenue on Nvidia capital expenditure and deployment metrics; evaluated initial coefficient estimates and p-values.

- **Heteroscedasticity Diagnostics** — Conducted residual analysis using fitted-value plots and formal diagnostic tests to detect non-constant error variance; identified a pronounced fan-shaped expansion of residuals concentrated at high capital expenditure tiers.

- **Multicollinearity Assessment** — Computed Variance Inflation Factors (VIFs) across regressors to identify collinear relationships among deployment and expenditure predictors that could distort standard error estimates.

- **HC3 Robust Standard Error Correction** — Re-estimated the model using Heteroscedasticity-Consistent (HC3) standard errors via `statsmodels`, correcting for the identified error structure without altering point estimates.

- **Inference Comparison** — Benchmarked naive OLS p-values against HC3-corrected p-values to quantify the degree of false statistical confidence introduced by model misspecification.

**Tools:** Python · pandas · statsmodels · matplotlib · seaborn

---

## Key Findings

The naive OLS model exhibited **severe heteroscedasticity**, with residual variance expanding systematically at higher capital expenditure tiers — a pattern consistent with scale-dependent noise common in infrastructure investment data. This structural violation produced **artificially compressed standard errors and inflated t-statistics**, causing deployment metrics to appear more statistically significant than the data could legitimately support.

Applying **HC3-robust standard errors** appropriately widened the confidence intervals and adjusted p-values upward, revealing the true degree of uncertainty in the model's coefficient estimates. The correction did not alter the directional relationships between variables, but materially changed the inferential conclusions — underscoring that valid hypothesis testing in heteroscedastic environments requires robust estimation by default, not as an afterthought.

> **Takeaway:** In high-variance capital expenditure environments, naive OLS inference is not just imprecise — it is systematically misleading. Robust standard errors are a necessary condition for credible econometric analysis of AI infrastructure data.

---

*Lab conducted as part of ECON3916 · Northeastern University · Spring 2026*
