# 🤖 Thoughtful AI Support Agent

A simple AI-powered customer support assistant for Thoughtful AI. It uses hardcoded Q&A pairs for common questions and falls back to GPT-3.5 for everything else.

Built with Python and Streamlit for a clean and interactive web interface.

---

## 🧠 Features

- ✅ Hardcoded responses for known Thoughtful AI questions  
- 💬 Fallback to OpenAI GPT-3.5 for general queries  
- 🌐 Gradio-based conversational interface  
- 🔒 Environment variables managed with `.env`  

---

## 📁 Project Structure

.
├── app.py # Streamlit app entry point
├── utils.py # Contains response logic
├── qa_data.py # Static question-answer dataset
├── .env.example # Environment variable template
├── requirements.txt # Python package requirements
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/engineer718/thoughtfulai.git

### 2. Install Python Dependencies

pip install -r requirements.txt

### 3. Add Your OpenAI API Key
Create a .env file in the root directory based on the provided template:

cp .env.example .env
Inside .env:

OPENAI_API_KEY=sk-xxxxxx // Paste your OpenAI API Key here

### 4. ▶️ Run the App

streamlit run app.py
This will launch the Gradio UI in your browser at http://localhost:8501

🧪 Example Questions
What does the eligibility verification agent (EVA) do?

What does the claims processing agent (CAM) do?

Tell me about Thoughtful AI’s Agents

What are the benefits of using Thoughtful AI’s agents?
