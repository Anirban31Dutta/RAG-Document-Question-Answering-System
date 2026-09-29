# 📄 RAG Document Question Answering System

**Ask questions about your PDF documents and get answers using AI.**

A document question-answering application built with Streamlit, FAISS, and transformer models. Upload a PDF, retrieve relevant text from the document, and generate answers based on its content.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/FAISS-Vector%20Search-green" alt="FAISS">
  <img src="https://img.shields.io/badge/AI-FLAN--T5-orange" alt="FLAN-T5">
</p>

---

## ✨ Features

* 📂 **PDF Upload:** Upload a PDF document directly through the web interface.
* 📝 **Text Extraction:** Extract text from PDF pages using PyMuPDF.
* ✂️ **Text Chunking:** Divide document text into smaller chunks for retrieval.
* 🧠 **Text Embeddings:** Convert document chunks into numerical representations using Sentence Transformers.
* 🔍 **Semantic Search:** Use FAISS to find relevant document sections.
* 💬 **AI-Generated Answers:** Generate answers using the FLAN-T5-base model.
* 🖥️ **Interactive Interface:** Use the application through a simple Streamlit web interface.

## 🛠️ Tech Stack

| Technology            | Purpose                                    |
| --------------------- | ------------------------------------------ |
| Python                | Core programming language                  |
| Streamlit             | Web application interface                  |
| PyMuPDF               | Extract text from PDF files                |
| Sentence Transformers | Generate text embeddings                   |
| FAISS                 | Similarity search over document embeddings |
| FLAN-T5-base          | Generate answers from retrieved context    |
| NumPy                 | Numerical operations                       |

## ⚙️ How It Works

The application follows a Retrieval-Augmented Generation (RAG)-style workflow:

1. **Upload a PDF** — Select a document using the Streamlit interface.
2. **Extract text** — Read the text from the PDF pages.
3. **Create chunks** — Split the extracted text into chunks of approximately 500 words.
4. **Generate embeddings** — Convert each chunk into a vector using `all-MiniLM-L6-v2`.
5. **Build the index** — Store the vectors in a FAISS index.
6. **Retrieve context** — Search for the three most relevant chunks based on the question.
7. **Generate an answer** — Pass the question and retrieved context to FLAN-T5-base.
8. **Display the result** — Show the retrieved text and generated answer in the application.

## 📁 Project Structure

```text
RAG-Document-Question-Answering-System/
│
├── src/
│   ├── app.py              # Streamlit application
│   ├── vectorstore.py      # PDF processing and FAISS search
│   └── chatbot.py          # Cohere-based chatbot implementation
│
├── requirements.txt        # Python dependencies
├── .gitattributes          # Git text-file configuration
├── LICENSE                 # Project license
└── README.md               # Project documentation
```

*Note: This structure reflects the intended organization. Adjust the paths if your files are arranged differently in the repository.*

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Anirban31Dutta/RAG-Document-Question-Answering-System.git
```

Navigate into the project directory:

```bash
cd RAG-Document-Question-Answering-System
```

### 2. Create a virtual environment

```bash
python -m venv rag_env
```

Activate it on Windows:

```bash
rag_env\Scripts\activate
```

On macOS or Linux:

```bash
source rag_env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The current application also imports packages for FAISS, Transformers, and NumPy. If they are not already listed in your `requirements.txt`, install them:

```bash
pip install faiss-cpu transformers torch numpy
```

### 4. Run the application

If your Streamlit file is located in `src/`:

```bash
streamlit run src/app.py
```

If `app.py` is in the repository root, use:

```bash
streamlit run app.py
```

### 5. Ask questions

1. Open the local URL displayed in your terminal.
2. Upload a PDF document.
3. Wait for the document to be indexed.
4. Enter a question about the document.
5. Review the retrieved context and generated answer.

## 🧪 Example

Imagine uploading a PDF about machine learning.

**Question:**

```text
What is supervised learning?
```

**Application workflow:**

* Searches the document for relevant text.
* Retrieves the top three matching chunks.
* Uses the retrieved context to generate an answer.

The response depends on the information available in the uploaded document.

## 📦 Models Used

| Model                                    | Usage                                           |
| ---------------------------------------- | ----------------------------------------------- |
| `sentence-transformers/all-MiniLM-L6-v2` | Converts text into embeddings                   |
| `google/flan-t5-base`                    | Generates answers from the question and context |

The models are loaded through their respective Python libraries. The first run may require downloading model files, depending on whether they are already available locally.

## ⚠️ Limitations

* The application works with PDF files and depends on extractable text.
* Scanned PDFs may require OCR, which is not currently implemented.
* Answer quality depends on the document's content and the retrieved chunks.
* The current implementation processes one uploaded document at a time.
* Large PDFs may require additional memory and processing time.
* The current answer-generation pipeline is designed as a demonstration and may occasionally produce incomplete or inaccurate answers.

## 🔮 Future Improvements

* Support multiple PDF documents.
* Add OCR for scanned documents.
* Display page numbers and source references for answers.
* Improve chunking with overlapping text chunks.
* Add conversation history and a chat-style interface.
* Improve error handling for empty or unreadable PDFs.
* Integrate the Cohere chatbot implementation into the main application.

## 👨‍💻 Author

**Anirban Dutta**

* GitHub: [Anirban31Dutta](https://github.com/Anirban31Dutta)

## 📜 License

This project is distributed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
