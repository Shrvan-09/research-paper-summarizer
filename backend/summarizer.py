from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import fitz  
import tempfile
import os
import re
import torch
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

# CUDA debugging (optional)
os.environ["CUDA_LAUNCH_BLOCKING"] = "1"

# Load model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("models/pegasus").to("cuda")
tokenizer = AutoTokenizer.from_pretrained("models/pegasus")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=0)

# FastAPI app
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text) 
    text = re.split(r'(?:References|REFERENCES)', text)[0]  
    return text.strip()

# Word-based chunking
def chunk_text(text, max_tokens=500):  
    words = text.split()
    for i in range(0, len(words), max_tokens):
        yield " ".join(words[i:i + max_tokens])

def summarize_paper(text):
    text = clean_text(text)
    chunks = list(chunk_text(text))
    summaries = []
    for idx, chunk in enumerate(chunks):
        try:
            print(f"Summarizing chunk {idx+1}/{len(chunks)}...")
            summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
            summaries.append(summary)
        except Exception as e:
            print(f"Error in chunk {idx+1}: {e}")
            summaries.append("[Error summarizing this section.]")
    return " ".join(summaries)

# PDF Summarization API
@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(contents)
            tmp_path = tmp.name

        # Extract text
        doc = fitz.open(tmp_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        os.remove(tmp_path)

        # Summarize the extracted text
        summary = summarize_paper(text)

        # Placeholder citations
        citations = [
            "Doe, J. (2023). Placeholder Citation 1.",
            "Smith, A. (2022). Placeholder Citation 2."
        ]

        return JSONResponse(content={
            "summary": summary,
            "citations": citations
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
