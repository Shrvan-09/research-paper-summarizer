
# 🔍 Research Paper Summarizer

This project is a web-based summarizer designed to generate concise summaries from research papers (PDF files). It leverages powerful transformer models like **PEGASUS** or **DistilBERT** to extract and summarize content.

---

## ✔ Features

- Upload and parse research paper PDFs
- Summarize content using fine-tuned NLP models
- Clean and readable interface
- Fast backend powered by Python and deep learning

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Shrvan-09/research-paper-summarizer.git
cd research-paper-summarizer
```

---

## ⚙️ Backend Setup

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Required Models Manually

⚠️ **Important**: You must manually download the following models and place them in the `backend/models/` directory.

#### a) PEGASUS

- Model: `google/pegasus-xsum`
- Download from: https://huggingface.co/google/pegasus-xsum
- Place the downloaded model files into:
  ```
  backend/models/pegasus/
  ```

#### b) DistilBERT

- Model: `distilbert-base-uncased`
- Download from: https://huggingface.co/distilbert-base-uncased
- Place the downloaded model files into:
  ```
  backend/models/distilbert/
  ```

> 📌 Make sure both models contain `config.json`, `pytorch_model.bin`, and tokenizer files.

---

## 🌐 Frontend Setup

### 4. Install Node.js Dependencies

Go to the frontend folder and run:

```bash
cd frontend
npm install
```

### 5. Start the Frontend App

```bash
npm start
```

By default, the frontend will be served at:

```
http://localhost:3000/
```

---

## ▶️ Running the Backend Application

From the root project folder:

```bash
cd backend
python app.py
```

This will start the backend server ( FastAPI). Access it at:

```
http://localhost:5000/
```

---

## 🛠 Dependencies

- Python 3.7+
- Flask / FastAPI
- HuggingFace Transformers
- PyPDF2 / pdfminer
- Torch
- Node.js & React (Frontend)

---

## 📬 Contact

For issues or enhancements, feel free to open an issue or contribute via pull requests.

---
