from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer
import os

print("Downloading Pegasus summarizer model...")
pegasus_path = "models/pegasus"
os.makedirs(pegasus_path, exist_ok=True)
model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-cnn_dailymail")
tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
model.save_pretrained(pegasus_path)
tokenizer.save_pretrained(pegasus_path)

print("Downloading DistilBERT model for KeyBERT...")
distilbert_path = "models/distilbert-keybert"
os.makedirs(distilbert_path, exist_ok=True)
sentence_model = SentenceTransformer("distilbert-base-nli-mean-tokens")
sentence_model.save(distilbert_path)

print("All models downloaded and saved locally!")
