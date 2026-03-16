# Data Wrangling & Engineering Pipeline

## Objective
Engineer a production-grade data preparation pipeline on a deliberately chaotic HR economics dataset, resolving structural missingness, multicollinearity traps, and high-cardinality categorical variables to produce a clean, model-ready feature matrix.

---

## Dataset
**messy_hr_economics.csv** — A synthetic HR economics dataset containing employee-level salary, tenure, department, and geographic data, intentionally contaminated with missing values, raw categorical fields, and high-cardinality ZIP code identifiers.

---

## Methodology

- **Environment Initialization** — Configured an analytical stack using `pandas`, `numpy`, `statsmodels`, `missingno`, and `category_encoders` to cover the full spectrum of forensic diagnosis, statistical modeling, and feature engineering.

- **Visual Missingness Forensics** — Deployed `missingno.matrix()` to render a structural missingness map across all columns, enabling visual identification of aligned white-gap patterns between `bonus_pay` and `performance_rating` — a diagnostic signature of Missing at Random (MAR) rather than MCAR or MNAR mechanisms.

- **Conditional Median Imputation** — Resolved MAR-driven nulls in `base_salary` via grouped median imputation using `groupby().transform()`, preserving within-department salary variance structures rather than applying a crude global mean that would distort distributional integrity.

- **Dummy Variable Trap (Intentional Failure)** — Deliberately constructed a full-rank dummy matrix via `pd.get_dummies()` without dropping a reference class, then added a constant intercept via `sm.add_constant()` to engineer perfect multicollinearity. The resulting singular matrix caused OLS to fail, empirically demonstrating the trap.

- **Reference Class Escape (k-1 Methodology)** — Re-encoded department categories using `drop_first=True`, establishing a baseline reference class and eliminating linear dependence. The corrected OLS model fit successfully, producing interpretable coefficient estimates relative to the omitted category.

- **Target Encoding for High Cardinality** — Applied `category_encoders.TargetEncoder` to the `office_zip` column, collapsing hundreds of ZIP code categories into a single continuous vector representing the conditional mean of `base_salary` per geography — preserving signal while eliminating dimensionality explosion.

---

## Key Findings

Visual forensics confirmed a MAR missingness structure, with `bonus_pay` and `performance_rating` gaps co-occurring systematically rather than at random — validating the use of conditional rather than global imputation. The Dummy Variable Trap demonstration produced a concrete, observable OLS failure, reinforcing why the k-1 reference class methodology is a non-negotiable constraint in categorical encoding. Target Encoding successfully compressed high-cardinality geographic data into a statistically meaningful continuous feature, resolving a dimensionality problem that would otherwise render standard OLS estimation computationally unstable.

---

## Tech Stack
`Python` · `pandas` · `numpy` · `statsmodels` · `missingno` · `category_encoders`
