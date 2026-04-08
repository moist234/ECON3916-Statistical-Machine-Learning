# Tree-Based Models — Random Forests

**Objective:** Evaluate the predictive performance of ensemble tree-based methods against linear baselines on the California Housing dataset, and assess the practical tradeoffs between accuracy, interpretability, and tuning complexity.

**Methodology:**
- Loaded and split California Housing data (20,640 observations, 8 features) into 80/20 train/test sets
- Fit an unrestricted Decision Tree, Ridge Regression, and a 100-tree Random Forest regressor and compared Train/Test RMSE and R²
- Tuned Random Forest hyperparameters (n_estimators, max_depth, max_features) via 5-fold GridSearchCV
- Extracted MDI feature importance from training and permutation importance from the test set to assess and compare feature rankings
- Constructed a binary classification target (above/below median price) and compared a 200-tree RF classifier against logistic regression using AUC-ROC

**Key Findings:**
- Random Forest (default) achieved Test R² = 0.8049 vs Ridge R² = 0.5759, confirming that housing price patterns are substantially non-linear
- GridSearchCV tuning (best: max_depth=None, max_features=sqrt, n_estimators=200) improved Test R² marginally to 0.8158, indicating default settings were near-optimal
- MDI and permutation importance agreed that MedInc is the dominant predictor, though MDI overstated the importance of high-cardinality geographic features (Latitude, Longitude)
- RF classifier outperformed logistic regression on AUC (0.9611 vs 0.9087), though logistic regression remains preferable for production deployment given its interpretability and lower maintenance cost