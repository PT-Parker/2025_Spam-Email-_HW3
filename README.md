# 簡訊垃圾郵件分類器 (Spam SMS Classifier)

## 專案描述

本專案建立了一個以支援向量機 (SVM) 為核心的垃圾簡訊分類流程，涵蓋資料下載、前處理、模型訓練與評估，並透過 Streamlit 打造完整的繁體中文互動式網頁介面，方便快速測試與展示模型成果。

## 主要功能

- 使用 SVM 訓練的垃圾郵件分類模型。
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

## 專案結構

- `ingest/`：資料下載腳本，負責將公開資料集保存為本地 CSV。
- `preprocessing/`：資料前處理與 TF-IDF 向量化腳本，並將特徵與向量器輸出至 `artifacts/`。
- `models/`：基礎 SVM 模型訓練與評估腳本，輸出訓練好的模型檔案。
- `dataset/`：儲存原始資料集的資料夾。
- `artifacts/`：保存前處理產物與模型檔案。
- `app.py`：Streamlit 主程式，提供繁體中文 UI、側邊欄範例及即時翻譯功能。
- `requirements.txt`：專案依賴套件清單。
