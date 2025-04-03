# Marketing-Chatbot
# 📊 AI-Powered Marketing Strategy Chatbot

## 🚀 Overview
This AI-powered chatbot analyzes sales data from **PDF or Excel files** and generates **real-time marketing strategies**. It extracts user interaction data, identifies trends, and suggests strategies using Google's Gemini AI model.

## 🛠 Features
- **Upload PDF/Excel** files to extract and analyze sales data.
- **Real-time AI-powered strategy generation** based on user interactions.
- **Progress bar** to track analysis and strategy creation.
- **Target audience segmentation, ad campaigns, and growth recommendations** included in strategies.

---
## 🏗 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/AnubhavDubey23/Marketing-Chatbot.git
cd Marketing-Chatbot
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**
Create a **.env** file in the project directory based on **.env.example**:
```sh
cp .env.example .env
```
Edit `.env` and add your **Gemini API Key**:
```
GEMINI_API_KEY=your_google_gemini_api_key
```

### **4️⃣ Run the Chatbot**
```sh
streamlit run app.py
```
The chatbot will launch in your browser!

---
## 🏗 Project Structure
```
Marketing-Chatbot/
│── app.py                 # Streamlit app (frontend)
│── chatbot.py             # AI-powered strategy generator
│── data_processor.py      # Extracts and processes uploaded data
│── data_generation.py     # Generates sample sales data
│── requirements.txt       # Project dependencies
│── .env.example           # Environment variables template
│── README.md              # Project documentation
└── data/                  # Sample data folder
```

---
## 📂 How It Works
1. **User uploads** a PDF or Excel file containing sales data.
2. **Data is extracted** using `data_processor.py`.
3. **AI analyzes trends** (top-selling products, peak purchase time, etc.).
4. **A marketing strategy is generated** using Google's Gemini AI.
5. **Results are displayed** in the chatbot interface.

---
## 🤖 Technologies Used
- **Python** 🐍
- **Streamlit** 🎨 (Frontend UI)
- **Google Gemini AI** 🤖 (AI-powered text generation)
- **Pandas** 📊 (Data processing)
- **OpenAI GPT API** (LLM-based insights)

---
## 🌍 Deployment
To deploy this chatbot online:
1. Use **Streamlit Cloud**, **Render**, or **Google Cloud Run**.
2. Ensure your API keys are set as **environment variables**.
3. Push updates using Git:
   ```sh
   git add .
   git commit -m "Updated chatbot functionality"
   git push origin main
   ```

---
## 📜 License
This project is open-source under the **MIT License**.

---
## 🛠 Future Enhancements
- **Better error handling** for incorrect file formats.
- **Data visualization** for sales insights.
- **Multilingual support** for global strategy recommendations.

### 🔥 Enjoy generating marketing strategies with AI! 🚀
