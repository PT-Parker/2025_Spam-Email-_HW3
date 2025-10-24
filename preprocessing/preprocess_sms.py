"""
Preprocess the SMS spam dataset and generate TF-IDF features.

Steps:
1. Load ``dataset/sms_spam.csv`` (no header) and rename the columns to ``label`` and ``message``.
2. Clean the message text by lowercasing, removing punctuation, and dropping English stopwords.
3. Fit a TF-IDF vectorizer on the cleaned text.
4. Persist the fitted vectorizer and the transformed feature matrix with labels for downstream tasks.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Final

import joblib
import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer

DEFAULT_INPUT_PATH: Final[str] = "dataset/sms_spam.csv"
DEFAULT_VECTORIZER_PATH: Final[str] = "artifacts/tfidf_vectorizer.pkl"
DEFAULT_OUTPUT_DATA_PATH: Final[str] = "artifacts/preprocessed_data.pkl"

STOPWORDS = set(ENGLISH_STOP_WORDS)
PUNCTUATION_PATTERN = re.compile(r"[^\w\s]")


def clean_message(text: str) -> str:
    """
    Apply lowercase transformation, remove punctuation, and drop stopwords.
    """
    text = text.lower()
    text = PUNCTUATION_PATTERN.sub(" ", text)
    tokens = [token for token in text.split() if token not in STOPWORDS]
    return " ".join(tokens)


def preprocess_dataset(
    input_path: Path, vectorizer_path: Path, output_data_path: Path
) -> None:
    """
    Run preprocessing pipeline and persist artifacts.
    """
    df = pd.read_csv(input_path, header=None, names=["label", "message"])
    df["message"] = df["message"].fillna("").astype(str).map(clean_message)

    vectorizer = TfidfVectorizer(lowercase=False)
    features = vectorizer.fit_transform(df["message"])
    labels = df["label"].values

    vectorizer_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(vectorizer, vectorizer_path)

    output_data_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"features": features, "labels": labels}, output_data_path)

    print(f"Fitted TF-IDF vectorizer written to {vectorizer_path.resolve()}")
    print(
        "Preprocessed data saved to "
        f"{output_data_path.resolve()} with shape {features.shape}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preprocess the SMS spam dataset and persist TF-IDF artifacts."
    )
    parser.add_argument(
        "--input-path",
        default=DEFAULT_INPUT_PATH,
        type=Path,
        help="Path to dataset/sms_spam.csv.",
    )
    parser.add_argument(
        "--vectorizer-out",
        default=DEFAULT_VECTORIZER_PATH,
        type=Path,
        help="Output path for the fitted TF-IDF vectorizer.",
    )
    parser.add_argument(
        "--data-out",
        default=DEFAULT_OUTPUT_DATA_PATH,
        type=Path,
        help="Output path for the serialized TF-IDF features and labels.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    preprocess_dataset(args.input_path, args.vectorizer_out, args.data_out)


if __name__ == "__main__":
    main()
