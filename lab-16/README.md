High-Dimensional GDP Growth Forecasting with Lasso and Ridge Regularization
Objective: Demonstrate and correct the OLS failure mode in high-dimensional cross-country regression by applying cross-validated Lasso and Ridge regularization to forecast 5-year average real GDP per capita growth across 120+ countries using World Bank development indicators.

Methodology

Data acquisition: Downloaded 36 World Development Indicators spanning trade, macroeconomics, education, infrastructure, health, finance, natural resources, agriculture, and governance via the wbgapi Python API, covering 2013–2019 (pre-COVID) for ~150 countries
Dataset construction: Collapsed seven annual observations per country into a single cross-sectional row by time-averaging; dropped countries and indicators with more than 40% missing values; imputed remaining gaps with cross-country medians to avoid listwise deletion bias
OLS baseline: Fit plain OLS on standardized features to establish the overfitting benchmark; recorded both training and test R² to quantify the train–test gap at a predictor-to-observation ratio approaching 0.5
Regularization: Applied RidgeCV and LassoCV with 5-fold cross-validation over a log-spaced lambda grid to select the optimal penalty; standardized features using a scaler fit exclusively on training data to prevent data leakage
Lasso Path analysis: Computed the full coefficient trajectory across 100 penalty values using sklearn.linear_model.lasso_path to identify which indicators enter the model first as regularization relaxes


Key Findings
OLS achieved a training R² near 1.0 but substantially lower test R², confirming the variance explosion predicted by theory when p/n is large — the model memorized country-specific noise rather than learning generalizable patterns. Both RidgeCV and LassoCV meaningfully narrowed the train–test gap. Lasso produced a sparse solution, retaining roughly 5–10 predictors from a set of 30+, suggesting that most WDI indicators carry redundant information once the strongest proxies are included. The Lasso Path revealed a clear hierarchy: a small cluster of indicators — concentrated in macroeconomic stability, governance quality, and infrastructure access — entered the model at high penalty values, indicating robustness to what else is controlled for. Indicators that entered only at low lambda values are better interpreted as conditionally redundant rather than economically irrelevant, as their information is already captured by earlier-entering correlated predictors.

Tech Stack
Python · wbgapi · scikit-learn · pandas · numpy · matplotlib