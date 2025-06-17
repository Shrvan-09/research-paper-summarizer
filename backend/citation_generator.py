import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_citations(text, style="apa"):
    citations = set()
    
  
    years = re.findall(r'\b(?:19|20)\d{2}\b', text)
    
    if not years:
        return ["No valid years found for citations."]

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
          
            for year in years:
                name = ent.text.strip()
                if 3 <= len(name.split()) <= 4:  
                    if style == "apa":
                        citation = f"{name} ({year}). *Title unavailable*. Journal Name."
                    elif style == "mla":
                        citation = f"{name}. \"Title Unavailable.\" *Journal Name*, {year}."
                    else:
                        citation = f"{name} ({year})."
                    citations.add(citation)
                    break  

        if len(citations) >= 5:
            break

    return list(citations) if citations else [f"No citations found in {style.upper()} style."]
