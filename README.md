# Gen-AI Learning

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

A hands-on learning repository tracking the full journey through the **Generative AI / RAG (Retrieval-Augmented Generation) pipeline** — from raw text to LLM-powered answers.

Each topic folder contains Jupyter notebooks, sample data files, and small scripts that build on one another:

```
Text normalization → Chunking → Embeddings → LLMs → RAG architecture
```

## Repository structure

| Folder | Topic | Key files |
|---|---|---|
| [`Text_normalization/`](Text_normalization/) | Cleaning raw text: removing noise, expanding abbreviations, correcting spelling | `clean.py`, `text_clean.ipynb`, `correcting_words.ipynb`, `expandword_abb.ipynb` |
| [`Text_normalization/NLP/`](Text_normalization/NLP/) | Classic NLP with NLTK & spaCy: stopwords, stemming, lemmatization | `nltk_stopwords.ipynb`, `nltk_stemming.ipynb`, `spacy.ipynb`, `lemmatization.py` |
| [`Chunking/`](Chunking/) | Splitting documents into chunks for retrieval (fixed-size and recursive splitting) | `split.ipynb`, `task.ipynb`, `recrusive_loader.ipynb` |
| [`Embeddings/`](Embeddings/) | Generating embeddings (Sentence Transformers) and storing them in a vector DB (FAISS) | `Embedding_modules/ST.ipynb`, `Embedding_modules/vector_db.ipynb` |
| [`LLM/`](LLM/) | Calling LLMs: Google Gemini, Hugging Face, and local Ollama models | `gemini_llm.ipynb`, `huggingface_llm.ipynb`, `ollama_llm.ipynb`, `loader.ipynb` |
| [`Rag_archi/`](Rag_archi/) | Building RAG pipelines: retrieval + generation architecture | `rag_architecture.ipynb`, `rag.ipynb`, `rag_archi_2/` |
| [`mini_rag_project/`](mini_rag_project/) | A minimal end-to-end RAG project (vectorizer + KNN retrieval) | `vectorizer/embedding.ipynb` |

Root-level files (`workout.ipynb`, `data.txt`, `token_data.txt`, etc.) are standalone experiments and sample data used across the notebooks.

## Getting started

Requires **Python 3.12+**.

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install the pinned dependencies (versions are exact, see requirements.txt)
pip install -r requirements.txt

# 3. Download the NLTK and spaCy data used in the NLP notebooks
python -m spacy download en_core_web_sm
```

## Running the notebooks

```bash
jupyter notebook
```

Open the notebooks inside each topic folder and run the cells top to bottom. The `.txt` files next to each notebook are the sample inputs the cells read from.

## API keys & security

The `LLM/` notebooks call hosted models. **Never hardcode API keys** — the notebooks read them from environment variables. Set your keys before running:

```bash
# Linux / macOS
export GOOGLE_API_KEY="your-key-here"
export HF_TOKEN="your-hf-token-here"

# Windows (PowerShell)
$env:GOOGLE_API_KEY = "your-key-here"
$env:HF_TOKEN = "your-hf-token-here"
```

Or create a `.env` file (already ignored by `.gitignore`) and load it in the notebook:

```env
GOOGLE_API_KEY=your-key-here
HF_TOKEN=your-hf-token-here
```

> ⚠️ **Security note:** keys committed to a public repo are immediately exposed. This repository's `.gitignore` excludes `.env`, `.env.*`, and certificate/key files, and all notebooks reference keys via `os.environ` only. If you ever leak a key, revoke it in the provider dashboard and rotate it.

## Notes

- The Ollama notebook requires [Ollama](https://ollama.com) installed locally with a model pulled (e.g. `ollama pull llama3`).
- The `Text_normalization/NLP/` notebooks need spaCy's `en_core_web_sm` model (download step above).

## Roadmap

- [x] Text normalization & NLP
- [x] Chunking
- [x] Embeddings & vector DB
- [x] LLM integration (Gemini, Hugging Face, Ollama)
- [x] RAG architecture
- [ ] Full end-to-end RAG app (streamlit UI + chat over documents)