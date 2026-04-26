import fitz
import re

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_text(text):
    skills = re.findall(
    r'\b(Python|Java|AWS|NLP|ML|SQL|Docker|Kubernetes|TensorFlow|React|HTML|CSS|JavaScript)\b',
    text,
    re.I
)
    experience = re.findall(r'(\d+)\+?\s+years', text)
    return {
        "skills": list(set(skills)),
        "experience": int(experience[0]) if experience else 1
    }
