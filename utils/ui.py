import streamlit as st
from config import (
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    MODELS,
)


def apply_css():
    st.markdown(
        """
<style>

/* Main App */
.stApp{
    background-color:#0E1117;
}

/* Chat Messages */
[data-testid="stChatMessage"]{
    border-radius:15px;
    padding:12px;
    margin-bottom:10px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.15);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background-color:#161B22;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:10px;
    font-weight:bold;
}

/* Chat Input */
[data-testid="stChatInput"]{
    border-radius:15px;
}

</style>
""",
        unsafe_allow_html=True,
    )


def sidebar():
    with st.sidebar:
        st.title("⚙️ AI Settings")

        st.divider()

        uploaded_file = st.file_uploader(
            "📄 Upload a PDF",
            type=["pdf"],
        )

        model = st.selectbox(
            "Choose Model",
            MODELS,
            index=MODELS.index(DEFAULT_MODEL),
        )

        temperature = st.slider(
            "Temperature",
            0.0,
            2.0,
            DEFAULT_TEMPERATURE,
            0.1,
        )

        max_tokens = st.slider(
            "Max Tokens",
            100,
            4096,
            DEFAULT_MAX_TOKENS,
            100,
        )

        clear_chat = st.button("🗑️ Clear Chat")

    return (
        uploaded_file,
        model,
        temperature,
        max_tokens,
        clear_chat,
    )


def initialize_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def render_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def welcome_message():
    if len(st.session_state.messages) == 0:
        st.info(
            """
👋 Welcome!

You can ask me about:

- 💻 Programming
- 🤖 AI & Machine Learning
- 📚 Interview Questions
- 🐍 Python
- 🌐 Web Development
- 📄 Resume Help

You can also upload a PDF and ask questions about it!

Start typing below...
"""
        )


def clear_chat():
    st.session_state.messages = []
    st.session_state.chat_history = []

    if "vector_store" in st.session_state:
        del st.session_state["vector_store"]