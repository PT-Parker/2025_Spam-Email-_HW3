"""Streamlit page for exploring the SMS spam dataset."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

DATASET_PATH = Path("dataset/sms_spam.csv")


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            "找不到 dataset/sms_spam.csv。請先執行 `python ingest/download_dataset.py` 下載資料集。"
        )
    return pd.read_csv(DATASET_PATH, header=None, names=["label", "message"])


def main() -> None:
    st.title("資料分析")
    st.write("檢視垃圾郵件資料集的整體分布與特徵。")

    try:
        df = load_dataset()
    except FileNotFoundError as exc:
        st.error(str(exc))
        return

    st.subheader("資料集概覽")
    st.write(f"資料筆數：{len(df):,}")
    st.dataframe(df.head())

    st.subheader("類別分布")
    class_counts = df["label"].value_counts().sort_index()
    class_ratio = (class_counts / len(df)).rename("ratio")
    st.dataframe(
        pd.concat([class_counts.rename("count"), class_ratio], axis=1)
        .reset_index()
        .rename(columns={"index": "label"})
    )

    fig, ax = plt.subplots()
    class_counts.plot(kind="bar", color=["#4e79a7", "#f28e2b"], ax=ax)
    ax.set_title("Class distribution")
    ax.set_xlabel("label")
    ax.set_ylabel("count")
    for container in ax.containers:
        ax.bar_label(container, label_type="edge", padding=3)
    st.pyplot(fig)
    plt.close(fig)

    st.subheader("訊息長度分析")
    df["message_length"] = df["message"].str.len()
    st.dataframe(
        df.groupby("label")["message_length"]
        .agg(["count", "mean", "median", "min", "max"])
        .round({"mean": 2, "median": 2})
    )

    fig_len, ax_len = plt.subplots()
    df["message_length"].plot(kind="hist", bins=50, color="#59a14f", alpha=0.85, ax=ax_len)
    ax_len.set_title("Distribution of message length (characters)")
    ax_len.set_xlabel("characters per message")
    ax_len.set_ylabel("frequency")
    st.pyplot(fig_len)
    plt.close(fig_len)

    st.subheader("常見詞彙")
    tokens_exploded = df["message"].str.lower().str.findall(r"[A-Za-z0-9']+").explode()
    top_overall = tokens_exploded.value_counts().head(15).reset_index()
    top_overall.columns = ["token", "count"]
    st.dataframe(top_overall)

    label_frames = []
    for label, subset in df.groupby("label"):
        per_label_tokens = subset["message"].str.lower().str.findall(r"[A-Za-z0-9']+").explode()
        counts = per_label_tokens.value_counts().head(10)
        if counts.empty:
            continue
        label_frames.append(
            pd.DataFrame(
                {
                    "label": label,
                    "token": counts.index,
                    "count": counts.values,
                }
            )
        )
    if label_frames:
        st.dataframe(pd.concat(label_frames, ignore_index=True))
    else:
        st.info("未找到可顯示的詞頻統計。")

    st.subheader("範例訊息")
    for label, subset in df.groupby("label"):
        st.markdown(f"**範例訊息 - {label}**")
        sample_size = min(len(subset), 3)
        st.table(subset[["message", "message_length"]].sample(sample_size, random_state=42))


if __name__ == "__main__":
    main()
