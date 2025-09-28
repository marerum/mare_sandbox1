import streamlit as st

st.title("🧪 デプロイテスト")
st.success("✅ アプリは正常に起動しています！")

# 環境チェック
import sys
st.write(f"Python バージョン: {sys.version}")

# パッケージチェック
try:
    import numpy
    st.success("✅ numpy: OK")
except ImportError:
    st.error("❌ numpy: インポートエラー")

try:
    import PIL
    st.success("✅ PIL: OK")
except ImportError:
    st.error("❌ PIL: インポートエラー")

try:
    import pyzbar
    st.success("✅ pyzbar: OK")
except ImportError as e:
    st.warning(f"⚠️ pyzbar: {e}")

# 簡単なSecretsテスト
try:
    test_secret = st.secrets.get("TEST_KEY", "デフォルト値")
    st.info(f"Secrets テスト: {test_secret}")
except Exception as e:
    st.warning(f"Secrets エラー: {e}")

st.markdown("---")
st.info("💡 このページが表示されれば、基本的なデプロイは成功しています。")