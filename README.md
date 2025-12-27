# Resume Parser

## Problem Statement
Recruiters receive large volumes of resumes in unstructured formats such as PDFs, making manual screening time-consuming and inefficient. There is a need for an automated system that can extract key candidate information in a structured format.

## Solution Overview
Resume Parser is a lightweight AI-assisted web application that extracts structured information from PDF resumes. The system converts unstructured resume content into machine-readable JSON, enabling faster screening and integration with ATS systems.

## Features
- Upload PDF resumes
- Extract raw text from resumes
- Identify candidate name, email, and phone number
- Extract and normalize technical skills
- Display structured JSON output

## Tech Stack
- Python
- Flask
- PDFPlumber
- HTML, CSS, JavaScript

## How It Works
1. User uploads a PDF resume through the web interface
2. The backend extracts text from the PDF
3. NLP logic identifies basic candidate details
4. Skill extraction module matches and normalizes skills
5. Structured JSON output is returned to the user

## Project Structure
resume-parser/
├── app.py
├── ocr.py
├── nlp.py
├── skills.py
├── index.html
├── requirements.txt
└── README.md

## Output Example
{
"basic_info": {
"name": "John Doe",
"email": "john@example.com",
"phone": "+91XXXXXXXXXX"
},
"skills": [
"Python",
"Machine Learning",
"SQL"
]
}

## Use Cases
- Resume screening for recruiters
- Applicant Tracking Systems
- Campus placement automation
- Candidate profile generation

## Future Enhancements
- Google Vision OCR for scanned resumes
- Vertex AI NLP for advanced entity extraction
- Resume scoring and ranking
- Multi-language resume support
- Cloud deployment and scalability

## Team
Built as part of a hackathon prototype to demonstrate fast, scalable resume parsing using AI-assisted techniques.