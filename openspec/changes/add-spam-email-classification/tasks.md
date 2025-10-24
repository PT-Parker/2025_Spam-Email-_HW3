# Phase 1 – Baseline SVM Classifier
- [x] Data Ingestion  
  Created `ingest/download_dataset.py` to download the dataset URL and store it at `dataset/sms_spam.csv`.
- [x] Data Preprocessing  
  Implemented `preprocessing/preprocess_sms.py` to load `dataset/sms_spam.csv`, clean message text, fit a TF-IDF vectorizer, and persist both the vectorizer (`artifacts/tfidf_vectorizer.pkl`) and transformed data (`artifacts/preprocessed_data.pkl`).
- [x] Model Training & Evaluation  
  Added `models/train_svm.py` to load the preprocessed features/labels, run an 80/20 train-test split, train a baseline SVM, print accuracy/classification report/confusion matrix, and save the model (`artifacts/svm_model.pkl`).

# Phase 2 – Reserved

# Phase 3 – Reserved
