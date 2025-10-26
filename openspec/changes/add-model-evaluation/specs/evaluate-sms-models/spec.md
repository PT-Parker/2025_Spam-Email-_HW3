## ADDED Requirements
### Requirement: Evaluate Trained SMS Models
The system MUST provide a CLI workflow that evaluates each trained SMS classifier on a common test split using the shared TF-IDF features and reports comparable metrics.

#### Scenario: Evaluate available models on consistent split
- **GIVEN** `artifacts/preprocessed_data.pkl` contains TF-IDF features and labels
- **WHEN** the evaluation script runs with default parameters
- **THEN** it loads each available model artifact (`artifacts/svm_model.pkl`, `artifacts/logreg_model.pkl`, etc.)
- **AND** prints consolidated metrics (accuracy and precision/recall/F1) for every model using the same test subset

#### Scenario: Handle missing model artifacts
- **GIVEN** at least one expected model artifact is absent
- **WHEN** the evaluation script executes
- **THEN** it skips the missing model, emits a clear warning naming the missing file, and continues evaluating remaining models without failing