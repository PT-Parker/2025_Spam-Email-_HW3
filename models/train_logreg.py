"""
Train and evaluate a Logistic Regression classifier on the preprocessed SMS spam data.

This script mirrors ``models/train_svm.py`` but uses scikit-learn's Logistic Regression
estimator. It consumes TF-IDF features prepared by ``preprocessing/preprocess_sms.py``,
prints standard evaluation metrics, and persists the trained model artifact.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Final, Tuple

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

DEFAULT_DATA_PATH: Final[str] = "artifacts/preprocessed_data.pkl"
DEFAULT_MODEL_PATH: Final[str] = "artifacts/logreg_model.pkl"
DEFAULT_TEST_SIZE: Final[float] = 0.2
DEFAULT_RANDOM_STATE: Final[int] = 42


def load_preprocessed_artifacts(path: Path) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load TF-IDF features and labels persisted with joblib, ensuring the artifact exists.
    """
    if not path.exists():
        raise FileNotFoundError(f"Preprocessed artifact not found: {path}")

    payload = joblib.load(path)
    features = payload["features"]
    labels = payload["labels"]
    return features, labels


def train_and_evaluate(
    data_path: Path,
    model_path: Path,
    test_size: float,
    random_state: int,
) -> None:
    """
    Train a Logistic Regression model and print evaluation metrics.
    """
    features, labels = load_preprocessed_artifacts(data_path)

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=test_size,
        random_state=random_state,
        stratify=labels,
    )

    classifier = LogisticRegression(max_iter=1000, solver="liblinear")
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, digits=4)
    matrix = confusion_matrix(y_test, predictions)

    print(f"Accuracy: {acc:.4f}")
    print("Classification Report:")
    print(report)
    print("Confusion Matrix:")
    print(matrix)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(classifier, model_path)
    print(f"Trained Logistic Regression model saved to {model_path.resolve()}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train a Logistic Regression classifier on TF-IDF features."
    )
    parser.add_argument(
        "--data-path",
        default=DEFAULT_DATA_PATH,
        type=Path,
        help="Path to the joblib file containing TF-IDF features and labels.",
    )
    parser.add_argument(
        "--model-out",
        default=DEFAULT_MODEL_PATH,
        type=Path,
        help="Destination path for the trained Logistic Regression model.",
    )
    parser.add_argument(
        "--test-size",
        default=DEFAULT_TEST_SIZE,
        type=float,
        help="Fraction of data to reserve for testing (default: 0.2).",
    )
    parser.add_argument(
        "--random-state",
        default=DEFAULT_RANDOM_STATE,
        type=int,
        help="Random seed for the train/test split (default: 42).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        train_and_evaluate(
            data_path=args.data_path,
            model_path=args.model_out,
            test_size=args.test_size,
            random_state=args.random_state,
        )
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
