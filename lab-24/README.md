Causal ML — Double Machine Learning for 401(k) Policy Evaluation
Objective: Estimate the causal effect of 401(k) eligibility on household net financial assets using Double Machine Learning to eliminate regularization bias from high-dimensional covariate control.
Methodology:

Demonstrated regularization bias by showing LASSO shrinks the treatment coefficient toward zero when applied naively to a simulated DGP with TRUE ATE of $5,000
Built a DoubleML Partially Linear Regression model using Random Forest nuisance learners for both the outcome and treatment equations
Applied 5-fold cross-fitting on the 401(k) dataset to produce a debiased ATE estimate with valid confidence intervals
Conducted CATE analysis by splitting the sample into income quartiles and fitting separate DML models per subgroup
Ran sensitivity analysis to assess robustness of the ATE to potential unmeasured confounders

Key Findings: DML recovered an ATE meaningfully higher than the naive LASSO estimate, confirming that regularization bias is a real concern in causal inference with many controls. The CATE analysis revealed that the 401(k) eligibility effect is larger for higher-income quartiles, consistent with higher-income households having greater capacity to direct additional savings into retirement accounts. The sensitivity analysis confirmed the estimate is robust to plausible unmeasured confounders, supporting the credibility of the causal interpretation.