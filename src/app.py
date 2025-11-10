import streamlit as st
from vectorstore import VectorStore
from transformers import pipeline

st.set_page_config(page_title="RAG Document Q&A", layout="wide")

def main():
    st.title("📄 RAG Document Question Answering System (Offline - FAISS)")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Save uploaded PDF locally
        pdf_path = "uploaded_document.pdf"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success("PDF uploaded successfully.")

        # Initialize Vector Store
        with st.spinner("Indexing document..."):
            vectorstore = VectorStore(pdf_path)
        st.success("Document indexed. You can now ask questions!")

        # Question input
        user_question = st.text_input("Ask a question about the document:")

        if user_question:
            with st.spinner("Searching relevant document sections..."):
                results = vectorstore.search(user_question, top_k=3)

            st.write("### Retrieved Context 🔍")
            for r in results:
                st.write("- " + r)

            # Local answer generation (small offline model for demo)
            with st.spinner("Generating answer..."):
                generator = pipeline("text2text-generation", model="google/flan-t5-base")
                prompt = f"Answer the question based on the context.\nQuestion: {user_question}\nContext: {' '.join(results)}"
                answer = generator(prompt, max_length=150)[0]['generated_text']

            st.write("### ✅ Answer")
            st.write(answer)

if __name__ == "__main__":
    main()
