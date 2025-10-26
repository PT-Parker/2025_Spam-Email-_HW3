## ADDED Requirements
### Requirement: Streamlit Multi-Page Navigation
The system MUST organize the Streamlit app into multiple pages so users can access prediction, data analysis, and model performance views from a single deployment.

#### Scenario: Data analysis page available
- **GIVEN** the Streamlit app is running
- **WHEN** the user selects the "Data Analysis" page from the sidebar
- **THEN** the app loads `dataset/sms_spam.csv`, shows class distribution charts, message length histograms, and common token tables without raising errors

#### Scenario: Model performance page available
- **GIVEN** trained model artifacts exist in `artifacts/`
- **WHEN** the user opens the "Model Performance" page
- **THEN** the app reuses the evaluation pipeline to display accuracy and classification metrics for each model in a readable layout, or clearly indicates when a model artifact is missing

#### Scenario: Prediction page remains accessible
- **GIVEN** the multi-page navigation is enabled
- **WHEN** the user visits the home page (`app.py`)
- **THEN** the existing spam classifier UI behaves as before, allowing message input, model selection, and prediction feedback