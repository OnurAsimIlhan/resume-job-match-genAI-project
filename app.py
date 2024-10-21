import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
You are an advanced Application Tracking System (ATS) designed to evaluate resumes in the technology 
field (software engineering, data science, data analysis, big data engineering) against specific job descriptions. 
The current job market is highly competitive, so your goal is to provide precise feedback on how well the 
resume matches the job description and suggest improvements.
Your task:
- Assess the resume based on the job description (JD).
- Identify the percentage match between the resume and the JD.
- Highlight missing or insufficient keywords/skills from the JD.

Evaluate the following:
resume:{text}
description:{jd}

The structure of your response should be:
{{"JD Match":"X%","MissingKeywords":["keyword1", "keyword2", ...],"Profile Summary":"A brief overview of the resume's alignment with the job description, highlighting strengths and areas to improve."}}
"""

## streamlit app
st.title("ATS Scanner")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)
