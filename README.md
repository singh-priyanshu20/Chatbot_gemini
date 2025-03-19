#  Gemni - AI Chatbot  

A modular AI chatbot built using **Google Gemini API, LangChain, and Streamlit**.

---

## **1️⃣ Setup Environment (Using Conda)**  
First, create and activate a **Conda environment**:  
```bash
conda create --name first_gemni python=3.9 -y
conda activate first_gemni
```

```bash
pip install -r requirements.txt
```

```bash
streamlit run main.py
```

```bash
first_gemni/
│── main.py               # Streamlit app UI
│── config.py             # API configurations
│── langchain_utils.py    # LangChain model & processing
│── requirements.txt      # Dependencies
│── .env                  # Store API Keys
```
