"""
Streamlit interface for the SMS spam classifier baseline.

The UI uses Traditional Chinese for titles and instructions while keeping
interactive elements (button, prediction feedback) in English, per the
project requirements.
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import joblib
import streamlit as st
from googletrans import Translator

from preprocessing.preprocess_sms import clean_message

VECTORIZER_PATH = Path("artifacts/tfidf_vectorizer.pkl")
MODEL_PATH = Path("artifacts/svm_model.pkl")


@st.cache_resource
def load_artifacts() -> Tuple[object, object]:
    """
    Lazily load the TF-IDF vectorizer and trained SVM model.
    """
    vectorizer = joblib.load(VECTORIZER_PATH)
    model = joblib.load(MODEL_PATH)
    return vectorizer, model


def main() -> None:
    st.set_page_config(page_title="簡訊垃圾郵件分類器", page_icon="📱")
    st.title("簡訊垃圾郵件分類器")
    st.write("這是一個使用 SVM 機器學習模型來偵測垃圾簡訊的應用程式。請在下方輸入一則英文訊息來進行測試。")

    translator = Translator()

    st.sidebar.title("範例訊息")
    spam_examples = [
        ("垃圾郵件範例 1", "Congratulations! You have won a $1000 Walmart gift card. Click here to claim."),
        ("垃圾郵件範例 2", "URGENT! Your bank account is suspended. Verify your details now at http://fakebank.com"),
    ]
    ham_examples = [
        ("正常郵件範例 1", "Hey, are we still meeting for lunch tomorrow at noon?"),
        ("正常郵件範例 2", "Reminder: Your dentist appointment is scheduled for Friday at 3 PM."),
    ]

    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

    for label, text in spam_examples:
        if st.sidebar.button(label):
            st.session_state.input_text = text

    for label, text in ham_examples:
        if st.sidebar.button(label):
            st.session_state.input_text = text

    col1, col2 = st.columns(2)
    with col1:
        st.text_area("請輸入要分析的簡訊內容：", height=200, key="input_text")

    with col2:
        st.subheader("即時中文翻譯")
        if st.session_state.input_text:
            try:
                translation = translator.translate(
                    st.session_state.input_text, src="en", dest="zh-tw"
                )
                st.info(translation.text)
            except Exception:
                st.error("翻譯服務暫時無法使用")
        else:
            st.info("... 等待輸入 ...")

    input_text = st.session_state.input_text

    if st.button("預測"):
        if not input_text.strip():
            st.warning("Please enter a message before requesting a prediction.")
            return

        try:
            vectorizer, model = load_artifacts()
        except FileNotFoundError as exc:
            st.error(f"Required artifact missing: {exc}")
            return

        cleaned_text = clean_message(input_text)
        features = vectorizer.transform([cleaned_text])
        prediction = model.predict(features)[0]

        if str(prediction).lower() == "spam":
            st.error("預測結果：垃圾郵件", icon="🚫")
        else:
            st.success("預測結果：正常郵件", icon="✅")


if __name__ == "__main__":
    main()
