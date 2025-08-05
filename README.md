# 🤖 RAG E-Commerce Chatbot

This is a Retrieval-Augmented Generation (RAG)-style chatbot designed to help users with e-commerce queries like order issues, refunds, delivery, and product selling. The chatbot uses FAISS for fast semantic search and a SentenceTransformer for vector embeddings, all wrapped in a simple Gradio UI.

---

## 🚀 Features

- ✅ Instant responses for FAQs (e.g., order status, refund policy)
- 📦 Selling logic with follow-up questions based on product (mobile/laptop)
- 💬 Personalized greetings (detects "Hi, I'm Gurleen" and replies)
- 🧠 FAISS vector similarity search with fallback support contact
- 🖼️ Clean and user-friendly Gradio UI

---

## 📁 Project Structure
```
rag_ecom_chatbot/
├── app.py # Main Gradio UI
├── rag_chatbot.py # RAG chatbot logic (embedding, faiss, follow-up)
├── ecom_data_qa.json # Static QA data used for semantic search
├── requirements.txt # Python dependencies
└── README.md # Project overview & setup instructions
```

---

## 🔧 How to Run the Project Locally

### 🛠️ Prerequisites

- Python 3.8 or higher
- Git installed

---

### 🧪 1. Clone the Repository

```bash
git clone https://github.com/gurleenkaurbali19/rag_ecom_chatbot.git
cd rag_ecom_chatbot
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Chatbot
```
python app.py
```
The chatbot will launch at: http://127.0.0.1:7860

🙋‍♀️ Notes
The chatbot works fully locally – no APIs or cloud models required.
Includes follow-up logic for product selling conversations (mobile/laptop).
If the bot can't answer, it provides a fallback response with contact info.

🧑‍💻 Author
Made by Gurleen Kaur Bali
