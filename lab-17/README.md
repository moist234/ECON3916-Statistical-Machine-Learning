NY Fed Yield Curve Recession Model Replication
Objective: Replicated the Federal Reserve Bank of New York's yield curve recession forecasting model using logistic regression on live FRED macroeconomic data to predict NBER-defined recessions 12 months ahead.
Methodology:

Pulled T10Y3M (10Y–3M Treasury yield spread) and USREC (NBER recession indicator) from FRED via API, resampled to monthly frequency, and applied a 12-month lag to align with the NY Fed's forward-looking framework
Demonstrated Linear Probability Model (OLS) failure modes on binary outcomes, including predicted probabilities outside [0, 1]
Fitted a logistic regression (sklearn) to estimate the S-curve relationship between yield spread and recession probability
Extracted the yield spread odds ratio with 95% confidence intervals via statsmodels Logit
Generated a full recession probability time series (1970–present) and evaluated model performance using time-series cross-validation (TimeSeriesSplit) against a naive baseline
Extended the one-predictor model with a second FRED variable (UNRATE) and compared odds ratios and cross-validated accuracy across both specifications

Key Findings: The logistic model successfully replicates the NY Fed's published recession probability series, with the yield spread odds ratio confirming that curve steepening significantly reduces near-term recession risk. The contested 2022–2024 inversion — the longest since the 1980s — drove predicted recession probability to ~40%, the highest in the sample outside actual recessions, yet no NBER recession materialized, highlighting the distinction between elevated probabilistic risk and realized outcomes. Both the one- and two-predictor models outperformed the naive baseline in time-series cross-validation.