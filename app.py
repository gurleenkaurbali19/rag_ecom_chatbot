import gradio as gr
from rag_chatbot import get_answer

def respond(message, history):
    response = get_answer(message)
    return response

custom_css = """
* {
    font-size: 18px !important;
    font-family: 'Segoe UI', sans-serif;
}
.gradio-container {
    max-width: 700px;
    margin: auto;
    padding-top: 30px;
}
footer {
    visibility: hidden;
}
"""

gr.ChatInterface(
    fn=respond,
    title="📦 E-Commerce Support ChatBot",
    description="Need help? Ask me anything about your orders, refunds, deliveries, or products!",
    theme=gr.themes.Soft(),  # clean soft theme
    css=custom_css
).launch(share=False)
