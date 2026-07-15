import re

# Add more skills as you learn new technologies
SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai",
    "ml",
    "nlp",
    "computer vision",
    "tensorflow",
    "pytorch",
    "keras",
    "opencv",
    "numpy",
    "pandas",
    "scikit-learn",
    "streamlit",
    "flask",
    "django",
    "langchain",
    "faiss",
    "chroma",
    "llm",
    "rag"
]

def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"

def extract_phone(text):
    pattern = r'(\+?\d{1,3}[\s\-]?)?(?:\(?\d+\)?[\s\-]?){6,14}\d'

    match = re.search(pattern, text)

    if match:
        return match.group().strip()

    return "Not Found"


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))

def find_missing_skills(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))
    print("Resume Skills:", resume_skills)
    print("Job Skills:", job_skills)
    missing = sorted(list(job_skills - resume_skills))

    return missing