import streamlit as st
import fitz  # PyMuPDF for PDF extraction
import pandas as pd
from model import JobRecommendationSystem

st.title("AI-Powered Job Recommendation System")
st.write("Upload your resume as a PDF file, and get 20 job recommendations tailored to you!")

# ✅ Cache the model to prevent reloading every time
@st.cache_resource
def load_recommender():
    return JobRecommendationSystem("JobsFE.csv")

recommender = load_recommender()

# File uploader for PDF resume
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF resume"""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text.strip()

resume_text = ""

if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ Resume text extracted successfully!")

if st.button("Recommend Jobs"):
    if resume_text:
        with st.spinner("Analyzing your resume and finding best job matches..."):
            recommendations = recommender.recommend_jobs(resume_text, top_n=20)
            job_results = recommendations.get("recommended_jobs", [])

        if job_results:
            st.success(f"Found {len(job_results)} job recommendations for you!")
            for i, job in enumerate(job_results, start=1):
                st.subheader(f"Job {i}: {job.get('position', 'N/A')}")
                st.write(f"**Company:** {job.get('workplace', 'N/A')}")
                st.write(f"**Mode:** {job.get('working_mode', 'N/A')}")
                st.write(f"**Duties:** {job.get('job_role_and_duties', 'N/A')}")
                st.write(f"**Required Skills:** {job.get('requisite_skill', 'N/A')}")
                st.write("---")
        else:
            st.warning("No jobs found. Please try a different resume.")
    else:
        st.warning("Please upload a valid PDF resume before proceeding.")
