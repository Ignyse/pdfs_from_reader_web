import re

def strict_clean(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9\s.,;:!?()'“”’\"\-+=]", "", text)
def preprocess(text: str) -> str:
    text = text.replace("…", "...")
    # text = text.replace("“", '"').replace("”", '"')
    text = text.replace(" ‘ ", "’")
    text = text.replace("‘", "’")
    # text = text.replace("-","-")
    # text = text.replace("–", "-")
    return text

def clean(text: str) -> str:
    text = preprocess(text)
    return strict_clean(text)