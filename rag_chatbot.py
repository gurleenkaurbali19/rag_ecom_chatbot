import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Loading the data
with open("ecom_data_qa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extracting Q&A pairs
questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Loading sentence transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# Vectorizing questions
embeddings = model.encode(questions, convert_to_numpy=True)

# Creating FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Session state per user (temporary, per runtime only)
session_state = {
    "context": None,
    "product": None,
    "awaiting_followup": False
}

import re

def get_answer(query):
    query_lower = query.lower()

    # Checking if user is introducing themselves
    name_match = re.search(r"(?:my name is|i am|i’m|this is|its)\s+(\w+)", query_lower)
    if name_match:
        name = name_match.group(1).capitalize()
        return f"Hello {name}, how can I help you today? 😊"

    # Detecting selling intent
    if any(keyword in query_lower for keyword in ["sell", "i want to sell", "i need to sell"]):
        if "phone" in query_lower or "mobile" in query_lower:
            session_state["context"] = "selling"
            session_state["product"] = "mobile"
            session_state["awaiting_followup"] = True
            return ("Great! I can help you sell your mobile.\n"
                    "Could you please answer a few quick questions?\n"
                    "1. What's your phone’s battery health?\n"
                    "2. Are all buttons working properly?\n"
                    "3. Any physical damage like scratches or cracks?")

        elif "laptop" in query_lower:
            session_state["context"] = "selling"
            session_state["product"] = "laptop"
            session_state["awaiting_followup"] = True
            return ("Sure, I can help you sell your laptop.\n"
                    "Please answer a few quick questions:\n"
                    "1. What's the battery backup?\n"
                    "2. Is the screen or keyboard damaged?\n"
                    "3. Any heating or performance issues?")

    # Handle follow-up answers
    if session_state.get("awaiting_followup"):
        good_keywords = ["no damage", "all buttons working", "good", "working fine", "screen fine", "battery is good", "no scratches"]
        if any(kw in query_lower for kw in good_keywords):
            product = session_state.get("product", "product")
            # Reset session after reply
            session_state["awaiting_followup"] = False
            session_state["context"] = None
            session_state["product"] = None
            return (f"Awesome! It sounds like your {product} is in good condition. 🎉\n"
                    "You can list it on our platform here: [Sell Your Gadget](https://gadgetguruz.com/sell)")
        else:
            return "Got it! Please share more about the condition — any damage, battery issues, or other concerns?"

    # FAISS fallback
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)

    if D[0][0] < 1.0:
        return answers[I[0][0]]
    else:
        return (
            "Hmm, I couldn’t find an exact answer to your question. But don’t worry! "
            "You can reach our support team directly at:\n"
            "📞 +91-9876543210\n📧 support@gadgetguruz.com"
        )
