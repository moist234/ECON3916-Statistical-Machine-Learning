FedSpeak Analysis — NLP on FOMC Minutes
Objective: Quantify the tone and uncertainty of Federal Reserve communications across two decades of FOMC meeting minutes using NLP and unsupervised machine learning.
Methodology:

Loaded 462 FOMC meeting minutes and statements (2000-2026) via HuggingFace datasets
Preprocessed text with tokenization, stop word removal, and lemmatization using NLTK
Built a TF-IDF document-term matrix (unigrams and bigrams, 1000 features) with TfidfVectorizer
Computed Loughran-McDonald sentiment scores (net sentiment and uncertainty) using a domain-specific financial dictionary
Reduced TF-IDF matrix to 50 dimensions with TruncatedSVD, then clustered documents with K-Means (K=3) and visualized in 2D PCA space
Compared pre-COVID and post-COVID sentiment distributions using overlaid histograms

Key Findings: K-Means identified three distinct language regimes roughly corresponding to pre-crisis, crisis-era, and post-COVID tightening periods, with the 2020 and 2022 meetings standing out as clear outliers in PCA space. Post-COVID documents show meaningfully lower net sentiment and higher uncertainty scores than the pre-2020 baseline, consistent with the Fed navigating emergency rate cuts followed by the most aggressive tightening cycle in four decades. The LM uncertainty index spiked most sharply during March 2020 and remained elevated through 2022, reflecting genuine policy ambiguity rather than routine communication shifts.