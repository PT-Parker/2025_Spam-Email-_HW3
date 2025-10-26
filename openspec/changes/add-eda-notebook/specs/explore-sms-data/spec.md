## ADDED Requirements
### Requirement: Exploratory Analysis Notebook
The system MUST include an exploratory data analysis notebook for the SMS spam dataset so contributors can inspect distributions and data quality before modeling.

#### Scenario: Generate dataset overview
- **GIVEN** `dataset/sms_spam.csv` is available in the repository
- **WHEN** a contributor runs the `notebooks/sms_spam_eda.ipynb` notebook top-to-bottom
- **THEN** the notebook loads the dataset, reports class counts and descriptive statistics, and presents at least one visualization of message characteristics

#### Scenario: Surface missing data artifacts
- **GIVEN** the dataset file is missing or unreadable
- **WHEN** the notebook attempts to load the CSV
- **THEN** it surfaces a clear error or markdown guidance indicating the expected dataset location instead of failing silently