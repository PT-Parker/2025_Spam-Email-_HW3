## Why
- Selecting the "Data Analysis" page currently raises `ValueError: Duplicate column names` when rendering token frequency tables.
- The error breaks the multi-page experience we just added, so we need a quick bugfix to restore normal navigation.

## What Changes
- Adjust the token aggregation logic so the concatenated DataFrame uses unique column names per label.
- Ensure the Streamlit page continues to show per-label top tokens without runtime errors.

## Impact
- User-facing: Data Analysis page becomes usable again.
- Technical: Small tweak within `pages/1_Data_Analysis.py`; no new dependencies required.