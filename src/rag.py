from src.embedding import model
from src.retriever import collection
from src.gpt import generate_text


def ask_rag(question):

    # =========================
    # 1. 用户问题 embedding
    # =========================
    query_embedding = model.encode(question).tolist()

    # =========================
    # 2. Chroma 检索
    # =========================
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    documents = results["documents"][0]

    # =========================
    # 3. 拼接 context
    # =========================
    context = "\n".join(documents)

    # =========================
    # 4. Prompt
    # =========================
    prompt = f"""
You are an AI archive assistant for a contemporary artist.

Use the following archive materials to answer the question.

Archive:
{context}

Question:
{question}

Answer professionally.
"""

    # =========================
    # 5. GPT生成
    # =========================
    answer = generate_text(prompt)

    return answer