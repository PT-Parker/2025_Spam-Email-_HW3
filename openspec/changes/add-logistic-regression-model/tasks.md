## 1. Training Pipeline
- [x] Mirror the SVM trainer to create a Logistic Regression training script with equivalent CLI arguments and metrics output.
- [x] Persist the trained Logistic Regression model as `artifacts/logreg_model.pkl` and document artifact expectations.

## 2. Application Updates
- [x] Update the Streamlit app to allow selecting between the SVM and Logistic Regression models at inference time.
- [x] Ensure missing-artifact errors remain user-friendly for both model options.

## 3. Documentation & Validation
- [x] Update README usage instructions to cover training and serving the Logistic Regression model.
- [x] Run lint/tests or a smoke prediction using the new model to confirm the end-to-end flow still works.
