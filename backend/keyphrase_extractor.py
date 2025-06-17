from keybert import KeyBERT
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("models/distilbert-keybert")
kw_model = KeyBERT(model=model)

def extract_keyphrases(text):
    keyphrases = kw_model.extract_keywords(text, top_n=10)
    return [kw[0] for kw in keyphrases]
