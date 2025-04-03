import streamlit as st
from chatbot import generate_marketing_strategy_from_file

st.set_page_config(page_title="AI Marketing Strategy Generator", layout="wide")

st.title("📊 AI-Powered Marketing Strategy Generator")

uploaded_file = st.file_uploader("📂 Upload your PDF or Excel file", type=["pdf", "xlsx"])

if uploaded_file:
    st.info(f"✅ File uploaded: {uploaded_file.name}")
    
    with st.spinner("🔍 Extracting and analyzing data..."):
        strategy = generate_marketing_strategy_from_file(uploaded_file)
    
    if strategy:
        st.success("🎯 Strategy Generated!")
        st.text_area("📢 Marketing Strategy", strategy, height=400)
    else:
        st.error("❌ Failed to generate strategy. Check your data format!")
