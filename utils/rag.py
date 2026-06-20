from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Use ONLY the information provided in the context below to answer the user's question.

If the answer is not found in the context, respond exactly with:

"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}
"""
)


def get_rag_response(
    vector_store,
    llm,
    question: str,
):
    """
    Retrieve relevant document chunks and stream an answer.
    """

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    documents = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    chain = RAG_PROMPT | llm

    return chain.stream(
        {
            "context": context,
            "question": question,
        }
    )