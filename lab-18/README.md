Fraud Detection Model Evaluation — Metrics that Matter
Objective: Rigorously evaluate a logistic regression fraud detector on a severely imbalanced real-world dataset, demonstrating why accuracy is a misleading metric and how threshold selection must be driven by business constraints rather than statistical defaults.
Methodology:

Loaded the Kaggle Credit Card Fraud Detection dataset (284,807 transactions, 0.172% positive class) with PCA-anonymized features V1–V28 and transaction Amount
Established a naive all-negative baseline to demonstrate the accuracy paradox: 99.83% accuracy with zero fraud detected
Trained a logistic regression classifier and evaluated performance using confusion matrices, classification report (Precision, Recall, F1), ROC-AUC, and Precision-Recall AUC on the minority fraud class
Swept the classification threshold to identify the F1-optimal operating point, illustrating how the default τ = 0.5 is inappropriate under severe class imbalance
Applied a capacity constraint (maximum 500 daily investigations) to select the most aggressive threshold that keeps flagged transactions within operational limits, then computed Recall and Precision at that operating point

Key Findings:

The accuracy paradox confirms that a model predicting no fraud achieves 99.83% accuracy, making accuracy a useless standalone metric for imbalanced fraud detection
Logistic regression achieved strong ROC-AUC and meaningful PR-AUC, indicating the model reliably separates fraud from legitimate transactions despite extreme class imbalance
The F1-optimal threshold differed substantially from 0.5, highlighting that default thresholds systematically underperform on imbalanced classes
Under the 500-investigation capacity constraint, the selected threshold revealed the tradeoff between operational feasibility and Recall, providing a concrete framework for communicating model limitations to a VP of Risk