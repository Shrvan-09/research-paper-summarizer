from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader

from summarizer import summarize_paper
from citation_generator import extract_citations
from evaluation import evaluate_summary  

from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu
import textstat
import bert_score

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # Save uploaded PDF to temporary file
        with open("temp.pdf", "wb") as f:
            f.write(contents)

        # Extract text from PDF
        reader = PdfReader("temp.pdf")
        full_text = " ".join(page.extract_text() or "" for page in reader.pages)

        # Run summarization and citation extraction
        summary = summarize_paper(full_text)
        citations = extract_citations(full_text)

   
        reference = full_text[:1000]
        evaluation = evaluate_summary(reference, summary)

        return JSONResponse(content={
            "summary": summary,
            "citations": citations,
            "evaluation": evaluation
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Evaluation 
def evaluate_summary(reference: str, generated: str):
    # ROUGE
    rouge = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_scores = rouge.score(reference, generated)

    # BLEU
    bleu = sentence_bleu([reference.split()], generated.split())

    # Readability
    flesch = textstat.flesch_reading_ease(generated)
    smog = textstat.smog_index(generated)

    # BERTScore
    P, R, F1 = bert_score.score([generated], [reference], lang="en", verbose=False)

    return {
        "ROUGE-1": round(rouge_scores['rouge1'].fmeasure, 4),
        "ROUGE-2": round(rouge_scores['rouge2'].fmeasure, 4),
        "ROUGE-L": round(rouge_scores['rougeL'].fmeasure, 4),
        "BLEU": round(bleu, 4),
        "BERTScore_F1": round(F1[0].item(), 4),
        "Flesch Reading Ease": round(flesch, 2),
        "SMOG Index": round(smog, 2)
    }


@app.post("/evaluate")
async def evaluate(
    generated_summary: str = Form(...),
    reference_summary: str = Form(...)
):
    try:
        scores = evaluate_summary(reference_summary, generated_summary)
        return JSONResponse(content={"metrics": scores})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
