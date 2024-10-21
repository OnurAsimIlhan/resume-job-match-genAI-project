# Job Description - Resume Analyzer GenAI Project

This is a Streamlit application designed to help users improve their resumes by evaluating them against job descriptions using a generative AI model. The application extracts text from uploaded PDF resumes and provides feedback on how well the resume matches the job description, including missing keywords and a profile summary.

## Features

- Upload a PDF resume and paste a job description.
- Evaluate the resume against the job description using a generative AI model.
- Receive feedback on the percentage match, missing keywords, and a profile summary.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Paste the job description in the provided text area.

4. Upload your resume in PDF format.

5. Click the "Submit" button to receive feedback on your resume.
