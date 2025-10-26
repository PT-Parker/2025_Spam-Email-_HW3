## Why
- We currently train multiple classifiers (SVM, Logistic Regression) but lack a single evaluation entrypoint to compare their performance on the same held-out split.
- Having a shared evaluation script simplifies regression tracking and reporting for future models.

## What Changes
- Add a CLI script that loads the existing TF-IDF features and all trained models, evaluates them on a consistent test set, and prints a comparison table/metrics.
- Ensure the script gracefully handles missing model artifacts and documents how to run it.
- Update docs to cover the evaluation workflow so teammates can reproduce comparisons.

## Impact
- Introduces a new script (e.g., `models/evaluate_models.py`) and optional CSV/console output for metrics.
- Relies on existing artifacts (`artifacts/preprocessed_data.pkl`, `artifacts/svm_model.pkl`, `artifacts/logreg_model.pkl`).
- No breaking change to existing training or UI flows.