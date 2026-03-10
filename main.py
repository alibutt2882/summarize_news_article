import requests
from bs4 import BeautifulSoup
import sys

# 1. Loading the Brains (NLP Models)
print("--- [ SYSTEM ] ---")
print("Loading Neural Networks... Please wait.")
try:
    from transformers import BartForConditionalGeneration, BartTokenizer
    import torch
except ImportError:
    print("Error: Required libraries not found. Run: pip install transformers torch requests beautifulsoup4")
    sys.exit()

# Load model and tokenizer once at the start
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def get_text_from_url(url):
    """
    Scrapes text while bypassing basic bot detection using Headers.
    """
    # Mimic a real Chrome Browser to bypass security blocks
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    }

    try:
        print(f"[*] Connecting to: {url}...")
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 403:
            print("[-] Access Denied: The website blocked the script. Try pasting the text manually.")
            return None
            
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')

        # Target only paragraph tags to filter out menu links and ads
        paragraphs = soup.find_all('p')
        article_text = " ".join([p.get_text() for p in paragraphs])
        return article_text
    except Exception as e:
        print(f"[-] Error during fetch: {e}")
        return None

def run_summarizer():
    print("\n" + "═"*40)
    print("      SOFTGROW TECH: NEON SUMMARIZER      ")
    print("═"*40)
    print("1. https://en.wikipedia.org/wiki/Mode_%28statistics%29 - Scrape and summarize a news link")
    print("2. [TEXT MODE] - Summarize text you paste directly")
    
    choice = input("\nSelect Mode (1 or 2): ").strip()

    if choice == '1':
        url = input("Paste URL: ").strip()
        text_to_process = get_text_from_url(url)
    elif choice == '2':
        print("Paste your text (Press Enter twice to finish):")
        text_to_process = input("> ").strip()
    else:
        print("Invalid Selection.")
        return

    # Check if we actually got text
    if not text_to_process or len(text_to_process) < 150:
        print("\n[!] Error: Not enough content to process.")
        return

    print("\n[*] Running Abstractive Summarization...")
    
    # Tokenize and Generate
    # We truncate to 1024 tokens (BART limit)
    inputs = tokenizer([text_to_process[:4000]], max_length=1024, return_tensors='pt', truncation=True)
    
    summary_ids = model.generate(
        inputs['input_ids'], 
        num_beams=4, 
        max_length=150, 
        min_length=40, 
        early_stopping=True
    )
    
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    print("\n" + "⚡"*20)
    print("DECODED SUMMARY:")
    print("⚡"*20)
    print(f"\n{summary_text}\n")
    print("═"*40)

if __name__ == "__main__":
    while True:
        run_summarizer()
        cont = input("Summarize another? (y/n): ").lower()
        if cont != 'y':
            break