import streamlit as st

from src.retriever import add_document, retrieve
from src.gpt import generate_text

# =========================
# Page
# =========================
st.title("AI Creative Assistant")

# =========================
# Session state (避免重复逻辑)
# =========================
if "archive" not in st.session_state:
    st.session_state.archive = ""

# =========================
# Archive input
# =========================
archive_text = st.text_area("Paste archive text")

# =========================
# Save Archive (ONLY ONE ENTRY POINT)
# =========================
if st.button("Save Archive"):
    if archive_text.strip():
        add_document(
            doc_id="archive",
            text=archive_text.strip()
        )
        st.session_state.archive = archive_text.strip()
        st.success("Archive saved.")
    else:
        st.warning("Archive is empty.")

# =========================
# Question input
# =========================
question = st.text_input("Ask a question")

# =========================
# Ask button
# =========================
if st.button("Ask"):

    context = retrieve(question)

    prompt = f"""
You are an AI art archive assistant.

ONLY use archive context.

ARCHIVE:
{context}

QUESTION:
{question}

If answer is not in archive, say: not found in archive
"""

    answer = generate_text(prompt)

    st.subheader("Answer")
    st.write(answer)

# =========================
# Debug (optional)
# =========================
if st.checkbox("Show current archive in memory"):
    st.write(st.session_state.archive)