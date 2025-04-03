import os
import pandas as pd
import google.generativeai as genai
from data_processor import extract_data_from_file
import streamlit as st
from dotenv import load_dotenv  # ✅ Load environment variables

# Load API key from .env file
load_dotenv()  # ✅ This loads the .env variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("❌ Missing GEMINI_API_KEY. Set it as an environment variable.")

genai.configure(api_key=GEMINI_API_KEY)

def generate_marketing_strategy_from_file(file):
    """Extracts data, analyzes it, and generates a marketing strategy."""
    
    df = extract_data_from_file(file)
    
    if df is None or df.empty:
        return "❌ No valid data found in the file."

    # Show progress bar
    progress = st.progress(20, text="📊 Analyzing sales trends...")

    # Extended Data Analysis
    location_counts = df["user_location"].value_counts().to_dict()
    product_counts = df["product_purchased"].value_counts().to_dict()

    # Detect peak purchase time (if time data exists)
    if "interaction_time" in df.columns:
        df["interaction_time"] = pd.to_datetime(df["interaction_time"])
        peak_time = df["interaction_time"].dt.hour.mode()[0]
    else:
        peak_time = "Unknown"

    progress.progress(50, text="🤖 Generating AI-powered strategy...")

    prompt = f"""
    Given the following market insights:
    - Top sales location: {max(location_counts, key=location_counts.get)}
    - Best-selling product: {max(product_counts, key=product_counts.get)}
    - Purchase breakdown: {product_counts}
    - Peak purchase hour: {peak_time}

    Craft a **detailed marketing strategy** to increase sales. 
    Include: 
    - Target audience segmentation
    - Recommended ad campaigns
    - Pricing strategies
    - Growth opportunities
    """

    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        progress.progress(100, text="✅ Strategy Ready!")
        return response.text
    except Exception as e:
        return f"❌ Error generating strategy: {e}"
