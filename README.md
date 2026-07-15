# 📄 AI Resume Screening System

An AI-powered Resume Screening System built using **Python**, **Streamlit**, and **Sentence Transformers**. This application analyzes resumes, compares them with a job description, calculates a match score, extracts candidate information, and ranks multiple resumes based on their relevance.

---

## 🚀 Features

- 📄 Upload one or multiple PDF resumes
- 📝 Enter a job description
- 🤖 AI-based resume matching using Sentence Transformers
- 📊 Resume match score with progress bar
- 📧 Extract candidate email
- 📱 Extract phone number
- 💻 Extract technical skills
- ❌ Identify missing skills
- 🏆 Rank multiple resumes based on similarity
- 🎨 Interactive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Sentence Transformers
- Scikit-learn
- Pandas
- NumPy
- PyMuPDF
- NLTK
- phonenumbers

---

## 📂 Project Structure

```
AI-Resume-Screening-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── pdf_reader.py
│   ├── similarity.py
│   ├── skill_extractor.py
│   └── text_preprocessing.py
│
├── data/
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-System.git
```

### Go to the project folder

```bash
cd AI-Resume-Screening-System
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📌 How It Works

1. Upload one or more PDF resumes.
2. Enter the job description.
3. The application extracts text from resumes.
4. Text is preprocessed using NLP techniques.
5. Sentence Transformers generate embeddings.
6. Cosine similarity is used to calculate the match score.
7. Candidate details and skills are extracted.
8. Missing skills are identified.
9. All resumes are ranked based on similarity.

---

## 📈 Future Enhancements

- Resume feedback using LLMs
- Skill recommendation system
- Resume summary generation
- CSV/PDF report export
- Dashboard with analytics
- Database integration
- User authentication

---

## 🎯 Skills Demonstrated

- Natural Language Processing (NLP)
- Sentence Embeddings
- Semantic Similarity
- Machine Learning
- PDF Text Extraction
- Data Preprocessing
- Information Extraction
- Streamlit Application Development
- Python Programming

---

## 👨‍💻 Author

**Dharani Kumar**

GitHub: https://github.com/Dharanikumar01



---

## ⭐ If you found this project useful, consider giving it a star!