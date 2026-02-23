Hypothesis Testing & Causal Evidence Architecture
Project Overview

This lab operationalizes the scientific method within a computational framework to evaluate causal claims using the Lalonde (1986) randomized job training dataset.

Rather than treating statistical estimation as an endpoint, the project reframes inference as an act of falsification — rigorously attempting to disprove a null hypothesis through structured contradiction. The core question:

Does participation in job training produce a measurable, statistically defensible increase in real earnings?

The result is a reproducible causal evidence pipeline designed to adjudicate between competing narratives of economic impact.

Objective: From Estimation to Falsification

Most data analysis workflows stop at point estimates. This project pivots from “What is the average effect?” to “Can we rigorously reject the hypothesis that the effect is zero?”

The objective was to construct a formal hypothesis testing architecture that:

Quantifies the Signal-to-Noise Ratio of the estimated treatment effect

Tests robustness under both parametric and distribution-agnostic assumptions

Controls for Type I error (false positives)

Produces statistically defensible causal evidence

This shift represents a philosophical move from descriptive accounting to epistemic discipline — from measuring differences to actively attempting to falsify them.

Technical Approach

The analysis was implemented in Python using SciPy and standard scientific computing libraries.

Parametric Test (Welch’s T-Test)

Estimated the Average Treatment Effect (ATE) as the difference in mean post-treatment earnings between treated and control groups

Applied Welch’s T-Test to account for unequal variances

Interpreted the test statistic explicitly as a Signal-to-Noise Ratio

Controlled for Type I error using a predefined significance threshold (α = 0.05)

Non-Parametric Validation (Permutation Test)

Executed 10,000 random label permutations

Constructed an empirical null distribution

Compared the observed treatment effect against the simulated distribution

Validated inference robustness against non-normal earnings distributions

This dual-framework architecture ensures the inference does not rely solely on normality assumptions, reinforcing the credibility of the rejection decision.

Key Findings

Estimated ATE: ~$1,795 increase in real earnings

Parametric test: Statistically significant lift

Permutation test: Observed effect falls in the extreme tail of the empirical null distribution

Conclusion: Reject the Null Hypothesis via statistical contradiction

The evidence supports a positive and statistically defensible causal impact of job training participation.

Business Insight: Hypothesis Testing as a Safety Valve

In the algorithmic economy, statistical significance is not an academic formality — it is a risk control mechanism.

Without disciplined falsification:

Data grubbing becomes strategy

Spurious correlations masquerade as insight

False positives scale into capital misallocation

Rigorous hypothesis testing functions as a safety valve:

It constrains overfitting

It formalizes uncertainty

It protects decision systems from noise-driven narratives

It enforces intellectual accountability in production analytics

In high-stakes environments — fintech underwriting, growth experimentation, A/B testing, or policy evaluation — controlling Type I error is not optional. It is infrastructure.

Return-Aware Experimentation (as practiced at companies like Netflix) frames experiments around expected business value — decisions are made when the projected revenue, engagement, or retention gains outweigh the risk of being wrong. This differs from the academic p < 0.05 standard, which optimizes for statistical certainty rather than economic payoff. In industry, decision thresholds are calibrated to ROI, scale, and cost of error, not fixed scientific convention. In other words, experimentation is judged by whether it improves outcomes, not just whether it clears a universal significance bar.

This project demonstrates how causal evidence can be architected, validated, and stress-tested before being operationalized — aligning statistical rigor with real-world economic decision-making.
