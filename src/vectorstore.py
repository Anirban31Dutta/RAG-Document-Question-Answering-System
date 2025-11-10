import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

        # Load PDF and chunk text
        self.docs = self.load_and_chunk_pdf(self.pdf_path)

        # Load embedding model
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

        # Build vector index
        self.build_index()

    def load_and_chunk_pdf(self, file_path, chunk_size=500):
        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        words = text.split()
        chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
        return chunks

    def embed_text(self, text_list):
        return self.model.encode(text_list)

    def build_index(self):
        self.embeddings = self.embed_text(self.docs)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)

        self.index.add(self.embeddings)

    def search(self, query, top_k=3):
        query_vec = self.embed_text([query])
        distances, indices = self.index.search(query_vec, top_k)

        results = [self.docs[i] for i in indices[0]]
        return results
