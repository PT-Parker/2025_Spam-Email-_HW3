# 簡訊垃圾郵件分類器 (Spam SMS Classifier)

## 🚀 線上 Demo 網站

您可以點擊以下網址，直接在瀏覽器中體驗這個專案：

[https://2025spam-email-hw3-parker-ho.streamlit.app/](https://2025spam-email-hw3-parker-ho.streamlit.app/)

## 專案描述

本專案建立了一個以支援向量機 (SVM) 為核心的垃圾簡訊分類流程，涵蓋資料下載、前處理、模型訓練與評估，並透過 Streamlit 打造完整的繁體中文互動式網頁介面，方便快速測試與展示模型成果。現已額外提供 Logistic Regression 模型作為輕量化替代方案，可直接在 UI 中切換比較。

## 主要功能

- 提供 SVM 與 Logistic Regression 兩種垃圾郵件分類模型，可在介面中即時切換。
- 主頁顯示垃圾郵件機率並提供決策門檻 slider，可依需求調整靈敏度。
- 完整的繁體中文 Streamlit 互動介面。
- 提供點擊即可填入訊息的側邊欄範例。
- 具備即時英翻中的翻譯功能，協助理解輸入內容。

## 安裝步驟

```bash
git clone [https://github.com/PT-Parker/2025_Spam-Email-_HW3]
cd hw3
pip install -r requirements.txt
```

## 如何執行

```bash
streamlit run app.py
```

Streamlit 伺服器啟動後，左側導覽列會顯示多個頁面：
- **Spam Classifier**：主頁，提供即時簡訊預測與模型切換。
- **Data Analysis**：呈現資料集的類別分布、訊息長度統計與常見詞彙。
- **Model Performance**：即時讀取 `artifacts/` 中的模型並顯示比較結果。

## 模型訓練

所有模型訓練腳本都會使用 `artifacts/preprocessed_data.pkl` 中的 TF-IDF 特徵與標籤，並將結果輸出到 `artifacts/`：

```bash
# 訓練線性 SVM
python models/train_svm.py

# 訓練 Logistic Regression
python models/train_logreg.py

# 比較所有訓練好的模型
python models/evaluate_models.py
```

可以透過 `--data-path`、`--model-out`、`--test-size`、`--random-state` 參數調整輸入與訓練設定。Logistic Regression 模型會輸出至 `artifacts/logreg_model.pkl`，若檔案不存在，Streamlit 介面會提示使用者需先訓練模型。執行 `models/evaluate_models.py` 會讀取所有已訓練模型，並在相同的測試切分上輸出精確率、召回率與 F1 的比較報表，缺少模型檔時則會跳過並顯示警告訊息。

## 資料探索 (EDA)

- 探索式資料分析 Notebook 位於 `notebooks/sms_spam_eda.ipynb`，可使用 VS Code 的 Jupyter 支援或下列指令開啟：
  ```bash
  jupyter notebook notebooks/sms_spam_eda.ipynb
  ```
- Notebook 會自動載入 `dataset/sms_spam.csv`、計算標籤分布、訊息長度統計與常見詞彙，並產生對應圖表。若資料集不存在，第一個讀取儲存格會提示先執行 `python ingest/download_dataset.py`。

## 專案結構

- `ingest/`：資料下載腳本，負責將公開資料集保存為本地 CSV。
- `preprocessing/`：資料前處理與 TF-IDF 向量化腳本，並將特徵與向量器輸出至 `artifacts/`。
- `models/`：SVM、Logistic Regression 等模型的訓練腳本，以及統一的比較工具。
- `pages/`：Streamlit 多頁應用程式的資料分析與模型表現頁面。
- `dataset/`：儲存原始資料集的資料夾。
- `artifacts/`：保存前處理產物與模型檔案。
- `app.py`：Streamlit 主程式，提供繁體中文 UI、側邊欄範例及即時翻譯功能。
- `requirements.txt`：專案依賴套件清單。
