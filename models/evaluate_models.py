"""
Evaluate all trained SMS classification models on a consistent test split.

This script loads the preprocessed TF-IDF features and labels, reuses a fixed
train/test split, and scores each available model (e.g., SVM, Logistic Regression)
to help compare performance side-by-side.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Final, Iterable, List, Tuple

import joblib
import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

DEFAULT_DATA_PATH: Final[Path] = Path("artifacts/preprocessed_data.pkl")
DEFAULT_RANDOM_STATE: Final[int] = 42
DEFAULT_TEST_SIZE: Final[float] = 0.2
DEFAULT_MODEL_PATHS: Dict[str, Path] = {
    "Linear SVM": Path("artifacts/svm_model.pkl"),
    "Logistic Regression": Path("artifacts/logreg_model.pkl"),
}


def load_features_and_labels(path: Path) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load the TF-IDF features and labels stored via joblib.
    """
    payload = joblib.load(path)
    return payload["features"], payload["labels"]


def load_available_models(model_paths: Dict[str, Path]) -> Dict[str, object]:
    """
    Load models whose artifacts exist, returning a map from display name to model.
    """
    available: Dict[str, object] = {}
    for label, path in model_paths.items():
        if not path.exists():
            print(f"[Warn] Missing model artifact: {path}")
            continue
        try:
            available[label] = joblib.load(path)
        except Exception as exc:
            print(f"[Warn] Failed to load {label} from {path}: {exc}")
    return available


def compute_model_metrics(
    models: Dict[str, object],
    X_test: np.ndarray,
    y_test: np.ndarray,
    target_names: Iterable[str],
) -> Dict[str, Dict[str, object]]:
    """
    Evaluate each model and return both structured metrics and formatted reports.
    """
    results: Dict[str, Dict[str, object]] = {}
    for label, model in models.items():
        predictions = model.predict(X_test)
        structured = classification_report(
            y_test,
            predictions,
            target_names=target_names,
            output_dict=True,
        )
        formatted = classification_report(
            y_test,
            predictions,
            target_names=target_names,
            digits=4,
        )
        results[label] = {
            "formatted": formatted,
            "structured": structured,
        }
    return results


def evaluate_models(
    models: Dict[str, object],
    X_test: np.ndarray,
    y_test: np.ndarray,
    target_names: Iterable[str],
) -> List[str]:
    """
    Evaluate each model and collect formatted report strings.
    """
    reports: List[str] = []
    metrics = compute_model_metrics(models, X_test, y_test, target_names)
    for label, payload in metrics.items():
        header = f"=== {label} ==="
        reports.append(f"{header}\n{payload['formatted']}")
    return reports


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate trained SMS classification models on a shared test split."
    )
    parser.add_argument(
        "--data-path",
        default=DEFAULT_DATA_PATH,
        type=Path,
        help="Path to the joblib artifact with TF-IDF features and labels.",
    )
    parser.add_argument(
        "--test-size",
        default=DEFAULT_TEST_SIZE,
        type=float,
        help="Fraction of the dataset reserved for testing (default: 0.2).",
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
    if not args.data_path.exists():
        raise SystemExit(f"Preprocessed data artifact not found: {args.data_path}")

    features, labels = load_features_and_labels(args.data_path)
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=args.test_size,
        random_state=args.random_state,
        stratify=labels,
    )
    # Suppress unused warning for completeness: training split may be reused later.
    _ = (X_train, y_train)

    models = load_available_models(DEFAULT_MODEL_PATHS)
    if not models:
        raise SystemExit("No model artifacts found. Train models before evaluation.")

    target_names = sorted(np.unique(labels))
    reports = evaluate_models(models, X_test, y_test, target_names)

    print("Model comparison on shared test split")
    print("=" * 40)
    for block in reports:
        print(block)
        print("-" * 40)


if __name__ == "__main__":
    main()
