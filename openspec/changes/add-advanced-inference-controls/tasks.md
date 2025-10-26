## 1. Model Compatibility
- [x] Update `models/train_svm.py` so the trained SVM supports `predict_proba()` and re-train to refresh `artifacts/svm_model.pkl`.

## 2. UI Enhancements
- [x] In `app.py`, add a decision-threshold slider, switch to probability-based predictions, and display the spam probability with the result.

## 3. Documentation & Validation
- [x] Document the new controls (slider + probability display) in README.
- [x] Run the Streamlit app (or an automated smoke script) to confirm both models predict successfully with adjustable threshold.