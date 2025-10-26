"""Streamlit page to display model evaluation metrics."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

from models.evaluate_models import (
    DEFAULT_DATA_PATH,
    DEFAULT_MODEL_PATHS,
    DEFAULT_RANDOM_STATE,
    DEFAULT_TEST_SIZE,
    compute_model_metrics,
    load_available_models,
    load_features_and_labels,
)


def main() -> None:
    st.title("模型表現")
    st.write("檢視目前已訓練模型在共同測試集上的表現。")

    if not Path(DEFAULT_DATA_PATH).exists():
        st.error(
            "找不到前處理後的特徵檔案。請先執行 `preprocessing/preprocess_sms.py` 生成 `artifacts/preprocessed_data.pkl`。"
        )
        return

    features, labels = load_features_and_labels(Path(DEFAULT_DATA_PATH))

    X_train, X_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=DEFAULT_TEST_SIZE,
        random_state=DEFAULT_RANDOM_STATE,
        stratify=labels,
    )
    _ = (X_train, y_train)  # 目前未使用，但保留以利未來擴充

    models = load_available_models(DEFAULT_MODEL_PATHS)
    if not models:
        st.warning("沒有可用的模型檔案，請先完成模型訓練。")
        return

    target_names = sorted(pd.unique(labels))
    metrics = compute_model_metrics(models, X_test, y_test, target_names)

    for model_name, payload in metrics.items():
        st.subheader(model_name)
        records = []
        for key, value in payload["structured"].items():
            if isinstance(value, dict):
                records.append(
                    {
                        "Label": key,
                        "Precision": value.get("precision"),
                        "Recall": value.get("recall"),
                        "F1": value.get("f1-score"),
                        "Support": value.get("support"),
                    }
                )
            else:
                records.append({"Label": key, "Accuracy": value})
        structured_df = pd.DataFrame(records)
        desired_order = ["Label", "Precision", "Recall", "F1", "Support", "Accuracy"]
        structured_df = structured_df[[col for col in desired_order if col in structured_df.columns]]
        st.dataframe(structured_df)
        with st.expander("原始分類報告"):
            st.text(payload["formatted"])


if __name__ == "__main__":
    main()
