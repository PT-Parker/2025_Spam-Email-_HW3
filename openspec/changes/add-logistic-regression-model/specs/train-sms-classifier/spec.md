## ADDED Requirements
### Requirement: Logistic Regression Training Workflow
The system MUST provide a CLI workflow that trains and evaluates a Logistic Regression classifier using the existing TF-IDF features and labels, persisting the fitted model artifact.

#### Scenario: Train Logistic Regression model from preprocessed artifacts
- **GIVEN** `artifacts/preprocessed_data.pkl` contains TF-IDF features and labels
- **WHEN** the Logistic Regression training script runs with default arguments
- **THEN** it reports accuracy and classification metrics to stdout
- **AND** saves the trained model to `artifacts/logreg_model.pkl`

#### Scenario: Surface a clear error when training inputs are missing
- **GIVEN** the training script runs without the required preprocessed data artifact
- **WHEN** the load step fails
- **THEN** the script exits with an explanatory error message that names the missing file

### Requirement: Runtime Model Selection
The system MUST allow the Streamlit UI to run predictions with either the existing SVM model or the new Logistic Regression model using the shared TF-IDF vectorizer.

#### Scenario: User selects Logistic Regression in the UI
- **GIVEN** both `artifacts/svm_model.pkl` and `artifacts/logreg_model.pkl` are available
- **WHEN** the user selects the Logistic Regression option in the app
- **THEN** the app loads `logreg_model.pkl` and returns predictions using that model

#### Scenario: Missing Logistic Regression artifact
- **GIVEN** the user selects Logistic Regression but the artifact file is absent
- **WHEN** the app attempts to load the model
- **THEN** the UI displays a user-friendly error identifying the missing artifact without crashing