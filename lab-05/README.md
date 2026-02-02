Chief Risk Officer,

I stress-tested our SaaS revenue Monte Carlo by changing only one assumption: New Sales. The standard model uses a Normal distribution (bell curve), but real markets often experience “fat tails,” meaning extreme outcomes happen more often than the Normal model predicts.

To capture this, I replaced Normal New Sales with a Student’s t-distribution (df=3), which produces more outliers while keeping the same general sales scale. The business logic stayed identical: base revenue minus churn plus new sales.

The key result is that the 95% Value at Risk (VaR) — the 5th percentile of projected revenue — is lower under the fat-tail model than under the Normal model. This happens because the t-distribution has a heavier downside tail, so “bad sales years” are more likely than the bell curve suggests.

Implication: if we set capital reserves using the Normal VaR, we will be under-buffered more frequently than expected. The fat-tail VaR indicates a larger potential shortfall in low-probability scenarios, so a higher reserve requirement is justified to maintain the same confidence level in solvency and operating stability.
