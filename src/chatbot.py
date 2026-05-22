from src.retriever import search_documents
from src.gpt import generate_text


def ask_rag(question):

    # ===== retrieve =====

    results = search_documents(question)

    documents = results["documents"][0]

    context = "\n".join(documents)

    # ===== augmented prompt =====

    prompt = f"""
You are an AI art archive assistant.

Use the following archive context
to answer the question.

Archive Context:
{context}

Question:
{question}

Answer professionally.
"""

    # ===== generation =====

    answer = generate_text(prompt)

    return answer