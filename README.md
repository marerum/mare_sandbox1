# Supabase バーコードスキャナープロジェクト

## 📁 プロジェクト構造

```
Supabase_try0.1/
├── .env                           # 環境変数設定
├── .gitignore                     # Git除外設定
├── .venv/                        # Python仮想環境
│
├── 🟢 メインファイル（現在使用中）
├── supabase_sign_intry.py        # 認証システム
├── image_management_system.py     # 画像管理システム（デモ版）
├── BarcodesupaDB_3.py           # バーコードDB統合システム
├── simple_barcode_scanner.py     # シンプルバーコードスキャナー
├── ai_image_generator.py         # AI画像生成フレームワーク
├── BarcodeupaDBbyJP.ipynb       # Jupyter ノートブック版
│
├── 📂 archive/                   # 過去バージョン・開発用ファイル
├── 📂 production/               # 本番用ファイル
├── 📂 sql/                      # データベース設定SQL
└── 📂 data/                     # CSVデータファイル
```

## 🚀 使用方法

### メイン機能の起動
```bash
# 画像管理システム（デモ版）
streamlit run image_management_system.py

# 認証システム
streamlit run supabase_sign_intry.py

# バーコードDB統合システム
streamlit run BarcodesupaDB_3.py

# シンプルバーコードスキャナー
streamlit run simple_barcode_scanner.py
```

### 本番環境への移行
```bash
# 本番用認証システム
streamlit run production/secure_image_management.py
```

## 📂 ディレクトリ詳細

### `/archive/` - アーカイブファイル
- 開発過程で作成されたファイル
- 過去バージョンのコード
- テスト用ファイル

### `/production/` - 本番用ファイル
- 認証必須のセキュアなシステム
- 本番環境向けの設定

### `/sql/` - データベース設定
- Supabase用SQL設定ファイル
- RLS（Row Level Security）ポリシー
- テーブル作成スクリプト

### `/data/` - データファイル
- ダミーデータCSV
- エクスポートデータ

## 🔧 環境設定

1. `.env` ファイルに以下を設定：
```
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_anon_key
JANCODE_LOOKUP_APP_ID=your_app_id
```

2. 必要なライブラリをインストール：
```bash
pip install streamlit supabase python-dotenv pillow requests pandas
```

## 📝 ファイル移動時の注意

- **ルートディレクトリでの実行が必要**: `.env` ファイルへのアクセスのため
- **サブディレクトリから実行する場合**: 
  ```bash
  # productionディレクトリから実行する場合の例
  cd production
  streamlit run secure_image_management.py --server.fileWatcherType none
  ```
  ただし、`.env` ファイルが見つからないエラーが発生する可能性あり

## 🎯 推奨使用パターン

1. **開発・テスト**: ルートディレクトリから `image_management_system.py` を実行
2. **本番使用**: SQL設定完了後、`production/secure_image_management.py` を実行
3. **機能確認**: 各機能を個別に `simple_barcode_scanner.py` 等で確認