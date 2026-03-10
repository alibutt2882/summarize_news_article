import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import BartForConditionalGeneration, BartTokenizer

# --- Page Configuration ---
st.set_page_config(page_title="Summarizer", page_icon="⚡", layout="wide")

# --- Neon CSS Styling ---
st.markdown("""
    <style>
    /* Main background and text */
    .stApp {
        background-color: #4A4646;
        color: #00ffc3;
    }

    /* Neon Titles */
    h1 {
        color: #EDF511 !important;
        text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Input boxes */
    .stTextInput input, .stTextArea textarea {
        background-color: #1a1a1a !important;
        color: #00ffc3 !important;
        border: 1px solid #00ffc3 !important;
        box-shadow: 0 0 5px #00ffc3;
    }

    /* Buttons */
    .stButton>button {
        background-color: transparent !important;
        color: #ff00ff !important;
        border: 2px solid #ff00ff !important;
        border-radius: 20px;
        box-shadow: 0 0 10px #ff00ff;
        transition: 0.3s;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff00ff !important;
        color: white !important;
        box-shadow: 0 0 20px #ff00ff;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #111 !important;
        border-right: 1px solid #ff00ff;
    }

    /* Success/Info boxes */
    .stAlert {
        background-color: #1a1a1a !important;
        border: 1px solid #00ffc3 !important;
        color: #00ffc3 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Load Model (Cached) ---
@st.cache_resource
def load_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# --- UI Header ---
st.markdown("<h1>📚 ARTICLE SUMMARIZER📄</h1>", unsafe_allow_html=True)
st.write("---")

# --- Input Section ---
input_type = st.radio("Select Input Method:", ("URL Link", "Direct Text Content"))

article_text = ""

if input_type == "URL Link":
    url = st.text_input("Paste News URL:", "")
    if st.button("Extract & Summarize"):
        with st.spinner("⚡ Intercepting Data..."):
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.content, 'html.parser')
                paragraphs = soup.find_all('p')
                article_text = " ".join([p.get_text() for p in paragraphs])
            except Exception as e:
                st.error(f"Signal Lost: {e}")
else:
    article_text = st.text_area("Paste your long text here:", height=200)
    if st.button("Process Text"):
        pass # The summarize logic below will trigger

# --- Summarization Logic ---
if article_text:
    if len(article_text) > 150:
        with st.spinner("🔮 Processing..."):
            # Limit to 10000 chars for performance
            inputs = tokenizer([article_text[:10000]], max_length=1024, return_tensors='pt', truncation=True)
            summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, min_length=50, early_stopping=True)
            summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            st.markdown("### 📝 Article Summary:")
            st.info(summary_text)

            st.success("Analysis Complete.")
    else:
        st.warning("Insufficient data. Please provide more text.")

# --- Sidebar ---
st.sidebar.markdown("<h2 style='color:#ff00ff;'>System Status</h2>", unsafe_allow_html=True)
st.sidebar.write("**Model:** BART-Large-CNN")
st.sidebar.write("**Status:** Operational")
st.sidebar.write("---")
st.sidebar.info("Built by Ali Haider Butt")