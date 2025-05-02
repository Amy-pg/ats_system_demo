# ATSポートフォリオシステム

求人情報管理・応募者管理を行うWebアプリケーションです。  
Flask + Bootstrap で構築し、CSVファイルをデータ管理に使用しています。

## 🌐 デモサイト
**[実際に動作するデモを見る](https://ats-system-demo.onrender.com/)**

## 🚀 主な機能

- 求人一覧表示
- 応募フォーム（CSVに応募データ保存）
- 応募者一覧表示
- 応募者詳細表示・ステータス／メモ更新
- 応募者データCSVダウンロード
- Bootstrapで簡易デザイン

## 📸 画面イメージ

![求人一覧](screenshot_jobs.png)
![応募者一覧](screenshot_applicants.png)
![応募者詳細](screenshot_detail.png)

## 📝 インストール・起動方法

```bash
git clone https://github.com/あなたのアカウント/ats_portfolio.git
cd ats_portfolio
python -m venv venv
source venv/bin/activate  # (Windowsなら venv\Scripts\activate)
pip install -r requirements.txt
python app.py

```

ブラウザで http://localhost:5000 にアクセスしてください。

## 🗂 データファイル
data/dummy_jobs.csv … 求人データ

data/applicants.csv … 応募者データ（20件のサンプルあり）

## 📖 備考
ダミーデータ生成用のスクリプト generate_applicants.py も含めています。
機能追加・UI改善など自由にカスタマイズ可能です。