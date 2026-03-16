# Architecting the Prediction Engine

## Objective
Architect a multivariate OLS prediction engine using the Patsy Formula API to forecast real estate valuations from the 2026 Zillow ZHVI Micro dataset, and rigorously evaluate out-of-sample performance through loss minimization and financial error quantification.

---

## Dataset
**Zillow ZHVI 2026 Micro Dataset** — Cross-sectional modern real estate market data capturing property-level valuations across U.S. micro-markets, with structural features as predictors of home value.

---

## Methodology

- **Environment Initialization** — Configured a reproducible analytical stack using `pandas`, `numpy`, `statsmodels`, and `matplotlib`, with `statsmodels.formula.api` (smf) as the Patsy Formula interface for R-style model specification.

- **Data Ingestion & EDA** — Ingested the Zillow dataset directly into a pandas DataFrame via external URL. Performed rapid Exploratory Data Analysis on the target variable `Home_Value` to characterize distributional scale, variance, and potential outlier exposure.

- **OLS Architecture via Patsy Formula** — Defined the regression architecture as a Patsy formula string (`Home_Value ~ Square_Footage + Property_Age + Distance_to_Transit`), delegating constant intercept injection and design matrix construction to the formula engine — eliminating manual orthogonal matrix handling.

- **Model Fitting & Diagnostic Extraction** — Fit the OLS model using `.fit()` and interrogated the `.summary()` output for coefficient estimates, t-statistics, p-values, and R² to validate economic intuition (e.g., depreciation effects from property age, accessibility premiums from transit proximity).

- **Predictive Evaluation via RMSE** — Transitioned from explanatory inference to predictive engineering by computing Root Mean Squared Error (RMSE) in raw U.S. dollar terms, grounding model performance in directly interpretable financial error units.

- **Residual Forensics Dashboard** — Built an interactive Plotly residual scatter plot (fitted values vs. residuals) with outlier flagging at ±2σ in crimson, enabling visual detection of heteroscedasticity and structural breaks in the prediction surface.

---

## Key Findings

The OLS engine successfully learned systematic relationships between structural property features and market valuations, with coefficient signs consistent with economic theory. The RMSE — expressed in actual U.S. dollars — provided a precise, business-interpretable measure of algorithmic prediction error, enabling direct quantification of financial risk embedded in the model's forecasting margin. Residual forensics surfaced the distribution of prediction errors across the fitted value range, flagging observations where the model's assumptions may be locally violated.

---

## Tech Stack
`Python` · `pandas` · `numpy` · `statsmodels (Patsy Formula API)` · `plotly`
