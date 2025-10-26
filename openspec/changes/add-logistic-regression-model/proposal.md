## Why
- Provide a lighter-weight baseline alongside the existing Linear SVM so we can compare models and tune for deployment constraints.
- Some environments (e.g., constrained devices) prefer interpretable coefficients and faster inference that Logistic Regression offers.

## What Changes
- Add a training and evaluation script for Logistic Regression that mirrors the current SVM workflow and persists the trained model artifact.
- Update the Streamlit app so users can choose between the SVM and Logistic Regression models at prediction time.
- Refresh project docs to explain how to train, evaluate, and select the Logistic Regression model.

## Impact
- Requires an additional model artifact (`artifacts/logreg_model.pkl`).
- Minor UI change in the Streamlit app to expose model selection.
- No breaking changes for existing SVM users; SVM remains the default.