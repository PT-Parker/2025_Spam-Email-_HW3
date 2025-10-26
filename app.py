"""
Streamlit interface for the SMS spam classifiers (SVM and Logistic Regression).

The UI uses Traditional Chinese for titles and instructions while keeping
interactive elements (button, prediction feedback) in English, per the
project requirements.
"""

from __future__ import annotations

from pathlib import Path

import joblib
import streamlit as st
from deep_translator import GoogleTranslator

from preprocessing.preprocess_sms import clean_message

VECTORIZER_PATH = Path("artifacts/tfidf_vectorizer.pkl")
SVM_MODEL_PATH = Path("artifacts/svm_model.pkl")
LOGREG_MODEL_PATH = Path("artifacts/logreg_model.pkl")
MODEL_OPTIONS = {
    "線性 SVM": SVM_MODEL_PATH,
    "邏輯迴歸": LOGREG_MODEL_PATH,
}


@st.cache_resource
def load_vectorizer() -> object:
    """
    Lazily load and cache the TF-IDF vectorizer.
    """
    return joblib.load(VECTORIZER_PATH)


@st.cache_resource
def load_model(model_path: Path) -> object:
    """
    Lazily load and cache a trained classification model.
    """
    return joblib.load(model_path)


def main() -> None:
    st.set_page_config(page_title="簡訊垃圾郵件分類器", page_icon="📱")
    st.title("簡訊垃圾郵件分類器")
    st.write("這是一個提供 SVM 與邏輯迴歸兩種模型來偵測垃圾簡訊的應用程式。請在下方輸入一則英文訊息來進行測試。")

    translator = GoogleTranslator(source="en", target="zh-TW")

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
                translation = translator.translate(st.session_state.input_text)
                st.info(translation)
            except Exception:
                st.error("翻譯服務暫時無法使用")
        else:
            st.info("... 等待輸入 ...")

    input_text = st.session_state.input_text
    model_choice = st.radio("選擇預測模型", list(MODEL_OPTIONS.keys()), index=0)
    selected_model_path = MODEL_OPTIONS[model_choice]
    threshold = st.slider(
        "決策門檻值 (Decision Threshold)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01,
    )

    if st.button("預測"):
        if not input_text.strip():
            st.warning("Please enter a message before requesting a prediction.")
            return

        try:
            vectorizer = load_vectorizer()
        except FileNotFoundError as exc:
            st.error(f"Required artifact missing: {exc}")
            return
        try:
            model = load_model(selected_model_path)
        except FileNotFoundError:
            st.error(f"找不到模型檔案：{selected_model_path}")
            return
        except Exception as exc:
            st.error(f"載入模型時發生錯誤：{exc}")
            return

        if not hasattr(model, "predict_proba"):
            st.error(
                "本模型目前不支援機率預測，請重新訓練或選擇其他模型。",
            )
            return

        cleaned_text = clean_message(input_text)
        features = vectorizer.transform([cleaned_text])
        probabilities = model.predict_proba(features)[0]

        classes = [str(label).lower() for label in getattr(model, "classes_", [])]
        try:
            spam_index = classes.index("spam")
        except ValueError:
            st.error("模型未包含 spam 類別，請確認訓練資料。")
            return

        spam_probability = probabilities[spam_index]
        is_spam = spam_probability >= threshold
        probability_display = f"{spam_probability * 100:.1f}%"

        if is_spam:
            st.error(f"預測結果：垃圾郵件 (機率: {probability_display})", icon="🚫")
        else:
            st.success(f"預測結果：正常郵件 (機率: {probability_display})", icon="✅")


if __name__ == "__main__":
    main()
