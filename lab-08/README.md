Hypothesis Testing & Causal Evidence Architecture
Objective
Most analytical workflows stop at estimation — computing a difference in means and treating it as ground truth. 
This project pivots from estimation to falsification: applying the formal logic of the scientific method to adjudicate between competing causal narratives. 
Using the Lalonde (1986) randomized experimental dataset, I operationalized hypothesis testing as a disciplined framework for separating signal from noise in program evaluation.

Technical Approach
Parametric Testing (Welch's T-Test): Computed the Average Treatment Effect (ATE) of job training on real earnings by calculating the signal-to-noise ratio across treatment and control groups using scipy.stats. 
Welch's formulation was chosen over Student's T-Test to avoid assuming equal population variances — a common source of Type I error inflation.
Non-Parametric Validation (Permutation Test, n=10,000): Earnings distributions are empirically non-normal, which violates a key assumption of parametric tests. 
I validated the T-Test result by constructing an empirical null distribution via random resampling, confirming robustness without distributional assumptions.
Type I Error Control: Both methods were evaluated against a pre-specified significance threshold, guarding against false positives and data dredging.

Result: A statistically significant lift of ~$1,795 in real earnings (p < 0.05), rejecting the null hypothesis via proof by statistical contradiction.
Business Insight
In production ML and algorithmic decision-making, the cost of a spurious correlation is not an academic footnote — it's a misallocated budget, a biased model, or a policy deployed at scale on a false premise. 
Rigorous hypothesis testing functions as the safety valve of the algorithmic economy: it enforces a formal burden of proof before any signal gets promoted into a business decision. 
Without this discipline, teams optimize for the appearance of lift rather than its existence, a failure mode known as p-hacking or data grubbing. 
The methodology applied here reflects the standard expected in any analytically mature organization where decisions carry real consequences.
