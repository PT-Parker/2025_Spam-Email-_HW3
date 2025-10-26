## Why
- We need descriptive analytics to understand the SMS spam dataset before training and deploying models.
- An exploratory notebook helps surface class imbalance, text length patterns, and data quality issues for future improvements.

## What Changes
- Add a Jupyter Notebook under `notebooks/` that opens `dataset/sms_spam.csv`, performs exploratory analysis, and visualizes key distributions.
- Include summaries such as class counts, message length statistics, and representative visualizations (histograms, bar charts).
- Document how to run the notebook (locally or via VS Code) so teammates can reproduce the analysis.

## Impact
- Introduces a new `notebooks/` directory with at least one `.ipynb` file.
- Requires pandas/matplotlib (already used elsewhere) to execute the notebook.
- No changes to production code paths; used strictly for analysis and documentation.