import pdfplumber
import re

def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_email(text):
    match = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return match[0] if match else "Not Found"

def extract_phone(text):
    match = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    return match[0] if match else "Not Found"

def extract_name(text):
    lines = text.strip().split('\n')
    return lines[0].strip() if lines else "Not Found"

def extract_skills(text):
    skills_list = [
        "Python", "Java", "C++", "C", "JavaScript", "HTML", "CSS",
        "SQL", "Machine Learning", "Deep Learning", "Flask", "Django",
        "React", "Node.js", "Git", "Linux", "Excel", "R", "Kotlin"
    ]
    found = [s for s in skills_list if s.lower() in text.lower()]
    return found if found else ["Not Found"]

def parse_resume(file_path):
    text = extract_text(file_path)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }