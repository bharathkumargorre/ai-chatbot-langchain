import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

from utils.rag import get_rag_response


def create_llm(
    api_key,
    model,
    temperature,
    max_tokens,
):
    return ChatGroq(
        api_key=api_key,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        streaming=True,
    )


def process_chat(prompt, llm):
    """
    Handle one complete user interaction.
    """

    if not prompt:
        return

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        full_response = ""

        try:

            # ---------- PDF RAG ----------
            if "vector_store" in st.session_state:

                stream = get_rag_response(
                    st.session_state.vector_store,
                    llm,
                    prompt,
                )

            # ---------- Normal Chat ----------
            else:

                st.session_state.chat_history.append(
                    HumanMessage(content=prompt)
                )

                stream = llm.stream(
                    st.session_state.chat_history
                )

            for chunk in stream:

                if chunk.content:

                    full_response += chunk.content

                    placeholder.markdown(
                        full_response + "▌"
                    )

            placeholder.markdown(full_response)

            st.session_state.chat_history.append(
                AIMessage(content=full_response)
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response,
                }
            )

        except Exception as e:

            st.error(f"Error: {e}")