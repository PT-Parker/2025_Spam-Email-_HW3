# Proposal: Spam Email Classification Roadmap

## Change Overview
- **Goal**: Build a machine learning pipeline for SMS spam email classification that ultimately delivers a logistic regression model.
- **Scope**: Establish a reproducible baseline using Support Vector Machines (SVM) and prepare the foundation for later phases that will iterate toward optimized logistic regression solutions.
- **Dataset**: `https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv`
- **Success Metrics**: Track precision, recall, F1 score, accuracy, and confusion matrix results; require at least 90% accuracy and 0.85 F1 before moving beyond the baseline phase.

## Motivation
Logistic regression is the target model for the spam email classifier, but a reliable baseline is needed to validate the preprocessing pipeline, evaluation harness, and dataset suitability. Establishing an SVM baseline provides an early benchmark, exposes data quality issues, and ensures that the later logistic regression work has measurable targets.

## Proposed Phases

### Phase 1 – Baseline SVM Classifier
- Ingest the SMS spam dataset and split it into training, validation, and test sets with reproducible random seeds.
- Perform text preprocessing (normalization, tokenization, and vectorization) and document all decisions.
- Train a linear SVM model, sweep key hyperparameters, and record metrics on validation/test sets.
- Produce baseline evaluation artifacts (confusion matrix plots, metric tables) and an initial write-up describing gaps to close before adopting logistic regression.

### Phase 2 – Reserved
This section is intentionally left blank to host future iterations (e.g., logistic regression experiments, feature engineering, and deployment planning).

### Phase 3 – Reserved
This section is intentionally left blank to support additional enhancements (e.g., ensemble experimentation, monitoring, or on-device deployment studies).

## Deliverables
- Reproducible code notebooks or scripts for dataset ingestion, preprocessing, model training, and evaluation.
- Baseline performance report detailing metrics, insights, and recommendations for the upcoming logistic regression work.
- Documented next steps capturing hypotheses for improving performance in later phases.

## Risks & Mitigations
- **Dataset bias or imbalance**: Monitor class distribution and apply rebalancing strategies (e.g., stratified splits or class weights) if metrics indicate skewed performance.
- **Text preprocessing regressions**: Version preprocessing steps and add unit tests around tokenization/vectorization helpers to ensure consistency across phases.
- **Metric stagnation**: Set clear escalation criteria (e.g., revisit feature engineering or consider alternative models) if Phase 1 fails to meet success thresholds.

## Open Questions
- What environment (local notebook vs. production script) should host the final logistic regression model?
- Are there deployment constraints (latency, memory) that should shape feature design in future phases?
- Should later phases incorporate additional datasets or augmentation to improve generalization?
