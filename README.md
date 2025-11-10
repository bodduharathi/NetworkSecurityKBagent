# CS5342 – Network Security Tutor & Quiz Assistant

> A privacy-first intelligent tutor and quiz assistant built for the **CS5342 Network Security (Fall 2025)** course. The entire system operates locally, ensuring that no data leaves the user’s device.

---

## 🚀 Core Features

- **Smart Tutoring** – Responds to course questions using citations from lecture notes.
- **Dynamic Quiz Builder** – Generates custom quizzes with multiple-choice, true/false, and open-ended questions.
- **Auto-Grading** – Evaluates user answers and provides instant, detailed feedback.
- **Fully Offline** – All processes occur locally for complete privacy.

----

## ⚙️ System Requirements

| Component            | Recommended Version                                 |
| -------------------- | --------------------------------------------------- |
| **Operating System** | Windows 10 / Ubuntu 20+ / macOS                     |
| **Python**           | 3.9 – 3.11                                          |
| **Memory (RAM)**     | Minimum: 8 GB • Recommended: 16 GB                  |
| **Storage**          | ≥ 5 GB free space                                   |
| **Dependencies**     | Listed in `requirements.txt`                        |
| **GPU (Optional)**   | CUDA-supported GPU for faster embedding computation |

---

## 🧮 Libraries Used

| Library                 | Function                                                   |
| ----------------------- | ---------------------------------------------------------- |
| `streamlit`             | User interface for quiz and tutor operations               |
| `sentence-transformers` | Converts text into embeddings                              |
| `chromadb`              | Handles local embedding storage and retrieval              |
| `pypdf`                 | Extracts text content from lecture PDFs                    |
| `numpy`, `scikit-learn` | Handles preprocessing, vector comparison, and calculations |
| `os`, `json`, `random`  | Manages files and quiz logic                               |

All dependencies can be installed via `requirements.txt`.

---

## 🏗️ System Overview

Main components include:

1. **Streamlit UI** – Interface for Tutor and Quiz modes.
2. **Sentence-Transformer Engine** – Generates 768-dimensional text embeddings.
3. **ChromaDB Vector Store** – Stores and fetches relevant chunks based on user queries.
4. **Local Language Model** – Generates accurate, context-aware responses.
5. **Knowledge Repository** – Lecture slides and textbook PDFs used as the local training base.

### Workflow Summary

1. User enters a query in Streamlit.
2. Query is embedded using Sentence-Transformers.
3. ChromaDB retrieves relevant data chunks.
4. LLM merges context + query to produce a citation-backed answer.
5. The result is displayed as text, quiz, or feedback.

![System Architecture]
C:\Users\Yaswitha\Desktop\CS5342-Network-Security-main\data\images\Architecture_image.jpeg

**Figure 1:** Data flow in the Local Network Security Tutor & Quiz Assistant

---

## 🔁 Execution Steps

Follow this order to run the system:

1. **Clone Repository** – Download project code from GitHub.
2. **Set Up Virtual Environment** – Create and activate an isolated Python environment.
3. **Install Dependencies** – Use `pip install -r requirements.txt`.
4. **Run `ingest.py`** –
   - Extracts text from PDFs
   - Splits content into 500-word segments
   - Generates and stores embeddings using ChromaDB
   - Must be executed **once** before running the app
5. **Launch `app.py`** –
   - Starts the Streamlit interface
   - Loads local embeddings for quiz and tutoring modes
6. **Use the App** –
   - Tutor mode for Q&A
   - Quiz mode for question generation and grading
   - Feedback and citations appear locally

---

## 🧪 How to Run

```bash
# 1. Clone repository
git clone https://github.com/<groupname>/<repo>.git
cd <repo>

# 2. Create virtual environment
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (macOS/Linux)
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run data ingestion
python ingest.py

# 5. Launch Streamlit app
streamlit run app.py
```

Access the app at **http://localhost:8501**.

---

## 🧪 Example Use Cases

- "Define Entropy"
- “Create a quiz with 5 questions about attacks.”
- “Evaluate my quiz using Grade Quiz”

## 🎥 Demo

📹 **Video Demo:** [https://drive.google.com/file/d/1YS20XoCSJZBoZA3ORRyQYxwEXvtArVPN/view?usp=sharing]  
_(Demonstrates installation, tutor mode, quiz generation, and response flow.)_

---

## ⚠️ Common Issues and Fixes

| Issue                                    | Fix                                            |
| ---------------------------------------- | ---------------------------------------------- |
| Streamlit freezes on long responses      | Added caching and capped output at 500 tokens  |
| Embeddings not saved                     | Used `persist_directory='./chroma_db'`         |
| PDF text extraction fails for some files | Enabled `strict=False` in PyPDF                |
| Quiz scores not updating                 | Used Streamlit `session_state` for persistence |
| Embedding generation is slow             | Batched embeddings and saved incrementally     |

---

## 💡 Future Enhancements

Integrate GPU acceleration to significantly speed up model inference.

Implement real-time progress tracking and interactive performance dashboards.

Introduce additional quiz formats such as fill-in-the-blank and case-based assessments.

Incorporate voice-enabled feedback to enhance accessibility and user engagement.

**Team Learnings**

- Improved understanding of **RAG (Retrieval-Augmented Generation)**.
- Gained hands-on experience with open-source embeddings and ChromaDB.
- Learned advanced debugging and state management in Streamlit.

---

## 📊 Data and Training Setup

- **Knowledge Sources:** CS5342 lecture slides and textbook chapters (PDFs).
- **Preprocessing:** Converted to text and split into ~500-word chunks.
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`.
- **Vector Database:** Local ChromaDB (`persist_directory='./chroma_db'`).
- **Usage:** Context retrieval for generating Tutor and Quiz responses—fully offline.

---

## 📚 References

1. [Streamlit Docs](https://docs.streamlit.io)
2. [Medium – Building a RAG Chatbot (2025)](https://medium.com/@yuhongsun/how-i-built-a-rag-based-ai-chatbot-from-my-personal-data-2025)
3. [Composio – Building MCP Agents (2025)](https://www.composio.dev/blog/the-complete-guide-to-building-mcp-agents)
4. [LangGraph Guide – Data Science Collective (2025)](https://datasciencecollective.medium.com/the-complete-guide-to-building-your-first-ai-agent-with-langgraph-2025)
5. [YouTube – How to Build AI Chatbots (2025)](https://www.youtube.com/watch?v=JxgmHe2NyeY)
6. [Microsoft Tech Community – Azure OpenAI + ChromaDB + Chainlit](https://techcommunity.microsoft.com/)
7. [Beebom – ChatGPT API Chatbot (2023)](https://beebom.com/how-build-ai-chatbot-chatgpt-api/)
8. [CommandBar Blog – LangChain for Product Teams](https://www.commandbar.com/blog/langchain-product-people)
9. [Medium – Host Llama 2 on GPU for Free](https://medium.com/@yuhongsun/host-a-llama-2-api-on-gpu-for-free)
10. [ChromaDB Documentation](https://docs.trychroma.com)

---

## 👥 Team Members

- Yaswitha Ramisetty
- Harathi Boddu
- Snehitha Chava
- Rajasri Kondaveeti
- Cuma Cagri Mercan
- Jyothimanohar Reddy Pothireddy
- Natalie Hurt
