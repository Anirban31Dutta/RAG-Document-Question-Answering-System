<div align="center">

# 📄🤖 RAG Document Question Answering System

**Upload a PDF, ask questions in plain English, and get answers grounded in your document.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Cohere](https://img.shields.io/badge/LLM-Cohere-39594D)
![Pinecone](https://img.shields.io/badge/Vector%20DB-Pinecone-000000)
![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)

[Features](#-features) · [How It Works](#-how-it-works) · [Quick Start](#-quick-start) · [Project Structure](#-project-structure) · [Troubleshooting](#-troubleshooting)

</div>

---

## 💡 About

This project is a **Retrieval-Augmented Generation (RAG)** chatbot. Instead of guessing, it first *searches your PDF* for the passages most relevant to your question, then uses a language model to write an answer based only on those passages.

It is useful for quickly getting answers out of long documents such as research papers, reports, notes, and manuals, without reading them page by page.

---

## ✨ Features

- 📥 **PDF upload** – extract text from any text-based PDF
- ✂️ **Smart chunking** – long documents are split into small pieces for accurate search
- 🔎 **Semantic search** – finds passages by *meaning*, not just keywords
- 💬 **Grounded answers** – responses are generated from the retrieved parts of your document
- 🖥️ **Simple web interface** – built with Streamlit, no coding needed to use it

---

## 🧠 How It Works

```
 PDF ──► Extract text ──► Split into chunks ──► Create embeddings ──► Store in Pinecone
                                                                            │
 Your question ──► Create embedding ──► Search similar chunks ◄─────────────┘
                                               │
                                               ▼
                                  Cohere LLM writes the answer
                                               │
                                               ▼
                                     Answer shown in Streamlit
```

---

## 🛠 Tech Stack

| Purpose | Technology |
|---|---|
| Web interface | [Streamlit](https://streamlit.io/) |
| Language model | [Cohere](https://cohere.com/) |
| Vector database | [Pinecone](https://www.pinecone.io/) |
| PDF reading | [PyMuPDF](https://pymupdf.readthedocs.io/) |
| Embeddings | [Sentence Transformers](https://www.sbert.net/) |

---

## 🚀 Quick Start

### ✅ Prerequisites

- **Python 3.9 or higher** – check with `python --version`
- **Git** – to download the project
- A free **[Cohere API key](https://dashboard.cohere.com/api-keys)**
- A free **[Pinecone API key](https://app.pinecone.io/)**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Anirban31Dutta/RAG-Document-Question-Answering-System.git
cd RAG-Document-Question-Answering-System
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

> ⏳ The first install (and first run) can take a few minutes because the embedding model is downloaded.

### 4️⃣ Get your API keys

| Service | Where to get it |
|---|---|
| Cohere | [dashboard.cohere.com](https://dashboard.cohere.com/api-keys) |
| Pinecone | [app.pinecone.io](https://app.pinecone.io/) |

Keep both keys handy. Never commit them to GitHub.

### 5️⃣ Run the app

```bash
cd src
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

### 6️⃣ Use it

1. Enter your API keys when the app asks for them
2. **Upload a PDF**
3. Type your question in the box
4. Read the answer generated from your document 🎉

---

## 📁 Project Structure

```
RAG-Document-Question-Answering-System/
├── src/                 # Application source code (Streamlit app + RAG logic)
├── requirements.txt     # Python dependencies
├── LICENSE              # Apache 2.0 license
└── README.md            # You are here
```

---

## 🩺 Troubleshooting

| Problem | Fix |
|---|---|
| `streamlit: command not found` | Activate your virtual environment, then run `pip install -r requirements.txt` again |
| `No such file or directory: app.py` | Make sure you ran `cd src` before `streamlit run app.py` |
| Invalid API key error | Re-copy the key from the Cohere / Pinecone dashboard and check for extra spaces |
| Empty or wrong answers | The PDF may be a scanned image. Use a text-based PDF (you can select the text in it) |
| Slow first start | The embedding model is downloading. Later runs are much faster |
| Port 8501 already in use | Run `streamlit run app.py --server.port 8502` |

---

## 🔮 Future Improvements

- [ ] Support for multiple documents
- [ ] Multi-language documents
- [ ] Export chat history
- [ ] Cloud deployment
- [ ] Support for more vector databases

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

Distributed under the **Apache 2.0 License**. See [`LICENSE`](LICENSE) for details.

---

## 🙏 Acknowledgments

[Cohere](https://cohere.com/) · [Pinecone](https://www.pinecone.io/) · [Streamlit](https://streamlit.io/) · [PyMuPDF](https://pymupdf.readthedocs.io/) · [Sentence Transformers](https://www.sbert.net/)

<div align="center">

⭐ **If this project helped you, please give it a star!** ⭐

</div>
