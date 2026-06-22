import streamlit as st

from config import (
    GROQ_API_KEY,
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from utils.ui import (
    apply_css,
    sidebar,
    initialize_session,
    render_chat,
    welcome_message,
    clear_chat,
)

from utils.chat import create_llm, process_chat
from utils.pdf_loader import process_uploaded_pdf


# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
)

apply_css()

initialize_session()


# ----------------------------
# Sidebar
# ----------------------------

(
    uploaded_file,
    model,
    temperature,
    max_tokens,
    clear_button,
) = sidebar()


if clear_button:
    clear_chat()
    st.rerun()


# ----------------------------
# LLM
# ----------------------------

llm = create_llm(
    api_key=GROQ_API_KEY,
    model=model,
    temperature=temperature,
    max_tokens=max_tokens,
)


# ----------------------------
# PDF Processing
# ----------------------------

if uploaded_file:

    process_uploaded_pdf(uploaded_file)


# ----------------------------
# Main UI
# ----------------------------

st.title("🤖 AI Chatbot")

st.caption(
    "Powered by LangChain + Groq + Streamlit"
)


render_chat()

welcome_message()


# ----------------------------
# Chat
# ----------------------------

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    process_chat(
        prompt,
        llm,
    )