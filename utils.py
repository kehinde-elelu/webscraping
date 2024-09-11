import re

def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove special characters, numbers, and punctuation (keeping spaces and alphabets)
    text = re.sub(r'[^a-z\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def split_into_sentences_and_words(text):
    # Split text into sentences based on periods (.)
    sentences = re.split(r'\.|\n', text)
    
    # Tokenize each sentence into words
    corpus = [sentence.split() for sentence in sentences if sentence]

    return corpus