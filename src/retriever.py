import chromadb
from src.embedding import model

# =========================
# ChromaDB client
# =========================
client = chromadb.Client()

collection = client.get_or_create_collection(
    name="art_archive"
)

# =========================
# Add / Update document (FIXED)
# =========================
def add_document(doc_id, text):
    embedding = model.encode(text).tolist()

    # 🔥 关键：用 upsert = 覆盖写入（不是追加）
    collection.upsert(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )


# =========================
# Retrieve documents (FIXED)
# =========================
def retrieve(query, top_k=1):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    # 没有结果
    if not results["documents"] or not results["documents"][0]:
        return "not found in archive"

    # 只返回最相关的一条
    return results["documents"][0][0]


# =========================
# Optional: debug helper
# =========================
def debug_dump():
    return collection.get()