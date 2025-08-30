# Agentic AI - Agentic AI for Computer Vision Course

This project is an **agentic AI system** designed to assist educators teaching a Computer Vision course by automating the generation of exam questions from lecture materials and evaluating student answer scripts. 

---

## Technology Stack

- Python 3.x
- [Streamlit](https://streamlit.io) for the web UI
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF text extraction
- OpenAI Python client configured to use [PerplexityPro API](https://www.perplexity.ai)
- Environment variables for secure API key management

---

## Setup Instructions

1. **Clone the repo:**
    ```
    git clone https://github.com/bdhani/CV-Agentic-AI-Assignment.git
    cd CV-Agentic-AI-Assignment
    ```

2. **Create and activate a virtual environment:**
   - Windows:
     ```
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Add your Perplexity API key:**
   - Create a `.env` file in the project root with the line
     ```
     PERPLEXITY_API_KEY=your_api_key_here
     ```
   - Or set environment variable directly:
     - Windows PowerShell:
       ```
       setx PERPLEXITY_API_KEY "your_api_key_here"
       ```
     - macOS/Linux (in terminal config file):
       ```
       export PERPLEXITY_API_KEY="your_api_key_here"
       ```

5. **Run the Streamlit app:**
    ```
    streamlit run app.py
    ```

---

## Usage

- **Generate Questions Tab:** Upload your Computer Vision lecture PDF and click "Generate Questions" to receive AI-created exam questions.
- **Evaluate Answers Tab:** Upload both the course PDF and student answer PDF, then click "Evaluate Answers" to get detailed grading and feedback.

---

## Notes

- This app requires a valid **Perplexity Pro API key** for full access. Users must obtain their own keys for independent usage.
- The AI model used is `"sonar-pro"` from PerplexityPro.

---


