# 📰 AI News Article Summarizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An intelligent, AI-powered article summarizer built with Hugging Face Transformers and Streamlit.**  
Paste any text or drop a URL — get a crisp, abstractive summary in seconds.

[🚀 Quick Start](#️-installation--setup) · [💡 How It Works](#-how-it-works) · [📂 Project Structure](#-project-structure) · [🤝 Contributing](#-contributing)

</div>

---

## ✨ Overview

This project is an end-to-end **NLP summarization pipeline** that transforms long-form news articles into concise, readable summaries. It uses Meta's `facebook/bart-large-cnn` model — a state-of-the-art transformer trained specifically for abstractive summarization — wrapped in a clean, interactive Streamlit UI.

Whether you're keeping up with the news, doing research, or just don't have time to read a 2,000-word article, this tool extracts the key ideas and delivers them in a fraction of the time.

---

## 🎯 Key Features

- 📝 **Dual Input Mode** — Paste raw text directly or provide a news article URL
- 🌐 **Web Scraping** — Automatically extracts article content from URLs using BeautifulSoup
- 🤖 **Abstractive Summarization** — Uses BART to generate new, coherent sentences (not just copy-paste extracts)
- ⚡ **Fast & Interactive** — Streamlit UI with real-time feedback
- 🧩 **Modular Design** — Clean separation between UI (`app.py`) and summarization logic (`main.py`)

---

## 🧠 How It Works

```
User Input (Text or URL)
        │
        ▼
 ┌─────────────────┐
 │  URL Provided?  │
 └────────┬────────┘
    Yes   │   No
          │
    ┌─────▼──────┐        ┌───────────────┐
    │ BeautifulSoup│       │  Raw Text Used │
    │ Web Scraper │       └───────┬────────┘
    └─────┬───────┘               │
          └──────────┬────────────┘
                     ▼
         ┌───────────────────────┐
         │  BART Transformer     │
         │  (bart-large-cnn)     │
         │  Encoder → Decoder    │
         └───────────┬───────────┘
                     ▼
           📄 Abstractive Summary
```

1. **Input Handling** — `app.py` captures user input via the Streamlit UI
2. **Text Extraction** — If a URL is given, `BeautifulSoup` scrapes and parses the article body
3. **Tokenization & Encoding** — The text is tokenized and passed to the BART encoder
4. **Summary Generation** — The BART decoder generates an abstractive summary using beam search
5. **Display** — The result is rendered back in the Streamlit interface

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| UI | [Streamlit](https://streamlit.io/) | Interactive web interface |
| NLP Model | [Hugging Face Transformers](https://huggingface.co/docs/transformers) | Model loading & inference |
| Summarizer | [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn) | Abstractive text summarization |
| Web Scraping | [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) | Extract article text from URLs |
| Deep Learning | [PyTorch](https://pytorch.org/) | Backend for transformer inference |
| Language | Python 3.8+ | Core language |

---

## 📂 Project Structure

```
summarize_news_article/
│
├── app.py              # Streamlit UI — handles input, output, and user interaction
├── main.py             # Core summarization logic using Hugging Face Transformers
├── requirements.txt    # Project dependencies
├── .gitignore          # Files excluded from version control
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python **3.8 or later** — [Download here](https://www.python.org/downloads/)
- `pip` package manager (included with Python)
- ~3 GB disk space (for the BART model, downloaded automatically on first run)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/alibutt2882/summarize_news_article.git
cd summarize_news_article
```

### Step 2 — Create a Virtual Environment (Recommended)

```bash
# Create
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS/Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit transformers torch beautifulsoup4 requests
```

### Step 4 — Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at **`http://localhost:8501`**

> **⚠️ Note:** On first run, the BART model (~1.6 GB) will be downloaded automatically from Hugging Face. This only happens once and is cached locally afterwards.

---

## 💻 Usage

1. **Launch** the app with `streamlit run app.py`
2. **Choose your input mode:**
   - Paste article text directly into the text box, **or**
   - Enter a news article URL (e.g. from BBC, CNN, Reuters)
3. **Click "Summarize"**
4. **Read your summary** — generated in seconds

---

## 📦 Requirements

```
streamlit
transformers
torch
beautifulsoup4
requests
```

> If a `requirements.txt` is not present in the repo, create one with the packages above or run `pip freeze > requirements.txt` after manual installation.

---

## 🔮 Model Details

This project uses **[`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)** — a fine-tuned version of BART (Bidirectional and Auto-Regressive Transformer) trained on the CNN/DailyMail news dataset.

| Property | Detail |
|---|---|
| Model Type | Encoder-Decoder Transformer (BART) |
| Task | Abstractive Summarization |
| Training Data | CNN/DailyMail dataset |
| Parameters | ~400M |
| Max Input Length | 1024 tokens |

**Abstractive** summarization means the model generates *new sentences* capturing the core meaning — not just copying sentences from the original text. This produces more natural, readable summaries.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get involved:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add: brief description of change"`
4. **Push** to your branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

Please keep PRs focused and include a clear description of what was changed and why.

---

## 🗺️ Roadmap

- [ ] Add `requirements.txt` to the repository
- [ ] Support for multiple summarization models (T5, Pegasus)
- [ ] Adjustable summary length slider
- [ ] Batch URL processing
- [ ] Copy-to-clipboard button for summaries
- [ ] Deployed demo on Streamlit Cloud

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full details.

---

## 👨‍💻 Author

**Ali Haider Butt**  

[![GitHub](https://img.shields.io/badge/GitHub-alibutt2882-181717?style=flat&logo=github)](https://github.com/alibutt2882)

---

<div align="center">
  <sub>If you found this useful, consider giving it a ⭐ — it helps others discover the project!</sub>
</div>
