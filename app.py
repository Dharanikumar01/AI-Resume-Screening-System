import streamlit as st

from utils.skill_extractor import (
    extract_email,
    extract_phone,
    extract_skills,
    find_missing_skills
)

from utils.pdf_reader import extract_text_from_pdf
from utils.text_preprocessing import preprocess_text
from utils.similarity import calculate_similarity

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening System")

uploaded_files = st.file_uploader(
    "Upload Resume(s)",
    type=["pdf"],
    accept_multiple_files=True
)

job_description = st.text_area(
    "Enter Job Description"
)

if uploaded_files and job_description:

    results = []

    for uploaded_file in uploaded_files:

        # Extract Resume Text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Preprocess
        cleaned_resume = preprocess_text(resume_text)
        cleaned_job = preprocess_text(job_description)

        # Similarity Score
        score = calculate_similarity(
            cleaned_resume,
            cleaned_job
        )

        # Candidate Details
        email = extract_email(resume_text)
        phone = extract_phone(resume_text)
        skills = extract_skills(resume_text)
        missing = find_missing_skills(
            resume_text,
            job_description
        )

        results.append({
            "Resume": uploaded_file.name,
            "Score": float(score),
            "Email": email,
            "Phone": phone,
            "Skills": skills,
            "Missing": missing
        })

    # Sort by Highest Score
    results.sort(
        key=lambda x: x["Score"],
        reverse=True
    )

    st.header("🏆 Resume Rankings")

    for i, result in enumerate(results, start=1):

        st.markdown("---")

        st.subheader(f"👤 Candidate {i}")

        st.write(f"**Resume:** {result['Resume']}")

        # Match Score
        st.metric(
            "Match Score",
            f"{result['Score']:.2f}%"
        )

        # Progress Bar (0-100)
        progress_value = int(round(result["Score"]))

        if progress_value < 0:
            progress_value = 0
        elif progress_value > 100:
            progress_value = 100

        st.progress(progress_value)

        # Email & Phone
        col1, col2 = st.columns(2)

        with col1:
            st.info(f"📧 {result['Email']}")

        with col2:
            st.info(f"📱 {result['Phone']}")

        # Skills
        st.subheader("✅ Skills")

        if result["Skills"]:
            for skill in result["Skills"]:
                st.success(skill)
        else:
            st.warning("No skills detected.")

        # Missing Skills
        st.subheader("❌ Missing Skills")

        if result["Missing"]:
            for skill in result["Missing"]:
                st.error(skill)
        else:
            st.success("No Missing Skills 🎉")

        st.divider()