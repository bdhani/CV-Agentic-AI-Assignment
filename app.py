import os
import pdfplumber
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

api_key = os.getenv("PERPLEXITY_API_KEY")


# Setup
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Initialize PerplexityPro client
client = OpenAI(
    api_key=api_key,  # set your PerplexityPro API key in env variable PERPLEXITY_API_KEY
    base_url="https://api.perplexity.ai"
)


# -------- Helpers --------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text


def generate_questions(course_text):
    prompt = f"""
    You are an exam creator for a Computer Vision course. 
    Given the following material:
    {course_text}


    Generate 8 unique questions:
    - 3 MCQs with options
    - 2 short-answer
    - 2 descriptive
    - 1 problem-solving scenario
    Do not repeat questions if asked again.
    """
    resp = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return resp.choices[0].message.content


def evaluate_answers(student_answers, course_text):
    prompt = f"""
    You are a Computer Vision professor. 
    Grade the student's answers based on the reference material.


    Course Reference:
    {course_text}


    Student Answers:
    {student_answers}


    Provide:
    - Marks out of 100
    - Detailed feedback (strengths + weaknesses)
    - Suggestions for improvement
    """
    resp = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return resp.choices[0].message.content


# -------- Streamlit UI --------
st.set_page_config(page_title="Teacher AI - Computer Vision", layout="wide")
st.title("📘 Teacher AI Tool for Computer Vision")


tabs = st.tabs(["📝 Generate Questions", "📊 Evaluate Student Answers"])


# --- Tab 1: Generate Questions ---
with tabs[0]:
    st.header("Upload Course Material (PDF)")
    course_file = st.file_uploader("Upload PDF", type=["pdf"], key="course_pdf1")

    if course_file is not None:
        if st.button("Generate Questions"):
            course_text = extract_text_from_pdf(course_file)
            questions = generate_questions(course_text)
            st.subheader("Generated Test Questions")
            st.text_area("Questions", questions, height=400)


# --- Tab 2: Evaluate Student Answers ---
with tabs[1]:
    st.header("Upload Course Material + Student Answers (PDFs)")
    course_file2 = st.file_uploader("Upload Course PDF", type=["pdf"], key="course_pdf2")
    ans_file = st.file_uploader("Upload Student Answer PDF", type=["pdf"], key="ans_pdf")

    if course_file2 is not None and ans_file is not None:
        if st.button("Evaluate Answers"):
            course_text = extract_text_from_pdf(course_file2)
            student_text = extract_text_from_pdf(ans_file)
            evaluation = evaluate_answers(student_text, course_text)
            st.subheader("Evaluation Report")
            st.text_area("Report", evaluation, height=400)
