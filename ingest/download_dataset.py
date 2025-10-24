"""
Download the SMS spam dataset and store it locally.

This script retrieves the dataset from the public URL provided in the
Phase 1 baseline tasks and saves it to the dataset directory as
``sms_spam.csv``. The script creates the target directory when needed.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Final

import requests

DATASET_URL: Final[
    str
] = "https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv"
DEFAULT_DATASET_DIR: Final[str] = "dataset"
DEFAULT_OUTPUT_FILENAME: Final[str] = "sms_spam.csv"


def download_dataset(output_dir: Path) -> Path:
    """
    Download the SMS spam dataset into ``output_dir``.

    Returns the path of the downloaded file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / DEFAULT_OUTPUT_FILENAME

    response = requests.get(DATASET_URL, timeout=30)
    response.raise_for_status()

    output_path.write_bytes(response.content)
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download the SMS spam dataset into the dataset/ directory."
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_DATASET_DIR,
        type=Path,
        help="Directory where sms_spam.csv will be written (default: dataset/).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir: Path = args.output_dir
    output_path = download_dataset(output_dir)
    print(f"Dataset written to {output_path.resolve()}")


if __name__ == "__main__":
    main()
