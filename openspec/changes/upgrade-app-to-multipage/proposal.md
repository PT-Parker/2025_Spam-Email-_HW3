## Why
- The current Streamlit app only exposes the classifier page; analysis and evaluation insights are hidden in separate scripts/notebooks.
- A multi-page app lets stakeholders explore the dataset, review model performance, and try live predictions from one interface.

## What Changes
- Convert the Streamlit project to use the built-in multi-page structure (`pages/` directory).
- Add a "Data Analysis" page that surfaces EDA visuals (label distribution, message length histograms, frequent tokens) sourced from the dataset.
- Add a "Model Performance" page that runs the shared evaluation routine and renders metrics tables for the trained models.
- Keep the main `app.py` focused on interactive spam prediction as the landing page.

## Impact
- Introduces new Streamlit scripts under `pages/` reusing existing preprocessing/evaluation utilities.
- Users can navigate between prediction, analysis, and performance views without leaving the app.
- Minimal risk: relies on artifacts and dataset already produced in the workflow.