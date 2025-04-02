# Green 求人スクレイピングツール

## 📌 プロジェクト概要

このツールは、求人サイト [Green](https://www.green-japan.com/) に掲載されているエンジニア職の求人情報をスクレイピングし、CSVファイルとして保存するPythonスクリプトです。

## 🚀 機能一覧

- 求人タイトル、企業名、求人詳細ページURLを自動収集
- BeautifulSoupでHTML解析
- pandasでCSV保存
- ページ間巡回（今後追加予定）
- （オプション）詳細ページへのアクセス・技術タグ取得（今後追加）

## 🛠️ 使用技術

- Python 3.x
- requests
- BeautifulSoup4
- pandas

## 📂 実行方法

1. 仮想環境の作成・有効化（任意）

```bash
python -m venv venv
source venv/bin/activate  # Windowsは venv\Scripts\activate
