## MODIFIED Requirements
### Requirement: Data analysis page available
The Streamlit data analysis page MUST render aggregate token tables without raising duplicate-column errors.

#### Scenario: Token table renders without duplicate columns
- **GIVEN** the dataset is available and the user opens the Data Analysis page
- **WHEN** the app displays top tokens per label
- **THEN** the concatenated table uses unique column names and renders successfully without throwing `ValueError`