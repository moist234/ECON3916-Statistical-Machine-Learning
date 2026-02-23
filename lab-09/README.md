Recovering Experimental Truths via Propensity Score Matching
Project Overview

This lab reconstructs causal validity in observational data by modeling and correcting for selection bias using Propensity Score Matching (PSM) on the observational subset of the Lalonde dataset. The project demonstrates how rigorous econometric design can recover experimental-grade insights from non-randomized environments.

Objective

Repair observational failure by isolating causal signal from selection-driven noise through statistically principled matching techniques.

Methodology

Modeled selection bias using logistic regression to estimate treatment assignment probabilities

Computed individual-level propensity scores based on observable covariates

Applied Nearest Neighbor matching to construct balanced treated and control cohorts

Reduced covariate imbalance and simulated randomized comparability

Implemented the workflow using Python, Pandas, and Scikit-Learn

Key Findings

Naive observational estimate: −$15,204 (severely biased due to non-random selection)

Post-matching estimate: ≈ +$1,800 treatment effect

Result: Matching framework successfully recovered the experimentally validated causal lift in earnings

This analysis highlights how selection bias can invert causal conclusions and demonstrates that properly specified matching architectures can restore credible treatment effect estimation in real-world, non-randomized data environments.
