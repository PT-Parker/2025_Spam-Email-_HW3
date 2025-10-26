## MODIFIED Requirements
### Requirement: Runtime Model Selection
The prediction page MUST allow choosing any trained model and now surface probability-driven predictions with adjustable thresholds.

#### Scenario: Adjustable decision threshold
- **GIVEN** the classifier page is loaded
- **WHEN** the user adjusts the decision-threshold slider and submits a message
- **THEN** the app compares the spam probability to the slider value and displays a result using that threshold along with the probability percentage

#### Scenario: Probability support across models
- **GIVEN** the user selects either the SVM or Logistic Regression model
- **WHEN** the prediction runs
- **THEN** the underlying model provides `predict_proba()`; if the artifact lacks probability support, the UI surfaces a clear error instructing to retrain with the updated script