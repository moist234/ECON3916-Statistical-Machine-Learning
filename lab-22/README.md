Clustering World Economies with K-Means & PCA
Objective: Identify natural groupings among world economies using unsupervised machine learning applied to World Bank development indicators.
Methodology:

Downloaded 10 WDI indicators for ~160 countries via wbgapi (GDP per capita, life expectancy, infant mortality, and others)
Standardized all features with StandardScaler to ensure equal contribution to distance calculations
Selected optimal K using elbow method and silhouette analysis across K=2 through K=10
Fit K-Means (K=4) and projected results to 2D via PCA for visualization
Validated clusters against World Bank official income classifications using cross-tabulation
Extended pipeline to California Housing census tract data to confirm generalizability

Key Findings: K=4 produced the most interpretable clusters, aligning closely with the World Bank's low, lower-middle, upper-middle, and high income tiers. Cluster separation was driven primarily by GDP per capita and infant mortality, which together explain the majority of variance captured by PC1. The California Housing extension confirmed that the same pipeline generalizes to domestic housing markets, producing geographically and economically coherent groupings.