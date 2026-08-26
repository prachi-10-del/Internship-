import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

st.title("📄 Resume Matcher")
st.write("Upload your resume and compare it with a job description.")

# Upload Resume
resume_file = st.file_uploader("📤 Upload Resume PDF", type="pdf")

# Job Description
job = st.text_area("📝 Enter Job Description")


# Extract text from PDF
def get_resume_text(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# Clean text
def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text


# Match Resume and Job
def calculate_match(resume, job):

    vectorizer = TfidfVectorizer(stop_words="english")

    data = vectorizer.fit_transform([resume, job])

    score = cosine_similarity(data[0], data[1])[0][0]

    return score


# Match Button
if st.button("🔍 Match Resume"):

    if resume_file is None:
        st.error("Please upload your resume.")

    elif job.strip() == "":
        st.error("Please enter a job description.")

    else:

        # Read resume
        resume = get_resume_text(resume_file)

        # Clean both texts
        resume = clean(resume)
        job = clean(job)

        # Calculate score
        score = calculate_match(resume, job)

        # Show result
        percentage = score * 100

        st.subheader("📊 Match Result")

        st.metric(
            "Resume Match Score",
            f"{percentage:.0f}%"
        )

        if percentage >= 70:
            st.success("🎉 Excellent Match!")

        elif percentage >= 50:
            st.warning("👍 Good Match!")

        else:
            st.error("❌ Low Match")

        # Show resume text
        st.subheader("📄 Resume Text")

        with st.expander("View Resume"):
            st.write(resume)