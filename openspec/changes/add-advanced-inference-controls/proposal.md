## Why
- Stakeholders want to inspect the predicted spam probability and adjust decision sensitivity directly in the UI, matching the teacher demo.
- The current classifier page only returns a hard prediction, so we cannot tune precision/recall trade-offs without code changes.

## What Changes
- Update `app.py` to expose a decision-threshold slider, surface predicted spam probability, and base the final label on that threshold.
- Ensure both bundled models (SVM and Logistic Regression) expose `predict_proba()` so the new UI control works consistently.
- Modify the SVM training script when needed so exported artifacts include probability estimates.
- Refresh documentation as needed to explain the new controls.

## Impact
- Users gain transparent spam probability and adjustable threshold without leaving the app.
- SVM training script may require retraining models (probability=True) to produce compatible artifacts.
- Minor documentation updates; no new dependencies expected.